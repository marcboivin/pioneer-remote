var pioneerApp = angular.module('pioneerRemoteApp', []);

pioneerApp.controller('ButtonListCtrl', ['$scope', '$http', function ($scope) {
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