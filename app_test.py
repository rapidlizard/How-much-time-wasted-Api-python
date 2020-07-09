from app import app
from models.user import User
import pytest

@pytest.fixture
def client():
    return app.test_client()

def test_api_returns_steam_id(client):
    response = client.get('/howmuchtimehaveiwasted/42069')
    assert response.data == b'Your steam id is:42069'

def test_user_has_atribute_steam_id():
    user = User('123')
    assert user.steam_id == '123'
