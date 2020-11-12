#!/bin/bash

sg www-data -c "gunicorn --bind unix:myproject.sock -m 007 flaskapp.wsgi:app"
