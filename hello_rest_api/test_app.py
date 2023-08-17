# test_app.py
"""
Tests hello_rest_api endpoints.
"""
from . import app


def test_hello_200_response():
    """expects 200 OK and JSON response"""
    web = app.app.test_client()

    response = web.get('/api/v1/hello')
    assert response.status == '200 OK'
    assert response.data == b'{"msg":"hello"}\n'


def test_hello_200_round_robin():
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


def test_handshake_401_unauthorized():
    """expects 401 unauthorized and no response"""
    web = app.app.test_client()

    response = web.post('/api/v1/handshake')
    assert response.status == '401 UNAUTHORIZED'


def test_handshake_403_forbidden_invalid_user():
    """expects 403 unauthorized"""
    web = app.app.test_client()

    response = web.post('/api/v1/handshake', auth=('not_admin',
                                                   'admin_password'))
    assert response.status == '403 FORBIDDEN'


def test_handshake_403_forbidden_invalid_password():
    """expects 403 unauthorized"""
    web = app.app.test_client()

    response = web.post('/api/v1/handshake', auth=('admin',
                                                   'not_admin_password'))
    assert response.status == '403 FORBIDDEN'


def test_handshake_403_forbidden_valid_user():
    """expects 403 unauthorized"""
    web = app.app.test_client()

    response = web.post('/api/v1/handshake', auth=('user',
                                                   'user_password'))
    assert response.status == '403 FORBIDDEN'


def test_handshake_200_valid_admin():
    """expects 200 OK and JSON response"""
    web = app.app.test_client()

    response = web.post('/api/v1/handshake', auth=('admin',
                                                   'admin_password'))
    assert response.status == '200 OK'
    assert response.data == b'{"msg":"handshake"}\n'
