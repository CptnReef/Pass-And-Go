from flask import Blueprint, render_template

Main_Blueprint = Blueprint('main', __name__, template_folder='templates')


@Main_Blueprint.route('/', methods=['GET'])
def home():
    return render_template("home.html")


@Main_Blueprint.route('/go', methods=['GET'])
def go():
    #Use list or library for games and turn it into a length 
    game_cards = ['1','2','3','4','5','6','7','8','9']
    games = ['#','dtd_game.html','#','#','#','#','#','#','#']

    counter = 0

    if counter != 3:
        counter += 1
    else:
        counter = 0

    context = {
        'game2': 'dtd_game.html',
        'list': game_cards,
        'counter': counter,
    }
    return render_template("video_chat.html", **context)
