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


    new_room = Room(users=user_list)
    db_session.add(new_room)
    db_session.commit()

    return json.dumps(new_room.as_dict()), 200