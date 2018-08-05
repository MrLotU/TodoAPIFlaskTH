'use strict';

angular.module('todoListApp')
.factory('Todo', function($resource){
  return $resource('/api/v1/todos/:id', {id: '@id'}, {
    update: {
      method: 'PUT'
    }
  });
});