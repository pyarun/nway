'use strict';

var controllers = angular.module("nwayApp.controllers", ["ui.bootstrap"]);

controllers.controller("DashboardTabsCtrl", ["$scope", function($scope){
      	   
}]);  

controllers.controller("AddItemCtrl", ["$scope", "$http", function($scope, $http){
  $scope.status = {
      isopen: false
    };
  
	function getCategories(){
		$http.get("/api/products/").success(function(response){
			$scope.productCategories=response;
		});
	}
	getCategories();
	
}]);  

