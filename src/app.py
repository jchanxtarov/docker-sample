from flask import Flask, jsonify
from flask_restful import Api
from database import init_db
from apis.user import UserListAPI


def create_app():

  app = Flask(__name__)
  app.config.from_object('config.Config')

  init_db(app)

  api = Api(app)
  api.add_resource(UserListAPI, '/users')

  return app

app = create_app()