from flask import Flask, jsonify
from src.views.user import user_router
from src.database import init_db
from src.apis.user import UserAPI

def create_app():

  print("test. ここは読み込まれている")
  app = Flask(__name__)
  app.config.from_object('src.config.DevConfig')
  init_db(app) # (SQLAlchemy: python向けのORM) dbへ接続
  # https://github.com/zzzeek/sqlalchemy

  app.register_blueprint(user_router, url_prefix='/api/users')

  return app

app = create_app()