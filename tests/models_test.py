import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from models.user import User
from models.game import Game

def test_user_has_atributes():
    user = User(
        name='Lixard', 
        img='myimg.jpg', 
        url='myurl.com', 
        created='10/10/2012'
        )

    assert user.name == 'Lixard'
    assert user.img == 'myimg.jpg'
    assert user.url == 'myurl.com'
    assert user.created == '10/10/2012'

def test_user_to_json_returns_json():
    user = User(name='Lixard', img='myimg.jpg', url='myurl.com', created='10/10/2012')
    expected = {
        'name': 'Lixard',
        'img': 'myimg.jpg',
        'url': 'myurl.com',
        'created': '10/10/2012'
    }
    
    result = user.to_json()

    assert result == expected

def test_game_has_atributes():
    game = Game(appid= 10, playtime=1000)

    assert game.appid == 10
    assert game.playtime == 1000