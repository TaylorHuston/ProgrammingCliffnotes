var demoApp = angular.module('demoApp', []); //Empty array is for dependencies

demoApp.controller('demoController', function ($scope) {
  function SomeController($scope) {
    $scope.people = [{
      name: 'Al',
      state: 'Oklahoma'
      }, {
      name: 'Bob',
      state: 'Alaska'
      }, {
      name: 'Cat',
      state: 'Colorado'
      }]
  }


});
