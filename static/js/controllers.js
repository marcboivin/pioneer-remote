var pioneerApp = angular.module('pioneerRemoteApp', []);

pioneerApp.controller('ButtonListCtrl', ['$scope', '$http', function ($scope, $http) {

	$scope.buttons = []

	$http.get('/static/js/devices.json')
        .success(function(data) {
        		console.log(data)
        		$scope.buttons = data.PIONEERSC1228.commands
        })
        .error(function(data,status,error,config){
        	console.log(data)
        	console.log(status)
        	console.log(error)
        });
        
  $scope.send_cmd = function(cmd){
  	jQuery.get('run/'+ cmd)
  }
}]);