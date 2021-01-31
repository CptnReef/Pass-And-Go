from flask import Blueprint, render_template

Main_Blueprint = Blueprint('main', __name__, template_folder='templates')


@Main_Blueprint.route('/', methods=['GET'])
def home():
    return render_template("home.html")