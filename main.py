from flask import Flask, jsonify
from Employee import Employee

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello world</p>"

@app.route("/hello/<username>")
def hello_world2(username):
    print(username)
    return f'Subpath {username}'

@app.route("/getemployee/<username>")
def getuser(username):
    e = Employee("test", 10)
    return jsonify(e.serialize())

@app.route("/address/<username>")
def getaddress(username):
    e = Employee("test", 10)
    return jsonify(e.serialize())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')