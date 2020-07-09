from app import app
import pytest

@pytest.fixture
def client():
    return app.test_client()

def test_api_returns_steam_id(client):
    response = client.get('/howmuchtimehaveiwasted/42069')
    assert response.data == b'Your steam id is:42069'

