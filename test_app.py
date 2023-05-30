import json
from datetime import datetime
import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    data = json.loads(response.data)
    
    assert response.status_code == 200
    assert 'current_time' in data
    assert 'random_integer' in data

    # Check if current_time is a valid datetime
    try:
        datetime.fromisoformat(data['current_time'])
    except ValueError:
        assert False, "current_time is not a valid datetime"

    # Check if random_integer is an integer
    assert isinstance(data['random_integer'], int)
