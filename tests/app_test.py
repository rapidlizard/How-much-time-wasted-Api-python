from app import *
import pytest
import json


@pytest.fixture
def client():
    return app.test_client()


@pytest.fixture
def steamid():
    return "76561198066000502"


@pytest.fixture
def json_return():
    with open('/home/francisco/Desktop/TheSteamHourCalc/tests/testdata/fullreturn.json') as data:
        json_return = json.load(data)
    return json_return


# def test_api_returns_user_json(monkeypatch, client, steamid, json_return):

#     def user_mock():
#         with open('/home/francisco/Desktop/TheSteamHourCalc/tests/mockjson/user.json') as data:
#             mock_data = json.load(data)
#         return mock_data

#     def games_mock():
#         with open('/home/francisco/Desktop/TheSteamHourCalc/tests/mockjson/games.json') as data:
#             mock_data = json.load(data)
#         return mock_data

#     monkeypatch.setattr(Steam, 'get_user_data', user_mock)
#     monkeypatch.setattr(Steam, 'get_user_games', games_mock)

#     response = client.get('/howmuchtimehaveiwasted/' + steamid)

#     assert response.status_code == 200
#     assert response.get_json() == json_return


def test_api_returns_error_if_given_bad_steamid(client):
    bad_steamid = '42069'

    response = client.get('/howmuchtimehaveiwasted/' + bad_steamid)

    assert response.status_code == 400
    assert response.get_json() == 'There was a problem finding that user'


def test_api_returns_error_if_steamid_not_given(client):
    response = client.get('/howmuchtimehaveiwasted/')

    assert response.status_code == 400
    assert response.get_json() == 'Please provide a steamid'
