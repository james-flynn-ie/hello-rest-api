"""
flask web server.
"""
from flask import Flask, jsonify, request, abort

app = Flask(__name__)


"""
Mock user data for demonstrating authentication process.
Caution: Use a secure method such as Azure Entra ID (formerly Azure AD)
for production workloads!
"""
users_dict = {
    'admin': {'password': 'admin_password', 'role': 'admin'},
    'user': {'password': 'user_password', 'role': 'user'}
}


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
        The value returned is the list item at the current response index.
        """
        response = self.responses[self.current_response_index]
        self.increment_index()
        return response

    def increment_index(self):
        """
        Increment the current_response_index,
        using the mod of the responses list length to stay in bounds.
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


def authenticate(username, password):
    """
    Simple authentication check to validate user and password values.
    """
    user = users_dict.get(username)
    if user and user['password'] == password:
        return user
    return None


@app.route("/api/v1/handshake", methods=['POST'])
def check_admin_access():
    """
    Authorization check to validate account user and password values,
    as well as admin role privileges.
    """
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        abort(401)  # Unauthorized

    user = authenticate(auth.username, auth.password)
    if not user or user['role'] != 'admin':
        abort(403)  # Forbidden

    return handshake()


def handshake():
    """returns 200 OK and JSON {"msg": "handshake"}"""
    msg = {
        "msg": "handshake"
    }
    return (jsonify(msg), 200)


if __name__ == "__main__":
    app.run()
