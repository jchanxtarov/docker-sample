from flask_restful import Resource, reqparse
from src.models.user import UserModel, UserSchema
from src.database import db

class UserApi(Resource):

    def getUsers(self):
        results = UserModel.query.all() # consider: これで取れる仕組みが理解できていない
        users = UserSchema(many=True).dump(results)

        return users

    def postUser(self, user):
        user = UserModel(
            name=user['name']
        )

        db.session.add(user)
        db.session.commit()
        res = UserSchema().dump(user)

        return res