'use strict';

angular.module('todoListApp')
.factory('Todo', function($resource){
  var token = getToken
  var res = $resource('/api/v1/todos/:id', {id: '@id'}, {
    update: {
      method: 'PUT',
      headers: {
        Authorization: token
      }
    },
    get: {
        method: 'GET',
        isArray: false,
        headers: {
          Authorization: token
        }  
    },
    delete: {
        method: 'DELETE',
        headers: {
          Authorization: token
        }  
    },
    query: {
      method: 'GET',
      isArray: true,
      headers: {
        Authorization: token
      }
    },
    save: {
      method: 'POST',
      headers: {
        Authorization: token
      }
    }
  });

  function getToken() {
    var xmlHttp = new XMLHttpRequest();
    var url = 'http://' + location.host + '/api/v1/auth/token';
    xmlHttp.open("GET", url, false);
    xmlHttp.send(null);
    return 'Bearer ' + xmlHttp.responseText;
  };
  return res;
});