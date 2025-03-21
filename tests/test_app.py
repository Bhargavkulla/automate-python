import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_hello(client):
    """Test the hello endpoint"""
    rv = client.get('/')
    assert rv.data == b'Hello, Jenkins!'
