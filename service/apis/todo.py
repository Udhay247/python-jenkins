"""This is used to define the namespace"""
# pylint: disable=R0201
# pylint: disable=C0116
# pylint: disable=W0622


from flask_restx import Namespace, Resource, fields
from service.db import get_db

ns = Namespace('todos', description='TODO operations')

todo = ns.model('Todo', {
    'id': fields.Integer(readonly=True, description='The task unique identifier'),
    'task': fields.String(required=True, description='The task details')
})


class TodoDAO():
    """Used to communicate with the todo table in db"""

    def __init__(self):
        self.counter = 0

    def get(self, task_id):
        task = (
            get_db()
            .execute(
                "SELECT id, task"
                " FROM todo"
                " WHERE id = ?",
                (task_id,),
            )
            .fetchone()
        )
        if task is None:
            ns.abort(404, "Todo {} doesn't exist".format(task_id))
        return task

    def create(self, data):
        task = data
        task['id'] = self.counter = self.counter + 1

        db = get_db()
        db.execute(
            "INSERT INTO todo (id, task) VALUES (?,?)",
            (task['id'], task['task'],)
        )
        db.commit()

        return task

    def update(self, task_id, data):
        task = data
        task['id'] = task_id
        db = get_db()
        db.execute(
            "UPDATE todo SET task = ? WHERE id = ?", (data['task'], task_id)
        )
        db.commit()
        return task

    def delete(self, task_id):
        db = get_db()
        db.execute("DELETE FROM todo WHERE id = ?", (task_id,))
        db.commit()

    def list(self):
        db = get_db()
        todos = db.execute(
            "SELECT id, task"
            " FROM todo"
        ).fetchall()
        return todos


DAO = TodoDAO()


# DAO.create({'task': 'Build an API'})
# DAO.create({'task': '?????'})
# DAO.create({'task': 'profit!'})

@ns.route('/')
class TodoList(Resource):
    '''Shows a list of all todos, and lets you POST to add new tasks'''

    @ns.doc('list_todo')
    @ns.marshal_list_with(todo)
    def get(self):
        '''List all tasks'''
        ns.logger.info("Received request to list todos")
        return DAO.list()

    @ns.doc('create_todo')
    @ns.expect(todo)
    @ns.marshal_with(todo, code=201)
    def post(self):
        '''Create a new task'''
        ns.logger.info("Received request to create todo")
        return DAO.create(ns.payload), 201


@ns.route('/<int:id>')
@ns.response(404, 'Todo not found')
@ns.param('id', 'The task identifier')
class Todo(Resource):
    '''Show a single todo item and lets you delete them'''

    @ns.doc('get_todo')
    @ns.marshal_with(todo)
    def get(self, id):
        '''Fetch a given resource'''
        ns.logger.info("Received request to get todo")
        return DAO.get(id)

    @ns.doc('delete_todo')
    @ns.response(204, 'Todo deleted')
    def delete(self, id):
        '''Delete a task given its identifier'''
        ns.logger.info("Received request to delete todo")
        DAO.delete(id)
        return '', 204

    @ns.expect(todo)
    @ns.marshal_with(todo)
    def put(self, id):
        '''Update a task given its identifier'''
        ns.logger.info("Received request to update todo")
        return DAO.update(id, ns.payload)
