import pytest
import requests
import json

from user_data import USER_DATA_GENERATE as users


@pytest.mark.parametrize(
    "user", users['positive'],)
def test_positive_e2e(env, user):
    """Check positive response on generate page"""
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
    assert('Error' not in response.text)






# response = requests.post('http://127.0.0.1:8000/app/generate/')

# print(json.loads(response.text)['message'])

