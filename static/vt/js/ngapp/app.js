'use strict';

var nwayapp = angular.module("nwayApp", ["nwayApp.controllers", "ngRoute"]);


nwayapp.config(['$routeProvider',
	
  function($routeProvider) {
	  $routeProvider.
	    when('/login', {
	      templateUrl: 'login.html',
	      controller: 'RegistrationCtrl'
	    }).
	    when('/register', {
	      templateUrl: 'register.html',
	      controller: 'RegistrationCtrl'
	    }).
	    otherwise({
	      redirectTo: '/login'
	    });
}]);