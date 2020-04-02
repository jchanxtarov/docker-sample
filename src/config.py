import os

class DevelopmentConfig:

  DEBUG = True

  SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8'.format(
    **{
      'user': os.getenv('MYSQL_USER', 'flask'), # ローカルでの立ち上げに成功したらdefault値を削除する
      'password': os.getenv('MYSQL_PASSWORD', 'flask'),
      'host': os.getenv('MYSQL_HOST', 'mysql'),
      'database': os.getenv('MYSQL_DATABASE', 'flask_app'),
    })
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  SQLALCHEMY_ECHO = False

DevConfig = DevelopmentConfig
