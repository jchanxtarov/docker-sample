from flask_restful import Resource, reqparse, abort
from flask import jsonify
from models.user import UserModel, UserSchema
from database import db

class UserListAPI(Resource):
  def __init__(self):
    self.reqparse = reqparse.RequestParser()
    self.reqparse.add_argument('name', required=True)
    super(UserListAPI, self).__init__()

  def get(self):
    results = UserModel.query.all()
    jsonData = UserSchema(many=True).dump(results).data
    return jsonify({'items': jsonData})

  def post(self):
    args = self.reqparse.parse_args()
    user = UserModel(args.name, args.state)
    db.session.add(user)
    db.session.commit()
    res = UserSchema().dump(user).data
    return res, 201