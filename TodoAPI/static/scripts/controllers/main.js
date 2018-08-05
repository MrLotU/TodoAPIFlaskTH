'use strict';

angular.module('todoListApp')
.controller('mainCtrl', function($scope, Todo){
  
  $scope.todos = Todo.query();
  
  $scope.addTodo = function() {
    var todo = new Todo();
    todo.name = 'New task!'
    todo.completed = false;
    $scope.todos.unshift(todo);
  };
  
})