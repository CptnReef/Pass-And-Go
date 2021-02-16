from flask import Blueprint, render_template

Main_Blueprint = Blueprint('main', __name__, template_folder='templates')


@Main_Blueprint.route('/', methods=['GET'])
def home():
    return render_template("home.html")


@Main_Blueprint.route('/go', methods=['GET'])
def go():
    return render_template("video_chat.html")
