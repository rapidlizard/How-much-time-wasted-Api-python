from models.user import User
from models.game import Game


def test_user_has_atributes():
    user = User(
        name='Lixard',
        img='https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/4a/4ad45031967e52ce05f28c7f5591227e66715c5d_full.jpg',
        url='https://steamcommunity.com/profiles/76561198066000502/',
        created=1340730740,
        games=['hello', 'world'],
    )

    assert user.name == 'Lixard'
    assert user.img == 'https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/4a/4ad45031967e52ce05f28c7f5591227e66715c5d_full.jpg'
    assert user.url == 'https://steamcommunity.com/profiles/76561198066000502/'
    assert user.created == 1340730740
    assert user.games == ['hello', 'world']


def test_user_to_json_returns_json():
    expected = {
        'name': 'Lixard',
        'img': 'https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/4a/4ad45031967e52ce05f28c7f5591227e66715c5d_full.jpg',
        'url': 'https://steamcommunity.com/profiles/76561198066000502/',
        'created': 1340730740,
        'games': [
            'hello',
            'world'
        ]
    }

    user = User(
        name='Lixard',
        img='https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/4a/4ad45031967e52ce05f28c7f5591227e66715c5d_full.jpg',
        url='https://steamcommunity.com/profiles/76561198066000502/',
        created=1340730740,
        games=['hello', 'world'],
    )
    result = user.to_json()

    assert result == expected


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
