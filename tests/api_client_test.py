import pytest
import json

from models.api_client import Steam


@pytest.fixture
def steamid():
    return "76561198066000502"


@pytest.fixture
def user_data():
    return {
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


@pytest.fixture
def user_games():
    with open('/home/francisco/Desktop/TheSteamHourCalc/tests/gameslist.json') as f:
        games = json.load(f)
    return games


def test_steam_client_returns_user_data(steamid, user_data):
    data = Steam().get_user_data(steamid)

    assert data == user_data


def test_steam_client_returns_correct_user(steamid):
    data = Steam().get_user_data(steamid)

    assert data['steamid'] == steamid


def test_steam_client_returns_games_list(steamid, user_games):
    data = Steam().get_user_games(steamid)

    assert data == user_games
