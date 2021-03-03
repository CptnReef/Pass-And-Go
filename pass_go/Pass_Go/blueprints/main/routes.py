from flask import Blueprint, render_template, url_for
import os
import json

Main_Blueprint = Blueprint('main', __name__, template_folder='templates')


@Main_Blueprint.route('/', methods=['GET'])
def home():
    return render_template("home.html")


@Main_Blueprint.route('/go', methods=['GET'])
def go():

    # Get Game Title List
    gameDirectoryList = os.listdir("./Pass_Go/static/games")
    games = []

    for game in gameDirectoryList:
        games.append({
            "title": game,
            "imageUrl": f"games/{game}/title-image.png"
        })

    context = {"games": games}

    return render_template("video_chat.html", **context)


@Main_Blueprint.route('/get_game_url/<gameindex>', methods=['GET'])
def get_game_url(gameindex):

    gameDirectoryList = os.listdir("./Pass_Go/static/games")
    game = gameDirectoryList[int(gameindex)]

    gameFileList = os.listdir(f"./Pass_Go/static/games/{game}")

    htmlFile = ""
    jsFiles = []

    for file in gameFileList:
        if file.endswith('.js'):
            jsFiles.append(url_for("static", filename=f"games/{game}/{file}"))
        elif file.endswith('.html'):
            htmlFile = url_for("static", filename=f"games/{game}/{file}")

    game_url = json.dumps({"js": jsFiles, "html": htmlFile})

    return game_url
