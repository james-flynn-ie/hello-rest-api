"""
flask web server.
"""
from flask import Flask, jsonify

app = Flask(__name__)


class RoundRobinResponse:
    """
    Selects the response for the hello endpoint in round-robin format,
    where 50% of the responses return "hello"
    and 50% return "Hello from new v1".
    """
    def __init__(self, responses):
        self.responses = responses
        self.current_response_index = 0

    def get_next_response(self):
        """
        Get the next round-robin response.
        The method iterates the current_response_index each time it is used,
        using the mod of the responses list length to stay in bounds.
        """
        response = self.responses[self.current_response_index]
        self.increment_index()
        return response

    def increment_index(self):
        """
        Increment the current_response_index in a circular manner.
        """
        self.current_response_index = ((self.current_response_index + 1)
                                       % len(self.responses))


hello_responses = [
    "hello",
    "Hello from new v1",
]

round_robin = RoundRobinResponse(hello_responses)


@app.route("/api/v1/hello", methods=['GET'])
def hello():
    """returns 200 OK and JSON message"""

    response = round_robin.get_next_response()

    msg = {
        "msg": f"{response}"
    }
    return (jsonify(msg), 200)


@app.route("/api/v1/handshake", methods=['POST'])
def handshake():
    """returns 200 OK and JSON {"msg": "handshake"}"""
    msg = {
        "msg": "handshake"
    }
    return (jsonify(msg), 200)


if __name__ == "__main__":
    app.run()
