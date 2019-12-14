

USER_DATA_CHECK = {
    'positive': [
        {
            'user_name': 'test_dont_tuch_2',
            'user_password': 'zxc12345',
            'subscription': True,
            'token': 'cdwpftjpmc',
            'response': 'Ok'
        }
    ],
    'negative': [
        {
            'user_name': 'test_dont_tuch_666',
            'user_password': 'zxc12345',
            'subscription': False,
            'token': False,
            'response': 'User not found'
        },
        {
            'user_name': 'test_dont_tuch_1',
            'user_password': 'zxc123456',
            'subscription': False,
            'token': False,
            'response': 'Token not found'
        },
        {
            'user_name': 'test_dont_tuch_6666',
            'user_password': 'zxc123456',
            'subscription': True,
            'token': 'xuisosiguboitriasi',
            'response': 'User not found'
        },
        {
            'user_name': '',
            'user_password': '',
            'subscription': True,
            'token': 'xuisosiguboitriasi',
            'response': 'User not found'
        },
    ]
}

USER_DATA_GENERATE = {
    'positive': [
        {
            'user_name': 'test_dont_tuch_3',
            'user_password': 'zxc12345',
            'subscription': True,
            'token': True
        },
    ],
    'negative': [
        {
            'user_name': 'test_dont_tuch_1',
            'user_password': 'zxc12345',
            'subscription': False,
            'token': False,
            'response': 'No subscription for user'
        },
        {
            'user_name': 'test_dont_tuch_666',
            'user_password': 'zxc12345',
            'subscription': False,
            'token': False,
            'response': 'User not found'
        },
        {
            'user_name': 'test_dont_tuch_1',
            'user_password': 'zxc123456',
            'subscription': False,
            'token': False,
            'response': 'User not found'
        },
        {
            'user_name': 'test_dont_tuch_6666',
            'user_password': 'zxc123456',
            'subscription': True,
            'token': 'xuisosiguboitriasi',
            'response': 'User not found'
        },
        {
            'user_name': '',
            'user_password': '',
            'subscription': True,
            'token': 'xuisosiguboitriasi',
            'response': 'User not found'
        },
    ]
}
