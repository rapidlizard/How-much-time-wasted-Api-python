from models.user import User
from models.game import Game
from models.rating import Rating
from services.rating_calc import Rating_calc
from models.csgo_stats import Csgo_stats
from models.gun_stats import Gun_stats
import pytest
import json


@pytest.fixture
def user_json():
    with open('/home/francisco/Desktop/TheSteamHourCalc/tests/testdata/expected/user.json') as f:
        user_json = json.load(f)
    return user_json


@pytest.fixture
def gun_stats():
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


@pytest.fixture
def user(gun_stats):
    return User(
        name='Lixard',
        img='https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/4a/4ad45031967e52ce05f28c7f5591227e66715c5d_full.jpg',
        url='https://steamcommunity.com/profiles/76561198066000502/',
        created=1340730740,
        games=[
            Game(appid=10, playtime=82),
            Game(appid=80, playtime=0),
            Game(appid=100, playtime=0),
            Game(appid=240, playtime=98)
        ],
        rating_calc=Rating_calc(),
        csgo_stats=Csgo_stats(
            defused_bombs=717,
            hours=5272693,
            knife_kills=1177,
            money_earned=278525408,
            mvps=29980,
            planted_bombs=2732,
            shots_fired=2231475,
            shots_hit=552856,
            total_deaths=103202,
            total_kills=214095,
            total_wins=56101,
            gun_stats=gun_stats
        )
    )


@pytest.fixture
def gun_stats_json():
    with open('/home/francisco/Desktop/TheSteamHourCalc/tests/testdata/expected/gun_stats.json') as f:
        user_json = json.load(f)
    return user_json


def test_user_to_json_returns_json(user, user_json):
    expected = user_json

    assert user.to_json() == expected


def test_user_calculates_total_hours(user):
    expected = 3

    assert user.total_hours == expected


def test_user_calculates_score(user):
    expected = 4

    assert user.score == expected


def test_user_calculates_rating(user):
    expected = Rating(title='What even are games?',
                      description='Seriously what are they???')

    assert user.rating.title == expected.title
    assert user.rating.description == expected.description


def test_game_has_atributes():
    game = Game(appid=10, playtime=1000)

    assert game.appid == 10
    assert game.playtime == 1000


def test_game_to_json_returns_json():
    expected = {
        'appid': 10,
        'playtime': 1000
    }

    game = Game(appid=10, playtime=1000)
    result = game.to_json()

    assert result == expected


def test_rating_to_json_returns_json():
    expected = {
        'title': 'hello',
        'description': 'world'
    }

    rating = Rating(title='hello', description='world')
    result = rating.to_json()

    assert result == expected


def test_csgo_stats_calculates_accuracy_percent(gun_stats):
    csgo_stats = Csgo_stats(
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
        shots_hit=500,
        gun_stats=gun_stats
    )

    assert csgo_stats.accuracy == 50.0


def test_csgo_stats_rounds_accuracy_percent_to_2_decimal_places(gun_stats):
    csgo_stats = Csgo_stats(
        hours=1000,
        total_kills=1000,
        total_deaths=100,
        defused_bombs=1000,
        planted_bombs=1000,
        money_earned=1000,
        mvps=1000,
        total_wins=1000,
        knife_kills=1000,
        shots_fired=15643,
        shots_hit=6450,
        gun_stats=gun_stats
    )

    assert csgo_stats.accuracy == 41.23


def test_csgo_stats_calculates_kd_ratio(gun_stats):
    csgo_stats = Csgo_stats(
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
        gun_stats=gun_stats
    )

    result = csgo_stats.kd_ratio

    assert result == 10


def test_csgo_stats_kd_ratio_calc_rounds_to_2_decimal_places(gun_stats):
    csgo_stats = Csgo_stats(
        hours=1000,
        total_kills=4957,
        total_deaths=1260,
        defused_bombs=1000,
        planted_bombs=1000,
        money_earned=1000,
        mvps=1000,
        total_wins=1000,
        knife_kills=1000,
        shots_fired=1000,
        shots_hit=1000,
        gun_stats=gun_stats
    )

    result = csgo_stats.kd_ratio

    assert result == 3.93


def test_csgo_stats_to_json_returns_json():
    expected = {
        'hours': 1000,
        'total_kills': 1000,
        'total_deaths': 100,
        'defused_bombs': 1000,
        'planted_bombs': 1000,
        'money_earned': 1000,
        'mvps': 1000,
        'total_wins': 1000,
        'knife_kills': 1000,
        'shots_fired': 1000,
        'shots_hit': 1000,
        'accuracy': 100.0,
        'kd_ratio': 10
    }

    csgo_stats = Csgo_stats(
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
        gun_stats=gun_stats
    )
    result = csgo_stats.to_json()

    assert result == expected


def test_gun_stats_to_json_returns_json(gun_stats, gun_stats_json):
    expected = gun_stats_json

    assert gun_stats.to_json() == expected
