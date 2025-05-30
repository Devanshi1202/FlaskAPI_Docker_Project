import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_get_users(client):
    response = client.get('/users')
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)


def test_post_user(client):
    payload = {'name': 'Test User', 'email': 'test@example.com'}
    response = client.post('/users', json=payload)
    assert response.status_code == 201
    assert 'id' in response.get_json()
