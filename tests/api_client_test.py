import pytest
import json
import requests
from models.api_client import Steam


@pytest.fixture
def steamid():
    return "76561198066000502"


@pytest.fixture
def mock_user_json():
    with open('/home/francisco/Desktop/TheSteamHourCalc/tests/mockjson/user.json') as f:
        user_json = json.load(f)
    return user_json


@pytest.fixture
def mock_games_json():
    with open('/home/francisco/Desktop/TheSteamHourCalc/tests/mockjson/games.json') as f:
        games_json = json.load(f)
    return games_json


@pytest.fixture
def user_data():
    with open('/home/francisco/Desktop/TheSteamHourCalc/tests/mockdata/userdata.json') as f:
        user_data = json.load(f)
    return user_data


@pytest.fixture
def user_games():
    with open('/home/francisco/Desktop/TheSteamHourCalc/tests/mockdata/gamesdata.json') as f:
        games = json.load(f)
    return games


def test_steam_client_gets_user(requests_mock, user_data, mock_user_json, steamid):
    requests_mock.get('http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=2FA14ED02A1D7CCC0E4FCA80AE6AE194&steamids=' + steamid,
                      json=mock_user_json)

    resp = Steam().get_user_data(steamid)

    assert resp == user_data


def test_steam_client_gets_games(requests_mock, user_games, mock_games_json, steamid):
    requests_mock.get('http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=2FA14ED02A1D7CCC0E4FCA80AE6AE194&steamid=' + steamid,
                      json=mock_games_json)

    resp = Steam().get_user_games(steamid)

    assert resp == user_games


def test_steam_client_returns_correct_user(requests_mock, mock_user_json, steamid):
    requests_mock.get('http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=2FA14ED02A1D7CCC0E4FCA80AE6AE194&steamids=' + steamid,
                      json=mock_user_json)

    resp = Steam().get_user_data(steamid)
    assert resp['steamid'] == steamid


def test_steam_client_returns_user_data_with_correct_atributes(steamid, user_data):
    data = Steam().get_user_data(steamid)

    assert 'personaname' in data
    assert 'avatarfull' in data
    assert 'profileurl' in data
    assert 'timecreated' in data


def test_steam_client_returns_games_list_with_correct_atributes(steamid, user_games):
    data = Steam().get_user_games(steamid)

    for game_data in data:
        assert 'appid' in game_data
        assert 'playtime_forever' in game_data
