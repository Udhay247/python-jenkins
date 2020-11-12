from flask import Flask
import os
import sys

def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        # a default secret that should be overridden by instance config
        SECRET_KEY="dev"
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.update(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/")
    @app.route("/hello")
    def hello():
        return "Hello, World!"

    @app.route('/hello/<username>')  # dynamic route
    def hello_user(username):
        return 'Why Hello %s!' % username

    return app

app = create_app()

if __name__ == '__main__':
    app.run(host=sys.argv[1],port=sys.argv[2])