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
        'created': '1340730740',
        'games': []
    }


def test_api_returns_error_if_given_bad_steamid(client):
    bad_steamid = '42069'

    response = client.get('/howmuchtimehaveiwasted/' + bad_steamid)

    assert response.status_code == 400
    assert response.get_json() == 'There was a problem finding that user'


def test_api_returns_error_if_steamid_not_given(client):
    response = client.get('/howmuchtimehaveiwasted/')

    assert response.status_code == 400
    assert response.get_json() == 'Please provide a steamid'
