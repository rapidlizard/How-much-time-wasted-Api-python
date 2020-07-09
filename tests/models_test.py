import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from models.user import User

def test_user_has_atributes():
    user = User(name='Lixard', img='myimg.jpg', url='myurl.com', created='10/10/2012')
    assert user.name == 'Lixard'
    assert user.img == 'myimg.jpg'
    assert user.url == 'myurl.com'
    assert user.created == '10/10/2012'