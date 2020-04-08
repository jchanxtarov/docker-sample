from flask import Blueprint, request, make_response, jsonify
from src.models.room import RoomModel, RoomSchema
from src.apis.room import RoomApi
import json
import os

# ルーティング設定
room_router = Blueprint('room_router', __name__)
roomApi = RoomApi()

@room_router.route('', methods=['GET'])
def getRooms():
    rooms = roomApi.getRooms()
    
    return make_response(jsonify({
        'code': 200,
        'romrs': rooms
    }))

@room_router.route('', methods=['POST'])
def registRoom():
    # jsonデータを取得する
    jsonData = json.dumps(request.json)
    roomData = json.loads(jsonData)
    room = roomApi.postRoom(roomData)

    return make_response(jsonify({
        'code': 200,
        'room': room
    }))
