from flask import Flask, jsonify
from models.user import User
from models.api_client import Steam
from models.user_transformer import User_transformer
from models.game_transformer import Game_transformer

app = Flask(__name__)


@app.route('/howmuchtimehaveiwasted/')
def no_steamid():
    return jsonify('Please provide a steamid'), 400


@app.route('/howmuchtimehaveiwasted/<steamid>')
def get_user(steamid):
    try:
        user_data = Steam().get_user_data(steamid)
        games_data = Steam().get_user_games(steamid)
    except:
        return jsonify('There was a problem finding that user'), 400

    games = Game_transformer().transform_games_list(games_data)
    user = User_transformer().transform_user(user_data)

    for game in games:
        user.total_playtime += game.playtime

    for game in games:
        user.games.append(game.to_json())

    return jsonify(user.to_json())


if __name__ == '__main__':
    app.run()
