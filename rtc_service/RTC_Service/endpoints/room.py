import json
from flask import Blueprint, request

from RTC_Service import db_session
from RTC_Service.sql_models import (
    User_RTC_Room_Association,
    User_RTC,
    Room,
    User_Token,
)

Room_Blueprint = Blueprint('room',__name__)


@Room_Blueprint.route('/create', methods=['POST'])
def create():
    '''
    payload:
        {
        }

    '''
    print('create room')
    data = request.json()
    print(json.dumps(data, indent=2))


    new_room = Room()
    db_session.add(new_room)
    db_session.commit()

    return json.dumps(new_room.as_dict()), 200

@Room_Blueprint.route('/<room_code>', methods=['DELETE'])
def delete(room_code):
    '''
    payload:
        {
        }

    '''
    print('create room')
    data = request.json()
    print(json.dumps(data, indent=2))

    temp_room = db_session.query(Room).filter_by(code=room_code).first()
    db_session.delete(temp_room)
    db_session.commit()

    return json.dumps({'msg':'Deleted'}), 200

@Room_Blueprint.route('/<room_code>', methods=['GET'])
def get(room_code):
    '''
    payload:
        {
        }

    '''
    print('create room')
    data = request.json()
    print(json.dumps(data, indent=2))

    temp_room = db_session.query(Room).filter_by(code=room_code).first()
    if temp_room:
        return json.dumps(temp_room.as_dict()), 200
    return json.dumps({'msg':'Does Not Exist'}), 404