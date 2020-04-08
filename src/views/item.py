from flask import Blueprint, request, make_response, jsonify
from src.models.item import ItemModel, ItemSchema
from src.apis.item import ItemApi
import json
import os

# ルーティング設定
item_router = Blueprint('item_router', __name__)
itemApi = ItemApi()

@item_router.route('', methods=['GET'])
def getItems():
    items = itemApi.getItems()
    
    return make_response(jsonify({
        'code': 200,
        'items': items
    }))

@item_router.route('', methods=['POST'])
def registItem():
    # jsonデータを取得する
    jsonData = json.dumps(request.json)
    itemData = json.loads(jsonData)
    item = itemApi.postItem(itemData)

    return make_response(jsonify({
        'code': 200,
        'item': item
    }))
