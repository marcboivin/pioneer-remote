var pioneerApp = angular.module('pioneerRemoteApp', []);

pionnerApp.controller('ButtonListCtrl', function ($scope) {
  $scope.buttons = [
    {'name': 'Volume UP',
     'action': 'UP'},
  ];
});