'use strict';

angular.module('todoListApp')
.factory('Todo', function($resource){
  // var token = "eyJhbGciOiJIUzI1NiIsImlhdCI6MTUzMzkwMDc0MCwiZXhwIjoxNTMzOTA0MzQwfQ.eyJpZCI6MX0.OUbTZxXhY3tXtJbph0xTpW5FwDVIn2TIqSooEO_r0hI"
  // getToken()
  return $resource('/api/v1/todos/:id', {id: '@id'}, {
    update: {
      method: 'PUT',
      headers: {
        'Authorization': getToken
      }
    },
    get: {
        method: 'GET',
        isArray: false,
        headers: {
            'Authorization': getToken
        }
    },
    delete: {
        method: 'DELETE',
        headers: {
            'Authorization': getToken
        }
    },
  });
  function getToken(context) {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET", 'http://localhost:8080/api/v1/auth/token', false);
    xmlHttp.send(null);
    console.log(xmlHttp.responseText);
    return 'Bearer ' + xmlHttp.responseText;
  }
});