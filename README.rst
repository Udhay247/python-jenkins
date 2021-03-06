Python Service Tempate
======================

This template serves as a skeleton to build your service


Install
-------

clone the repository::

    $ git clone "Github Link"
    $ cd project


Create a virtualenv and activate it::

    $ python3 -m venv venv
    $ . venv/bin/activate

Or on Windows cmd::

    $ py -3 -m venv venv
    $ venv\Scripts\activate.bat

Install service::

    $ pip install -e .

Run Locally
-----------

::

    $ export FLASK_APP=service
    $ export FLASK_ENV=development
    $ flask init-db
    $ flask run

Or on Windows cmd::

    > set FLASK_APP=flaskr
    > set FLASK_ENV=development
    > flask init-db
    > flask run

Open http://127.0.0.1:5000 in a browser. This automatically
displays the swagger doc.

To get the swagger doc in json format, open
http://localhost:5000/swagger.json


Test
----

::

    $ pip install '.[test]'
    $ pytest

Run with coverage report::

    $ coverage run -m pytest
    $ coverage report
    $ coverage html  # open htmlcov/index.html in a browser

Run Pylint::

    $ pip install pylint_flask
    $ pylint --exit-zero --reports=n --rcfile=.pylintrc --load-plugins pylint_flask service



Generating the egg package
--------------------------

::

    $ pip install pyassembly
    $ python setup.py pyassembly

This command will generate the .egg file which is similar to our .zip format which will contain all the dependent
packages our service.

After obtaining this .egg file, we have to place that in the desired repository.


Installing the package in service host / local
----------------------------------------------


First we have to pull the artifacts from nexus repository into desired host. In order to deploy the python package that we built, we have to run the following command inside a python environment

::

    sudo easy_install --allow-hosts=None <artifact name>.egg

Running our application
-----------------------

Then in order to run our application which has been packaged and installed in python packages, we have to do the following

Since our application is fronted with gunicorn, we can just start a gunicorn start command using:

::

    export FLASK_APP=service
    flask init-db
    gunicorn --bind 0.0.0.0:8080 -m 007 service.wsgi:app

