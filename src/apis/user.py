from flask_restful import Resource, reqparse, abort
from flask import jsonify
from src.models.user import UserModel, UserSchema
from src.database import db

class UserAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('name', required=True)
        super(UserAPI, self).__init__()

    def getUserList(self):
        results = UserModel.query.all() # consider: これで取れる仕組みが理解できていない
        user_schema = UserSchema(many=True).dump(results).data
        users = user_schema.dump(results).data

        return users

    def postUser(self):
        print("[test] hogehogehogehoge")
        args = self.reqparse.parse_args()
        user = UserModel(
            name=args.name
        )
        db.session.add(user)
        db.session.commit()

        return user