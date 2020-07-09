import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

import pytest

from models.api_client import Steam

@pytest.fixture
def steamid():
    return "76561198066000502"

def test_steam_client_returns_json(steamid):
    data = Steam.get_user(steamid)

    assert type(data) == dict

def test_steam_client_returns_user_data_without_wrapping(steamid):
    expected = {
        "steamid": steamid,
        "communityvisibilitystate":3,
        "profilestate":1,
        "personaname":"Lixard",
        "commentpermission":1,
        "profileurl":"https://steamcommunity.com/profiles/76561198066000502/",
        "avatar":"https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/4a/4ad45031967e52ce05f28c7f5591227e66715c5d.jpg",
        "avatarmedium":"https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/4a/4ad45031967e52ce05f28c7f5591227e66715c5d_medium.jpg",
        "avatarfull":"https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/4a/4ad45031967e52ce05f28c7f5591227e66715c5d_full.jpg",
        "avatarhash":"4ad45031967e52ce05f28c7f5591227e66715c5d",
        "lastlogoff":1594245076,
        "personastate":0,
        "primaryclanid":"103582791463737200",
        "timecreated":1340730740,
        "personastateflags":4,
        "loccountrycode":"PT",
        "locstatecode":"14"
    }

    data = Steam.get_user(steamid)

    assert data == expected

def test_steam_client_returns_correct_user(steamid):

    data = Steam.get_user(steamid)

    assert data['steamid'] == steamid