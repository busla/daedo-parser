    var tkdApp = angular.module('tkdApp', []);
     
    phonecatApp.controller('FightListCtrl', ['$scope', '$http',
    function ($scope, $http) {
    $http.get('test.json').success(function(data) {
    $scope.fights = data;
    });
     
    $scope.orderProp = 'Start';
    }]);