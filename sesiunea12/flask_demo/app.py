from flask import Flask, request

app = Flask(__name__)


# GET
@app.route("/")
def index():
    return "OK", 200


# GET
@app.route("/hello/<name>")
def hello(name):
    return f"Hello {name}", 200


# POST
@app.route("/login", methods=["POST"])
def login():
    print(request.method)
    print(request.json)
    return "OK", 200


if __name__ == '__main__':
    app.run(debug=True)
