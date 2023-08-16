"""
flask web server.
"""
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/api/v1/hello", methods=['GET'])
def hello():
    """returns 200 OK and JSON {msg": "hello"}"""
    msg = {
        "msg": "hello"
    }
    return (jsonify(msg), 200)


@app.route("/api/v1/handshake", methods=['POST'])
def handshake():
    """returns 200 OK and JSON {msg": "handshake"}"""
    msg = {
        "msg": "handshake"
    }
    return (jsonify(msg), 200)


if __name__ == "__main__":
    app.run()
