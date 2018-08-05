import json

from flask import Blueprint, abort, jsonify, make_response, request
from flask_restful import Api, Resource, fields, inputs, marshal, marshal_with, reqparse, url_for

from TodoAPI.models import Todo

todo_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'edited': fields.Boolean,
    'completed': fields.Boolean
}

class TodoList(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'name',
            required=True,
            help='No TODO name provided',
            location=['form', 'json']
        )

    def get(self):
        return [marshal(todo, todo_fields) for todo in Todo.select()]
        
    def post(self):
        args = self.reqparse.parse_args()
        if args['name'] is None:
            return jsonify({'error': 'No name provided'}), 400
        todo = Todo.create(name=args['name'])
        return marshal(todo, todo_fields), 200
    
class TodoResource(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'name',
            required=True,
            help='No TODO name provided',
            location=['form', 'json']
        )

    def put(self, id):
        args = self.reqparse.parse_args()
        if args['name'] is None:
            return jsonify({'error': 'No name provided'}), 400
        todo = Todo.select().where(Todo.id == id).get()
        todo.name = args['name']
        todo.save()
        return 200
    
    def delete(self, id):
        todo = Todo.select().where(Todo.id == id).get()
        todo.delete_instance()
        return {}, 200

todo_api = Blueprint('resources.todo', __name__)

api = Api(todo_api)
api.add_resource(
    TodoList,
    '/todos',
    endpoint='todos'
)

api.add_resource(
    TodoResource,
    '/todos/<int:id>',
    endpoint='todo'
)