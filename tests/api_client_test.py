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
def mock_stats_json():
    with open('/home/francisco/Desktop/TheSteamHourCalc/tests/mockjson/stats.json') as f:
        stats = json.load(f)
    return stats


@pytest.fixture
def user_data():
    with open('/home/francisco/Desktop/TheSteamHourCalc/tests/testdata/userdata.json') as f:
        user_data = json.load(f)
    return user_data


@pytest.fixture
def user_games():
    with open('/home/francisco/Desktop/TheSteamHourCalc/tests/testdata/gamesdata.json') as f:
        games = json.load(f)
    return games


@pytest.fixture
def user_stats():
    with open('/home/francisco/Desktop/TheSteamHourCalc/tests/testdata/userstats.json') as f:
        stats = json.load(f)
    return stats


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


def test_steam_client_gets_csgo_stats(requests_mock, mock_stats_json, user_stats, steamid):
    requests_mock.get(
        'http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid=730&key=2FA14ED02A1D7CCC0E4FCA80AE6AE194&steamid=' + steamid, json=mock_stats_json)

    resp = Steam().get_user_csgo_stats(steamid)

    assert resp == user_stats


def test_steam_client_returns_user_data_with_correct_atributes(steamid):
    data = Steam().get_user_data(steamid)

    assert 'personaname' in data
    assert 'avatarfull' in data
    assert 'profileurl' in data
    assert 'timecreated' in data


def test_steam_client_returns_games_list_with_correct_atributes(steamid):
    data = Steam().get_user_games(steamid)

    for game in data:
        assert 'appid' in game
        assert 'playtime_forever' in game


def test_steam_client_returns_csgo_stats_data_with_correct_attributes(steamid):
    data = Steam().get_user_csgo_stats(steamid)

    assert 'total_time_played' in data
    assert 'total_kills' in data
    assert 'total_defused_bombs' in data
    assert 'total_planted_bombs' in data
    assert 'total_money_earned' in data
    assert 'total_mvps' in data
    assert 'total_wins' in data
    assert 'total_weapons_donated' in data
    assert 'total_kills_knife' in data
    assert 'total_matches_won' in data
    assert 'total_matches_played' in data
    assert 'total_shots_fired' in data
    assert 'total_shots_hit' in data
    assert 'total_deaths' in data


def test_steam_returns_csgo_stats_with_correct_gun_stats(steamid):
    data = Steam().get_user_csgo_stats(steamid)

    assert "total_kills_hegrenade" in data
    assert "total_kills_glock" in data
    assert "total_kills_deagle" in data
    assert "total_kills_elite" in data
    assert "total_kills_fiveseven" in data
    assert "total_kills_xm1014" in data
    assert "total_kills_mac10" in data
    assert "total_kills_ump45" in data
    assert "total_kills_p90" in data
    assert "total_kills_awp" in data
    assert "total_kills_ak47" in data
    assert "total_kills_aug" in data
    assert "total_kills_famas" in data
    assert "total_kills_g3sg1" in data
    assert "total_kills_m249" in data
    assert "total_kills_hkp2000" in data
    assert "total_kills_p250" in data
    assert "total_kills_sg556" in data
    assert "total_kills_scar20" in data
    assert "total_kills_ssg08" in data
    assert "total_kills_mp7" in data
    assert "total_kills_mp9" in data
    assert "total_kills_nova" in data
    assert "total_kills_negev" in data
    assert "total_kills_sawedoff" in data
    assert "total_kills_bizon" in data
    assert "total_kills_tec9" in data
    assert "total_kills_mag7" in data
    assert "total_kills_m4a1" in data
    assert "total_kills_galilar" in data
    assert "total_kills_molotov" in data
    assert "total_kills_decoy" in data
    assert "total_kills_taser" in data
