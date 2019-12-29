import pytest
import requests
import time

from user_data import USER_DATA_GENERATE as users


@pytest.mark.parametrize(
    "user", [users['positive'][0]])
def test_positive(env, user):
    """Check positive response on generate page"""
    data = {
        'login': user['user_name'],
        'password': user['user_password']
    }
    response = requests.post('%s/app/generate/' % env, data)
    assert('Error' not in response.text)


@pytest.mark.slow
@pytest.mark.parametrize(
    "user", [users['positive'][0]])
def test_positive_2(env, user):
    """Check what every time generates new token"""
    time.sleep(61)
    data = {
        'login': user['user_name'],
        'password': user['user_password']
    }
    response = requests.post('%s/app/generate/' % env, data)
    response2 = requests.post('%s/app/generate/' % env, data)
    assert(response2.text not in response.text)


@pytest.mark.parametrize(
    "user", users['negative'],)
def test_negative(env, user):
    """Check negative response on generate page with wrong user data"""
    data = {
        'login': user['user_name'],
        'password': user['user_password']
    }
    response = requests.post('%s/app/generate/' % env, data)
    assert(user['response'] in response.text)


@pytest.mark.parametrize(
    "user", users['negative'],)
def test_negative_2(env, user):
    """Check negative response on generate page with wrong params"""
    data = {
        user['user_name']: 'login',
        user['token']: 'password'
    }
    response = requests.post('%s/app/generate/' % env, data)
    assert('Error:' in response.text)


def test_negative_3(env):
    """Check negative response on GET request"""
    response = requests.get('%s/app/generate/' % env)
    assert('Wrong request type' in response.text)


@pytest.mark.parametrize(
    "user", [users['positive'][0]])
def test_negative_4(env, user):
    data = {
        'login': user['user_name'],
        'token': user['token']
    }
    response = requests.post('%s/app/generate/' % env, data)
    assert('Error' not in response.text)
