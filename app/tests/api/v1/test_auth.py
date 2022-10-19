from app.core.config import settings
import json


def test_login(client):
    # when
    response = client.post(f'{settings.API_V1_STR}/auth/login', {'username': 'test@test.com', 'password': '123'})

    # then
    assert response.status_code == 200
    assert response.json() == {
        'id': 1,
        'email': 'test@test.com',
    }


def test_signup(client):
    # when
    payload = {
        'email': 'test@test.co.kr',
        'password': '123',
    }
    response = client.post(f'{settings.API_V1_STR}/auth/signup', json.dumps(payload))

    # then
    assert response.status_code == 200
