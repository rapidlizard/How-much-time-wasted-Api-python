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
def user_data():
    with open('/home/francisco/Desktop/TheSteamHourCalc/tests/mockdata/userdata.json') as f:
        user_data = json.load(f)
    return user_data


@pytest.fixture
def user_games():
    with open('/home/francisco/Desktop/TheSteamHourCalc/tests/mockdata/gamesdata.json') as f:
        games = json.load(f)
    return games


def test_steam_client_gets_user(user_data, mock_user_json, requests_mock):
    test_id = '2FA14ED02A1D7CCC0E4FCA80AE6AE194'
    requests_mock.get('http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=2FA14ED02A1D7CCC0E4FCA80AE6AE194&steamids=2FA14ED02A1D7CCC0E4FCA80AE6AE194',
                      json=mock_user_json)

    resp = Steam().get_user_data(test_id)

    assert resp == user_data


def test_steam_client_returns_user_data(steamid, user_data):
    data = Steam().get_user_data(steamid)

    assert data == user_data


def test_steam_client_returns_correct_user(steamid):
    data = Steam().get_user_data(steamid)

    assert data['steamid'] == steamid


def test_steam_client_returns_games_list(steamid, user_games):
    data = Steam().get_user_games(steamid)

    assert data == user_games
