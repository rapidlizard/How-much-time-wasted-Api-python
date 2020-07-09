import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from app import app
import pytest

@pytest.fixture
def client():
    return app.test_client()

def test_api_returns_user_json(client):
    response = client.get('/howmuchtimehaveiwasted')
    assert response.get_json() == {
        'name': 'lizard',
        'img': 'img',
        'url': 'url',
        'created': 'now'
    }


