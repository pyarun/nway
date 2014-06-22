'use strict';

var controllers = angular.module("nwayApp.controllers", ["ui.bootstrap", , "ngCookies"]);

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

controllers.controller("RegistrationCtrl", ["$scope", "$http", "$log", "$cookies", "$location", "$timeout", 
            function($scope, $http, $log, $cookies, $location, $timeout){
	
	$scope.registerUser = function(){
		$log.debug("registerUser function called");
		
		function passwordMatch(){
			return $scope.registrationModel.password1 == $scope.registrationModel.password2;
		}
		
		if($scope.registrationform.$valid && passwordMatch()){
			
			var postData = angular.element.param($scope.registrationModel);
			
			$http.post(Urls.registration_register(), postData, {
	          headers:{"Content-Type": "application/x-www-form-urlencoded",
	            "X-CSRFToken":$cookies['csrftoken']
	            }
	     }).success(function(response, status, headers, config){
	    	 $log.debug("user registered");
	    	 $scope.alert = {
	    			 type:"success",
	    			 msg:"Thankyou for Registering. In few seconds you will be directed to login page."
	    	 }
	    	 function redirect(){
	    		 
	    		 window.location.replace(response.redirect_url)
	    	 }
	    	 
	    	 $timeout(redirect, 5000);
	    	 
	     }).error(function(response, status, headers, config){
	    	 $log.debug("Status: " + status);
	    	 $log.debug("headers: " + headers);
	    	 $log.debug("config: " + config);
	    	 $log.debug("response: " + response);
	     });
		}else{
			$scope.showFormErrors = true;
		}
		
	}
	
}]);

controllers.controller("AuthCtrl", ["$scope", function($scope){

}]);

