var pioneerApp = angular.module('pioneerRemoteApp', []);

pioneerApp.controller('ButtonListCtrl', ['$scope', '$http', function ($scope) {

	$http.get('devices.json')
        .success(function(data) {
        		console.log(data)
        })
        .error(function(data,status,error,config){
        	console.log(data)
        	console.log(status)
        	console.log(error)
        });
  $scope.buttons = [
    {'name': 'Volume UP',
     'action': 'VU'},
     {'name': 'Volume Down',
   		'action': 'VD'}
  ];
  $scope.send_cmd = function(cmd){
  	jQuery.get('run/'+ cmd)
  }
}]);