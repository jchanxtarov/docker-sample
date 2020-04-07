from flask_restful import Resource, reqparse
from src.models.item import ItemModel, ItemSchema
from src.database import db

class ItemApi(Resource):

    def getItems(self):
        results = ItemModel.query.all() # consider: これで取れる仕組みが理解できていない
        items = ItemSchema(many=True).dump(results)

        return items

    def postItem(self, item):
        item =ItemrModel(
            name=item['name']
        )

        db.session.add(item)
        db.session.commit()
        res = ItemSchema().dump(item)

        return res