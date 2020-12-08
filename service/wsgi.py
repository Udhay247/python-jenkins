"""This file is used for instantiating the Flask App"""
from service import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)


