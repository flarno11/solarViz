import re
import json
import datetime
import os
import urllib
from datetime import timedelta
from time import sleep

import pymongo
from flask import Flask, redirect, url_for, jsonify, request
from bson.objectid import ObjectId

from config import setup_logging, setup_db
from lib import TimeFormat
import smartMe

logger = setup_logging()
db = setup_db()
log_collection = db.log

time_before_2nd_panel = datetime.datetime(year=2016, month=3, day=18)


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        elif isinstance(o, datetime.datetime):
            return o.strftime(TimeFormat)
        return json.JSONEncoder.default(self, o)


class InvalidAPIUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv

app = Flask(__name__)


@app.errorhandler(InvalidAPIUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/smartMeImport', methods=['POST'])
def route_import():
    client_data = request.get_json(force=True)
    dates_from_to = smartMe.import_data(client_data['username'], client_data['password'], client_data['deviceId'], log_collection)
    return jsonify({'error': None, 'importFromTo': dates_from_to})


@app.route('/data/<device_id>/years')
def data_years(device_id):
    return get_data(device_id, "%Y")


@app.route('/data/<device_id>/months')
def data_months(device_id):
    return get_data(device_id, "%Y-%m")


@app.route('/data/<device_id>/weeks')
def data_weeks(device_id):
    return get_data(device_id, "%Y-%U")


@app.route('/data/<device_id>/days')
def data_days(device_id):
    return get_data(device_id, "%Y-%m-%d")


@app.route('/data/<device_id>/hours')
def data_hours(device_id):
    return get_data(device_id, "%Y-%m-%d %H")


def get_data(device_id, aggregation_date_format):
    def create_item(c):
        t = c['_id']
        watt_hours = c['wattHours']
        #if t < time_before_2nd_panel:
        #    watt_hours = watt_hours * 2
        return {'time': t, 'wattHours': watt_hours}

    return jsonify([create_item(c) for c in log_collection.aggregate([
        {'$match': {'deviceId': device_id}},
        {'$project': {'date': {'$dateToString': {'format': aggregation_date_format, 'date': "$time"}}, 'wattHours': '$wattHours'}},
        {'$group': {'_id': '$date', 'wattHours': {'$sum': '$wattHours'}}},
        {'$sort': {'_id': pymongo.DESCENDING}},
        {'$limit': 50},
        {'$sort': {'_id': pymongo.ASCENDING}},
    ])])


app.json_encoder = JSONEncoder


if __name__ == "__main__":
    # port = int(os.getenv("VCAP_APP_PORT", "-1"))
    app.run()
