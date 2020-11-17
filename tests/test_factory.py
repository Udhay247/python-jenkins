from flaskapp import create_app

def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing


def test_hello(client):
    response = client.get('/hello')
    assert response.data == b'Hello, World!'

def test_hello_user(client):
    response = client.get('/hello/user1')
    assert response.data == b'Why Hello user1!'