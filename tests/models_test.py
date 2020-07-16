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
def csgo_stats_json():
    with open('/home/francisco/Desktop/TheSteamHourCalc/tests/testdata/expected/csgo_stats.json') as f:
        csgo_stats_json = json.load(f)
    return csgo_stats_json


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
def csgo_stats(gun_stats):
    return Csgo_stats(
        hours=5272693,
        total_kills=214095,
        total_deaths=103202,
        defused_bombs=717,
        planted_bombs=2732,
        money_earned=278525408,
        mvps=29980,
        total_wins=56101,
        knife_kills=1177,
        shots_fired=2231475,
        shots_hit=552856,
        rescued_hostages=507,
        headshots=117038,
        weapons_donated=8067,
        dominations=3711,
        revenges=317,
        broken_windows=98,
        gun_stats=gun_stats
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
            rescued_hostages=507,
            headshots=117038,
            weapons_donated=8067,
            dominations=3711,
            revenges=317,
            broken_windows=98,
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


def test_game_has_attributes():
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


def test_csgo_stats_calculates_accuracy_percent(csgo_stats):

    assert csgo_stats.accuracy == 24.78


def test_csgo_stats_calculates_kd_ratio(csgo_stats):
    result = csgo_stats.kd_ratio

    assert result == 2.07


def test_csgo_stats_calculates_headshot_percentage(csgo_stats):
    result = csgo_stats.headshot_percentage

    assert result == 54.67


def test_csgo_stats_to_json_returns_json(csgo_stats, csgo_stats_json):
    expected = csgo_stats_json

    result = csgo_stats.to_json()

    assert result == expected


def test_gun_stats_to_json_returns_json(gun_stats, gun_stats_json):
    expected = gun_stats_json

    assert gun_stats.to_json() == expected
