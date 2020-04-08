from flask import Blueprint, request, make_response, jsonify
from src.models.history import HistoryModel, HistorySchema
from src.apis.user import UserApi
import json
import os

# ルーティング設定
history_router = Blueprint('history_router', __name__)
historyApi = HistoryApi()

# @history_router.route('', methods=['GET'])
# def getHistories():
#     print(os.getenv('MYSQL_USER'))
#     users = historyApi.getUsers()
    
#     return make_response(jsonify({
#         'code': 200,
#         'users': users
#     }))

# @history_router.route('', methods=['POST'])
# def registHistory():
#     # jsonデータを取得する
#     jsonData = json.dumps(request.json)
#     userData = json.loads(jsonData)
#     user = userApi.postUser(userData)

#     return make_response(jsonify({
#         'code': 200,
#         'user': user
#     }))