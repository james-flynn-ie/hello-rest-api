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


def test_handshake():
    """expects 200 OK and JSON {msg": "handshake"}"""
    web = app.app.test_client()

    response = web.post('/api/v1/handshake')
    assert response.status == '200 OK'
    assert response.data == b'{"msg":"handshake"}\n'
