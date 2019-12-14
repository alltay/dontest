ENVS = [
    {'name': 'local', 'url': 'http://127.0.0.1:8000'},
    {'name': 'prod', 'url': 'http://dongun.herokuapp.com'},
]


def pytest_addoption(parser):
    parser.addoption(
        "--env", action="store", default='local',
        help="run tests on different environment local, prod")


def pytest_generate_tests(metafunc):
    'Return domain for different invironment and special param'
    if "env" in metafunc.fixturenames:
        for env in ENVS:
            end = ENVS[0]['url']
            if metafunc.config.getoption("env") == env['name']:
                end = env['url']
        metafunc.parametrize("env", [end])
