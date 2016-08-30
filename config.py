import logging.config
import json
import os
import pymongo
from pymongo import MongoClient


def setup_logging():
    logging.config.fileConfig('logging.conf', defaults={})
    logger = logging.getLogger('solarViz')
    logger.setLevel(logging.DEBUG)
    return logger


def setup_db():
    mongo_url = os.getenv('MONGODB_URI', None)
    if mongo_url:
        db_name = mongo_url.split('/')[-1]
    else:
        vcap_services = json.loads(os.getenv("VCAP_SERVICES"))
        mongo_url = vcap_services["mongodb"][0]["credentials"]["uri"]
        db_name = vcap_services["mongodb"][0]["credentials"]["database"]

    db = MongoClient(mongo_url)[db_name]

    log_collection = db.log
    #log_collection.ensure_index([('type', pymongo.ASCENDING)])
    log_collection.create_index("sourceId")
    log_collection.create_index("time")

    return db
