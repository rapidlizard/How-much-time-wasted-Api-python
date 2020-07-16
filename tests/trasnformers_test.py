from models.game import Game
from models.user import User
from models.csgo_stats import Csgo_stats
from models.gun_stats import Gun_stats
from transformers.user_transformer import User_transformer
from transformers.game_transformer import Game_transformer
from transformers.csgo_stats_transformer import Csgo_stats_transformer
from transformers.gun_stats_transformer import Gun_stats_transformer


import json
import pytest


@pytest.fixture
def user_data():
    with open('/home/francisco/Desktop/TheSteamHourCalc/tests/testdata/inputs/userdata.json') as f:
        user_data = json.load(f)
    return user_data


@pytest.fixture
def games_data():
    with open('/home/francisco/Desktop/TheSteamHourCalc/tests/testdata/inputs/gamesdata.json') as f:
        games = json.load(f)
    return games


@pytest.fixture
def csgo_stats_data():
    with open('/home/francisco/Desktop/TheSteamHourCalc/tests/testdata/inputs/statsdata.json') as f:
        stats = json.load(f)
    return stats


@pytest.fixture
def gun_stats_obj():
    return Gun_stats(
        glock=7100,
        deagle=12602,
        elite=150,
        fiveseven=679,
        xm10=394,
        mac10=1169,
        ump=1576,
        p90=1128,
        awp=33620,
        ak47=107332,
        aug=1584,
        famas=721,
        g3sg1=222,
        m249=220,
        p2000=8907,
        p250=2403,
        sg556=1787,
        scar20=233,
        scout=1593,
        mp7=1593,
        mp9=932,
        nova=208,
        negev=299,
        sawedoff=112,
        bizon=386,
        tec9=463,
        mag7=137,
        m4a1=23951,
        galil=752
    )


def test_user_transformer_turns_user_data_into_user_obj(user_data, gun_stats_obj):
    games = [
        Game(appid=10, playtime=4600),
        Game(appid=20, playtime=2000)
    ]
    stats = Csgo_stats(
        hours=1000,
        total_kills=1000,
        total_deaths=100,
        defused_bombs=1000,
        planted_bombs=1000,
        money_earned=1000,
        mvps=1000,
        total_wins=1000,
        knife_kills=1000,
        shots_fired=1000,
        shots_hit=1000,
        gun_stats=gun_stats_obj
    )

    user = User_transformer().transform_user(user_data, games, stats)

    assert isinstance(user, User)


def test_user_transformer_returns_user_obj_with_correct_atributes(user_data):
    games = [
        Game(appid=10, playtime=4600),
        Game(appid=20, playtime=2000)
    ]
    stats = Csgo_stats(
        hours=1000,
        total_kills=1000,
        total_deaths=100,
        defused_bombs=1000,
        planted_bombs=1000,
        money_earned=1000,
        mvps=1000,
        total_wins=1000,
        knife_kills=1000,
        shots_fired=1000,
        shots_hit=1000,
        gun_stats=gun_stats_obj
    )

    user = User_transformer().transform_user(user_data, games, stats)

    assert user.name == 'Lixard'
    assert user.img == 'https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/4a/4ad45031967e52ce05f28c7f5591227e66715c5d_full.jpg'
    assert user.url == 'https://steamcommunity.com/profiles/76561198066000502/'
    assert user.created == 1340730740
    assert user.games == games
    assert user.csgo_stats == stats


def test_game_transformer_turns_game_data_into_game_obj():
    data = {
        "appid": 17390,
        "playtime_forever": 3257,
        "playtime_windows_forever": 0,
        "playtime_mac_forever": 0,
        "playtime_linux_forever": 0
    }

    game = Game_transformer().transform_game(data)

    assert isinstance(game, Game)


def test_game_transformer_turns_each_game_in_games_data_into_game_obj(games_data):
    games = Game_transformer().transform_games_list(games_data)

    for game in games:
        assert isinstance(game, Game)


def test_game_transformer_returns_game_obj_with_correct_atributes():
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


def test_csgo_stats_transformer_turns_stats_data_into_csgo_stats_obj(csgo_stats_data, gun_stats_obj):
    csgo_stats = Csgo_stats_transformer().transform_csgo_stats(
        csgo_stats_data, gun_stats_obj)

    assert isinstance(csgo_stats, Csgo_stats)


def test_csgo_stats_transformer_returns_obj_with_correct_atributes(csgo_stats_data, gun_stats_obj):
    csgo_stats = Csgo_stats_transformer().transform_csgo_stats(
        csgo_stats_data, gun_stats_obj)

    assert csgo_stats.hours == 5272693
    assert csgo_stats.total_kills == 214095
    assert csgo_stats.defused_bombs == 717
    assert csgo_stats.planted_bombs == 2732
    assert csgo_stats.money_earned == 278525408
    assert csgo_stats.mvps == 29980
    assert csgo_stats.total_wins == 56101
    assert csgo_stats.knife_kills == 1177
    assert csgo_stats.shots_fired == 2231475
    assert csgo_stats.shots_hit == 552856
    assert csgo_stats.total_deaths == 103202
    assert csgo_stats.gun_stats == gun_stats_obj


def test_gun_stats_transformer_returns_gun_stats_obj(csgo_stats_data):
    gun_stats = Gun_stats_transformer().transform_gun_stats(csgo_stats_data)

    assert isinstance(gun_stats, Gun_stats)


def test_gun_stats_transformer_returns_obj_with_correct_attributes(csgo_stats_data):
    gun_stats = Gun_stats_transformer().transform_gun_stats(csgo_stats_data)

    assert gun_stats.glock == 7100
    assert gun_stats.deagle == 12602
    assert gun_stats.elite == 150
    assert gun_stats.fiveseven == 679
    assert gun_stats.xm10 == 394
    assert gun_stats.mac10 == 1169
    assert gun_stats.ump == 1576
    assert gun_stats.p90 == 1128
    assert gun_stats.awp == 33620
    assert gun_stats.ak47 == 107332
    assert gun_stats.aug == 1584
    assert gun_stats.famas == 721
    assert gun_stats.g3sg1 == 222
    assert gun_stats.m249 == 220
    assert gun_stats.p2000 == 8907
    assert gun_stats.p250 == 2403
    assert gun_stats.sg556 == 1787
    assert gun_stats.scar20 == 233
    assert gun_stats.scout == 1593
    assert gun_stats.mp7 == 1329
    assert gun_stats.mp9 == 932
    assert gun_stats.nova == 208
    assert gun_stats.negev == 299
    assert gun_stats.sawedoff == 112
    assert gun_stats.bizon == 386
    assert gun_stats.tec9 == 463
    assert gun_stats.mag7 == 137
    assert gun_stats.m4a1 == 23951
    assert gun_stats.galil == 752
