
from app.core.config import settings
import json


def test_create_household_ledger(client, auth_user):
    # when
    payload = {
        'user_id': 1,
        'money': 10000,
        'content': '식비',
    }
    response = client.post(f'{settings.API_V1_STR}/household_ledger/create', json.dumps(payload))

    # then
    assert response.status_code == 200


def test_update_household_ledger(client, auth_user):
    # when
    payload = {
        'id': '1',
        'money': 30000,
        'content': '보험료'
    }
    response = client.post(f'{settings.API_V1_STR}/household_ledger/update', json.dumps(payload))

    # then
    assert response.status_code == 200


def test_delete_household_ledger(client, auth_user):
    # when
    payload = {
        'id': '1',
        'is_deleted': 1,
    }
    response = client.post(f'{settings.API_V1_STR}/household_ledger/delete', json.dumps(payload))

    # then
    assert response.status_code == 200
