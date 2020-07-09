import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from app import app
import pytest

@pytest.fixture
def client():
    return app.test_client()

@pytest.fixture
def steamid():
    return "76561198066000502"

def test_api_returns_user_json(client, steamid):
    response = client.get('/howmuchtimehaveiwasted/' + steamid)

    assert response.status_code == 200
    assert response.get_json() == {
        'name': 'Lixard',
        'img': 'https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/4a/4ad45031967e52ce05f28c7f5591227e66715c5d_full.jpg',
        'url': 'https://steamcommunity.com/profiles/76561198066000502/',
        'created': '1340730740'
    }


