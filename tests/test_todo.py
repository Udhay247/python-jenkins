from service.db import get_db
import json


def test_create(client, app):
    client.post('/todos/', json={"task": "Task1"})
    with app.app_context():
        db = get_db()
        count = db.execute('SELECT COUNT(id) FROM todo').fetchone()[0]
        assert count == 2


def test_update(client, app):
    client.put('/todos/1', json={"task": "Task1"})
    with app.app_context():
        db = get_db()
        post = db.execute("SELECT * FROM todo WHERE id = 1").fetchone()
        assert post["task"] == "Task1"


def test_delete(client, app):
    client.delete('/todos/1')
    with app.app_context():
        db = get_db()
        count = db.execute("SELECT COUNT(id) FROM todo").fetchone()[0]
        assert count == 0


def test_get(client, app):
    client.get('/todos/1')
    with app.app_context():
        db = get_db()
        post = db.execute("SELECT * FROM todo WHERE id = 1").fetchone()
        assert post["task"] == "Complete Service Template for Python"

    assert client.get("/todos/2").status_code == 404


def test_list(client, app):
    response = client.get('/todos/')
    assert len(json.loads(response.data)) == 1

