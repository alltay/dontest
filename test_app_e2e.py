import pytest
import requests
import json
import time

from user_data import USER_DATA_GENERATE as users
from user_data import USER_DATA_E2E as users_e2e


@pytest.mark.slow
@pytest.mark.parametrize(
    "user", users['positive'],)
def test_positive_e2e(env, user):
    """Check positive response on generate page"""
    data = {
        'login': user['user_name'],
        'password': user['user_password']
    }
    response = requests.post('%s/app/generate/' % env, data)
    time.sleep(61)
    data = {
        'login': user['user_name'],
        'token': json.loads(response.text)['message']['token']
    }
    response = requests.post('%s/app/check/' % env, data)
    assert('Error' not in response.text)


@pytest.mark.slow
@pytest.mark.parametrize(
    "user", users['positive'],)
def test_negative_e2e(env, user):
    """Check negative response on fast requests"""
    time.sleep(61)
    data = {
        'login': user['user_name'],
        'password': user['user_password']
    }
    response = requests.post('%s/app/generate/' % env, data)
    data = {
        'login': user['user_name'],
        'token': json.loads(response.text)['message']['token']
    }
    response = requests.post('%s/app/check/' % env, data)
    assert('Token is in use' in response.text)


@pytest.mark.slow
@pytest.mark.parametrize(
    "user", users['positive'],)
def test_negative2_e2e(env, user):
    """Check negative response on double login"""
    time.sleep(61)
    data = {
        'login': user['user_name'],
        'password': user['user_password']
    }
    response = requests.post('%s/app/generate/' % env, data)
    data = {
        'login': user['user_name'],
        'password': user['user_password']
    }
    response = requests.post('%s/app/generate/' % env, data)
    assert('No free tokens' in response.text)


@pytest.mark.slow
@pytest.mark.parametrize(
    "user", users['positive'],)
def test_negative3_e2e(env, user):
    """Check negative response on login when token already in use"""
    time.sleep(61)
    data = {
        'login': user['user_name'],
        'password': user['user_password']
    }
    response = requests.post('%s/app/generate/' % env, data)
    time.sleep(61)
    data = {
        'login': user['user_name'],
        'token': json.loads(response.text)['message']['token']
    }
    requests.post('%s/app/check/' % env, data)
    response = requests.post('%s/app/check/' % env, data)
    assert('Token is in use' in response.text)


@pytest.mark.parametrize(
    "user", users_e2e['positive'],)
def test_positive2_e2e(env, user):
    """Check multiple sub"""
    for i in range(user['subscription']):
        data = {
            'login': user['user_name'],
            'password': user['user_password']
        }
        response = requests.post('%s/app/generate/' % env, data)
    assert('Error' not in response.text)







# response = requests.post('http://127.0.0.1:8000/app/generate/', {'login': 'test_dont_tuch_3', 'password': 'zxc12345'})
# print(json.loads(response.text)['message'])

response = requests.post('http://127.0.0.1:8000/app/check/', {'login': 'test_dont_tuch_3', 'token': 'yrmyfsgegt'})
print(json.loads(response.text)['message'])