import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from app import app
import pytest

@pytest.fixture
def client():
    return app.test_client()

def test_api_returns_steam_id(client):
    response = client.get('/howmuchtimehaveiwasted/42069')
    assert response.data == b'Your steam id is:42069'


