'use strict';

angular.module('todoListApp')
.directive('todo', function(){
  return {
  	/*
  	===========================
  	CHANGE
  	
  	// Added /static to templateUrl
  	===========================
  	 */
    templateUrl: '/static/templates/todo.html',
    replace: true,
    controller: 'todoCtrl'
  }
});