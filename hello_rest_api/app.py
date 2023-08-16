from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/api/v1/hello", methods=['GET'])
def hello():
    msg = {
        "msg": "hello"
    }
    return (jsonify(msg), 200)


@app.route("/api/v1/handshake", methods=['POST'])
def handshake():
    msg = {
        "msg": "handshake"
    }
    return (jsonify(msg), 200)


if __name__ == "__main__":
    app.run()
