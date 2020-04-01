from flask import Blueprint, request, make_response, jsonify
from src.models import UserModel, UserSchema
from src.apis import UserAPI
import json

# ルーティング設定
user_router = Blueprint('user_router', __name__)

@user_router.route('/', methods=['GET'])
def getUserList():
    users = UserAPI.getUserList()
    
    return make_response(jsonify({
        'code': 200,
        'users': users
    }))

@user_router.route('/', methods=['POST'])
def registUser():
    # jsonデータを取得する
    jsonData = json.dumps(request.json)
    userData = json.loads(jsonData)
    user = UserAPI.postUser(userData)

    return make_response(jsonify({
        'code': 200,
        'user': user
    }))