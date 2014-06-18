'use strict';

var controllers = angular.module("nwayApp.controllers", ["ui.bootstrap"]);

controllers.controller("DashboardTabsCtrl", ["$scope",
      function($scope){
      	  $scope.tabs = [
    		{ title:'List', content:'Dynamic content 1' },
    		{ title:'New', content:'Dynamic content 2' }
  			];  
}]);  