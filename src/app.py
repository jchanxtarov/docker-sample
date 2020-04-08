from flask import Flask, jsonify
from src.views.room import room_router
from src.views.user import user_router
from src.views.item import item_router
from src.database import init_db

def create_app():
  
  app = Flask(__name__)
  app.config.from_object('src.config.DevConfig')
  init_db(app) # (SQLAlchemy: python向けのORM) dbへ接続
  # https://github.com/zzzeek/sqlalchemy

  app.register_blueprint(room_router, url_prefix='/api/rooms')
  app.register_blueprint(user_router, url_prefix='/api/users')
  app.register_blueprint(item_router, url_prefix='/api/items')
  app.register_blueprint(history_router, url_prefix='/api/histories')

  return app

app = create_app()
