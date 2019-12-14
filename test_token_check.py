import pytest
import requests

from user_data import USER_DATA_CHECK as users


@pytest.mark.parametrize(
    "user", users['positive'],)
def test_positive(env, user):
    """Check positive response on check page"""
    data = {
        'login': user['user_name'],
        'token': user['token']
    }
    response = requests.post('%s/app/check/' % env, data)
    assert(user['response'] in response.text)


@pytest.mark.parametrize(
    "user", users['positive'],)
def test_positive_2(env, user):
    """Check positive response on check page"""
    data = {
        'login': user['user_name'],
        'token': user['token']
    }
    response = requests.post('%s/app/check/' % env, data)
    assert('Error' not in response.text)



@pytest.mark.parametrize(
    "user", users['negative'],)
def test_negative(env, user):
    """Check negative response on check page with wrong user data"""
    data = {
        'login': user['user_name'],
        'token': user['token']
    }
    response = requests.post('%s/app/check/' % env, data)
    assert(user['response'] in response.text)


@pytest.mark.parametrize(
    "user", users['negative'],)
def test_negative_2(env, user):
    """Check negative response on check page with wrong params"""
    data = {
        user['user_name']: 'login',
        user['token']: 'token'
    }
    response = requests.post('%s/app/check/' % env, data)
    assert('Error:' in response.text)


def test_negative_3(env):
    """Check negative response on GET request"""
    response = requests.get('%s/app/check/' % env)
    assert('Wrong request type' in response.text)
