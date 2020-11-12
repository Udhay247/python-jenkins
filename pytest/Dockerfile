FROM python:3.8.2-alpine3.11 AS stage1

RUN mkdir -p /flaskapp/

COPY . /flaskapp/

WORKDIR /flaskapp/

ENV FLASK_APP=flaskapp
ENV FLASK_ENV=development

RUN pip install --editable .
# Unit tests
RUN pip install pytest coverage 

RUN coverage run -m pytest && coverage report && coverage html && coverage xml




