from flask import Flask, jsonify, request
from flask_restx import Resource, Api
from Employee import Employee

app = Flask(__name__)
api = Api()
api.init_app(app)

todos = {}

@api.route('/<string:todo_id>')
class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}

@api.route('/todo1')
class Todo1(Resource):
    def get(self):
        # Default to 200 OK
        return {'task': 'Hello world'}

@api.route('/todo2')
class Todo2(Resource):
    def get(self):
        # Set the response code to 201
        return {'task': 'Hello world'}, 201

@api.route('/todo3')
class Todo3(Resource):
    def get(self):
        # Set the response code to 201 and return custom headers
        return {'task': 'Hello world'}, 201, {'Etag': 'some-opaque-string'}

# @app.route("/")
# def hello_world():
#     return "<p>Hello world</p>"

# @app.route("/hello/<username>")
# @api.doc(params={'id': 'An ID'})
# def hello_world2(username):
#     print(username)
#     return f'Subpath {username}'

# @app.route("/getemployee/<username>")
# def getuser(username):
#     e = Employee("test", 10)
#     return jsonify(e.serialize())

# @app.route("/address/<username>")
# def getaddress(username):
#     e = Employee("test", 10)
#     return jsonify(e.serialize())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')