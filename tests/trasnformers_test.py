from models.game import Game
from models.user import User
from models.user_transformer import User_transformer
from models.game_transformer import Game_transformer

import json
import os
import sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)


def test_transformer_turns_user_data_into_user_obj():
    data = {
        "steamid": "76561198066000502",
        "communityvisibilitystate": 3,
        "profilestate": 1,
        "personaname": "Lixard",
        "commentpermission": 1,
        "profileurl": "https://steamcommunity.com/profiles/76561198066000502/",
        "avatar": "https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/4a/4ad45031967e52ce05f28c7f5591227e66715c5d.jpg",
        "avatarmedium": "https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/4a/4ad45031967e52ce05f28c7f5591227e66715c5d_medium.jpg",
        "avatarfull": "https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/4a/4ad45031967e52ce05f28c7f5591227e66715c5d_full.jpg",
        "avatarhash": "4ad45031967e52ce05f28c7f5591227e66715c5d",
        "lastlogoff": 1594245076,
        "personastate": 0,
        "primaryclanid": "103582791463737200",
        "timecreated": 1340730740,
        "personastateflags": 4,
        "loccountrycode": "PT",
        "locstatecode": "14"
    }

    user = User_transformer().transform_user(data)

    assert type(user) == User
    assert user.name == 'Lixard'
    assert user.img == 'https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/4a/4ad45031967e52ce05f28c7f5591227e66715c5d_full.jpg'
    assert user.url == 'https://steamcommunity.com/profiles/76561198066000502/'
    assert user.created == '1340730740'


def test_transformer_turns_game_data_into_game_obj():
    data = {
        "appid": 17390,
        "playtime_forever": 3257,
        "playtime_windows_forever": 0,
        "playtime_mac_forever": 0,
        "playtime_linux_forever": 0
    }

    game = Game_transformer().transform_game(data)

    assert game.appid == 17390
    assert game.playtime == 3257


def test_transformer_turns_each_game_in_games_data_into_game_obj():
    with open('/home/francisco/Desktop/TheSteamHourCalc/tests/gameslist.json') as f:
        data = json.load(f)

    games = Game_transformer().transform_games_list(data)

    for game in games:
        assert type(game) == Game
