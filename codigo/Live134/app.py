from flask import Flask, abort, jsonify, make_response, request, url_for
from flask_restx import Api, Namespace, Resource, fields

app = Flask(__name__, static_url_path='')

api = Api(
    app,
    'todos',
    description='Operações ligadas as suas tarefas',   
)
ns = Namespace('todos', description='Operações ligadas as suas tarefas')
api.add_namespace(ns)

todo = api.model(
    'Todo',
    {
        'id': fields.Integer(
            readonly=True, description='Identificador único da tarefa'
        ),
        'tittle': fields.String(required=True, description='Nome da Tarefa'),
        'description': fields.String(
            required=True, description='Descrição da tarefa'
        ),
        'done': fields.Boolean(
            required=True, description='A tarefa será concluída?'
        ),
    },
)


@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'error': 'Bad request'}), 400)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not Found'}), 404)


class TodoDAO(object):
    def __init__(self):
        self.counter = 0
        self.todos = []

    def get(self, id):
        for todo in self.todos:
            if todo['id'] == id:
                return todo
        api.abort(404, "Todo {} doens't exist".format(id))

    def create(self, data):
        todo = data
        todo['id'] = self.counter = self.counter + 1
        self.todos.append(todo)
        return todo

    def update(self, id, data):
        todo = self.get(id)
        todo.update(data)
        return todo

    def delete(self, id):
        todo = self.get(id)
        self.todos.remove(todo)


DAO = TodoDAO()


@ns.route('/api/tasks')
class TodoList(Resource):
    @ns.marshal_list_with(todo, code=200)
    def get(self):
        return DAO.todos

    @ns.expect(todo)
    @ns.marshal_with(todo, code=201)
    def post(self):
        return DAO.create(api.payload), 201


@ns.route('/api/tasks/<int:task_id>')
class Todo(Resource):
    @ns.marshal_with(todo)
    def get(self, task_id):
        return DAO.get(task_id)

    @ns.marshal_with(todo)
    def put(self, task_id):
        return DAO.update(task_id, api.payload)

    @ns.expect(todo)
    @ns.marshal_with(todo)
    def patch(self, task_id):
        return DAO.update(task_id, api.payload)

    @ns.marshal_with(todo)
    def delete(self, task_id):
        DAO.delete(task_id)
        return '', 204
