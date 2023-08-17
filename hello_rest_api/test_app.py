# test_app.py
"""
Tests hello_rest_api endpoints.
"""
from . import app


def test_hello():
    """expects 200 OK and JSON {msg": "hello"}"""
    web = app.app.test_client()

    response = web.get('/api/v1/hello')
    assert response.status == '200 OK'
    assert response.data == b'{"msg":"hello"}\n'


def test_hello_round_robin():
    """
    Test the round robin feature.
    Expects 200 OK and that the JSON message will alternate for each run
    """
    web = app.app.test_client()

    response = web.get('/api/v1/hello')
    assert response.status == '200 OK'
    assert response.data == b'{"msg":"Hello from new v1"}\n'

    response = web.get('/api/v1/hello')
    assert response.status == '200 OK'
    assert response.data == b'{"msg":"hello"}\n'

    response = web.get('/api/v1/hello')
    assert response.status == '200 OK'
    assert response.data == b'{"msg":"Hello from new v1"}\n'


def test_handshake():
    """expects 200 OK and JSON {msg": "handshake"}"""
    web = app.app.test_client()

    response = web.post('/api/v1/handshake')
    assert response.status == '200 OK'
    assert response.data == b'{"msg":"handshake"}\n'
