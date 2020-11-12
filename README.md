# pyservice-ci-template Package

This is a simple example package. You can use
[Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
to write your content.

Before creating the package of our python serivce, we need to install requirements using following command

`pip install -r requirements.txt`

# Generating the egg package 

`python setup.py pyassembly`

This command will generate the .egg file which is similar to our .zip format which will contain all the dependent
packages our service.

After obtaining this .egg file, we have to place that in the desired repository.

# Jenkins build

Once we obtain the `.egg` artifacts, jenkins pipeline will build our docker image and push the artifacts to nexus.
All these steps are automated once we push the changes to our project repo. We can track the jenkins build under: 
https://jenkins.cicd.sv2.247-inc.net/job/DSG/job/Pyjenkins/

# Installing the package in service host / local

First we have to pull the artifacts from nexus repository into desired host. In order to deploy the pyhton package that we built, we have to run the following command inside a python environment

`sudo easy_install --allow-hosts=None <artifact name>.egg`  

# Running our application 

Then in order to run our application which has been packaged and installed in python packages, we have to do the following

Since our application is fronted with gunicorn, we can just start a gunicorn start command using:
`gunicorn --bind 0.0.0.0:8083 -m 007 flaskapp.wsgi:app`

