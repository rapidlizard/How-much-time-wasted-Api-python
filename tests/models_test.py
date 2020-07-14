from models.user import User
from models.game import Game
from models.rating import Rating
from models.rating_calc import Rating_calc
from models.csgo_stats import Csgo_stats
import pytest


@pytest.fixture
def user():
    user = User(
        name='Lixard',
        img='https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/4a/4ad45031967e52ce05f28c7f5591227e66715c5d_full.jpg',
        url='https://steamcommunity.com/profiles/76561198066000502/',
        created=1340730740,
        games=[
            Game(appid=10, playtime=4600),
            Game(appid=20, playtime=2000)
        ],
        rating_calc=Rating_calc(),
        csgo_stats=Csgo_stats(
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
            shots_hit=1000
        )
    )

    return user


def test_user_to_json_returns_json(user):
    expected = {
        'name': 'Lixard',
        'img': 'https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/4a/4ad45031967e52ce05f28c7f5591227e66715c5d_full.jpg',
        'url': 'https://steamcommunity.com/profiles/76561198066000502/',
        'created': 1340730740,
        'total_hours': 110,
        'score': 6050,
        'games': [
            {
                'appid': 10,
                'playtime': 4600
            },
            {
                'appid': 20,
                'playtime': 2000
            }
        ],
        'rating': {
            'title': 'You might aswell just play mobile games',
            'description': 'Sponsored by RAID: Shadow Legends'
        },
        'csgo_stats': {
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
            'accuracy': 100.0
        }
    }

    result = user.to_json()

    assert result == expected


def test_user_calculates_total_hours(user):
    expected = 110

    assert user.total_hours == expected


def test_user_calculates_score(user):
    expected = 6050

    assert user.score == expected


def test_user_calculates_rating(user):
    expected = Rating(title='You might aswell just play mobile games',
                      description='Sponsored by RAID: Shadow Legends')

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


def test_csgo_stats_calculates_accuracy_percent():
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
        shots_hit=500
    )

    assert csgo_stats.accuracy == 50.0


def test_csgo_stats_rounds_accuracy_percent_to_2_decimal_places():
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
        shots_hit=6450
    )

    assert csgo_stats.accuracy == 41.23


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
        'accuracy': 100.0
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
        shots_hit=1000
    )
    result = csgo_stats.to_json()

    assert result == expected


def test_csgo_stats_calculates_kd_ratio():
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
        shots_hit=1000
    )

    result = csgo_stats.kd_ratio

    assert result == 10


def test_csgo_stats_kd_ratio_calc_rounds_to_2_decimal_places():
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
        shots_hit=1000
    )

    result = csgo_stats.kd_ratio

    assert result == 3.93
