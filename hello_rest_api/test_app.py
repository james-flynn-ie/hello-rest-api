# test_app.py
from . import app


def test_hello():
    web = app.app.test_client()

    response = web.get('/api/v1/hello')
    assert response.status == '200 OK'
    assert response.data == b'{"msg":"hello"}\n'


def test_handshake():
    web = app.app.test_client()

    response = web.post('/api/v1/handshake')
    assert response.status == '200 OK'
    assert response.data == b'{"msg":"handshake"}\n'
