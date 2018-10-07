angular.module("myApp", ['ngRoute', 'ngMaterial', 'suc.charts',])

.config(function($mdThemingProvider) {
  $mdThemingProvider.theme('default')
    .primaryPalette('red')
    .accentPalette('red');
})
.config(function($mdProgressCircularProvider) {
  $mdProgressCircularProvider.configure({
    progressSize: 20,
  });
})

.config(function($routeProvider) {
    $routeProvider
    .when("/", {
        templateUrl : "/static/home.html",
        controller : "homeController"
    })
    ;
})

.service('toaster', function($mdToast) {
    var last = {
      bottom: false,
      top: true,
      left: true,
      right: false
    };
    var toastPosition = angular.extend({},last);
    function getToastPosition() {
        sanitizePosition();
        return Object.keys(toastPosition)
          .filter(function(pos) { return toastPosition[pos]; })
          .join(' ');
    };
    function sanitizePosition() {
        var current = toastPosition;
        if ( current.bottom && last.top ) current.top = false;
        if ( current.top && last.bottom ) current.bottom = false;
        if ( current.right && last.left ) current.left = false;
        if ( current.left && last.right ) current.right = false;
        last = angular.extend({},current);
    }

    this.showSimpleToast = function(text) {
        var pinTo = getToastPosition();
        $mdToast.show(
            $mdToast.simple()
                .textContent(text)
                .position(pinTo)
                .hideDelay(3000)
        );
    };
})

.controller('navController', function($scope, $location, $log) {
})

.controller('homeController', function($scope, $q, $log, $http, $timeout, $window, toaster) {
    $scope.deviceId = '4ea9ec0b-b26b-467c-af63-e5912aebd3af';
})

.directive('chart', function($log, $http) {
	return {
	    restrict : "A",
		scope: {
			deviceId: '=',
            type: '@'
		},
		link: function($scope, $elem, $attrs) {
            $scope.chartOptions = {
                my_firstRowContainsLabels: true,
                displayAnnotations: true,
                title: $scope.type
            };

            var loadData = function(aggregationType, deviceId) {
                if (aggregationType != undefined && deviceId != undefined) {
                    $scope.loading = true;
                    $http.get('/data/' + deviceId + '/' + aggregationType).then(function successCallback(response) {
                        $scope.loading = false;
                        var r = response.data.map(function (d) { return [d.time, d.wattHours / 1000]; });
                        r.unshift(["Time", "kWh"]);
                        $scope.data = r;
                    }, function errorCallback(response) {
                        $scope.loading = false;
                        $log.error(response);
                    });
                }
            };

            loadData($scope.type, $scope.deviceId);
		},
		templateUrl: '/static/chart.html'
	};
})

;
