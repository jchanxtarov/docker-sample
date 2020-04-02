from flask import Blueprint, request, make_response, jsonify
from src.models.user import UserModel, UserSchema
from src.apis.user import UserApi
import json

# ルーティング設定
user_router = Blueprint('user_router', __name__)
userApi = UserApi()

@user_router.route('', methods=['GET'])
def getUsers():
    users = userApi.getUsers()
    
    return make_response(jsonify({
        'code': 200,
        'users': users
    }))

@user_router.route('', methods=['POST'])
def registUser():
    # jsonデータを取得する
    jsonData = json.dumps(request.json)
    userData = json.loads(jsonData)
    user = userApi.postUser(userData)

    return make_response(jsonify({
        'code': 200,
        'user': user
    }))