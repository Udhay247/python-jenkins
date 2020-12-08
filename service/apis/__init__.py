"""This is used to group all the namespaces and tells Python that the directory should be
treated as a package"""

from flask_restx import Api

from .todo import ns as ns1

api = Api(title='Todo API',
          version='1.0',
          description='A simple Todo API',
          # All API metadatas
          )

api.add_namespace(ns1)
