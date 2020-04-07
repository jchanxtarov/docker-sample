from flask_restful import Resource, reqparse
from src.models.room import RoomModel, RoomSchema
from src.database import db

class RoomApi(Resource):

    def getRooms(self):
        results = RoomModel.query.all() # consider: これで取れる仕組みが理解できていない
        rooms = RoomSchema(many=True).dump(results)

        return rooms

    def postRoom(self, room):
        room =RoomModel(
            name=room['name']
        )

        db.session.add(room)
        db.session.commit()
        res = RoomSchema().dump(room)

        return res