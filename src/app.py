from flask import Flask, jsonify
from flask_restful import Api
from src.database import init_db
from src.apis.user import UserListAPI


def create_app():

  app = Flask(__name__)
  app.config.from_object('src.config.Config')

  init_db(app)

  api = Api(app)
  api.add_resource(UserListAPI, '/users')

  return app

app = create_app()