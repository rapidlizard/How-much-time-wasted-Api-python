import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from models.user import User

def test_user_has_atribute_steam_id():
    user = User('123')
    assert user.steam_id == '123'