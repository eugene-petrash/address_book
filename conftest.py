from fixture.application import Application
import pytest
import json
import os.path

fixture = None
target = None


@pytest.fixture
def app(request):
    global fixture
    global target
    custom_browser = request.config.getoption("--browser")
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))
        with open(config_file) as f:
            target = json.load(f)
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=custom_browser, base_url=target["base_url"])
        fixture.session.login(username=target["user_name"], password=target["password"])
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")