import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from models.api_client import Steam

def test_steam_returns_user_data():
    data = Steam.get_user()
    assert type(data) == dict