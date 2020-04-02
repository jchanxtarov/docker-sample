from flask_restful import Resource, reqparse
from src.models.user import UserModel, UserSchema
from src.database import db

class UserApi(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('name', required=True)
        super(UserApi, self).__init__()

    def getUsers():
        results = UserModel.query.all() # consider: これで取れる仕組みが理解できていない
        users = UserSchema(many=True).dump(results)

        return users

    def postUser(self):
        test = reqparse.RequestParser()
        test.add_argument('name', required=True)
        args = test.parse_args()
        # args = self.reqparse.parse_args()
        user = UserModel(
            name=args.name
        )
        db.session.add(user)
        db.session.commit()
        res = UserSchema().dump(user)

        return res