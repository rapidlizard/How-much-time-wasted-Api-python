from models.game import Game
from models.user import User
from models.csgo_stats import Csgo_stats
from models.user_transformer import User_transformer
from models.game_transformer import Game_transformer
from models.csgo_stats_transformer import Csgo_stats_transformer


import json
import pytest


@pytest.fixture
def user_data():
    with open('/home/francisco/Desktop/TheSteamHourCalc/tests/mockdata/userdata.json') as f:
        user_data = json.load(f)
    return user_data


@pytest.fixture
def games():
    with open('/home/francisco/Desktop/TheSteamHourCalc/tests/mockdata/gamesdata.json') as f:
        games = json.load(f)
    return games


@pytest.fixture
def csgo_stats():
    with open('/home/francisco/Desktop/TheSteamHourCalc/tests/mockdata/userstats.json') as f:
        stats = json.load(f)
    return stats


def test_user_transformer_turns_user_data_into_user_obj(user_data):
    games = [
        Game(appid=10, playtime=4600),
        Game(appid=20, playtime=2000)
    ]
    user = User_transformer().transform_user(user_data, games)

    assert type(user) == User
    assert user.name == 'Lixard'
    assert user.img == 'https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/4a/4ad45031967e52ce05f28c7f5591227e66715c5d_full.jpg'
    assert user.url == 'https://steamcommunity.com/profiles/76561198066000502/'
    assert user.created == 1340730740
    assert user.games == games


def test__game_transformer_turns_game_data_into_game_obj():
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


def test_game_transformer_turns_each_game_in_games_data_into_game_obj(games):
    games = Game_transformer().transform_games_list(games)

    for game in games:
        assert type(game) == Game


def test_csgo_stats_transformer_turns_stats_data_into_csgo_stats_obj(csgo_stats):
    csgo_stats = Csgo_stats_transformer().transform_csgo_stats(csgo_stats)

    assert isinstance(csgo_stats, Csgo_stats) == True


def test_csgo_stats_transformer_returns_obj_with_correct_atributes(csgo_stats):
    csgo_stats = Csgo_stats_transformer().transform_csgo_stats(csgo_stats)

    assert csgo_stats.hours == 5272693
