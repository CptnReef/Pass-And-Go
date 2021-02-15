from flask import Flask, render_template, redirect, url_for, Blueprint, request, flash
from datetime import datetime
import os, pickle, json
from RTC_Service import db_session, socketio
from RTC_Service.models import USER_RTC_ROOM_ROLE
from RTC_Service.sql_models import Room
from threading import Lock
from flask_socketio import join_room, leave_room, emit

ROOM='test'

rooms_participants = dict()


# @socketio.on('connect', namespace='/signaler')
# async def connect():
#     sid = request.sid
#     print('Connected', sid)
#     await socketio.emit('ready', room=ROOM, skip_sid=sid)
#     join_room(ROOM)

@socketio.on('connect', namespace='/signaler')
def connect():
    sid = request.sid
    print('Connected', sid)
    emit('ready', data={}, room=ROOM, skip_sid=sid)
    join_room(ROOM)

@socketio.on('disconnect', namespace='/signaler')
def disconnect():
    sid = request.sid
    print('Disconnected', sid)
    leave_room(ROOM)


@socketio.on('data', namespace='/signaler')
def data(data):
    sid = request.sid
    print('data')
    print('Message from {}: {}'.format(sid, data))
    emit('data', data, room=ROOM, skip_sid=sid)
