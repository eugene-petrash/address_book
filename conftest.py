from fixture.application import Application
import pytest

fixture = None


@pytest.fixture
def app(request):
    global fixture
    custom_browser = request.config.getoption("--browser")
    base_url = request.config.getoption("--base_url")
    if fixture is None:
        fixture = Application(browser=custom_browser, base_url=base_url)
        fixture.session.login(username="admin", password="secret")
    else:
        if not fixture.is_valid():
            fixture = Application(browser=custom_browser, base_url=base_url)
            fixture.session.login(username="admin", password="secret")
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
    parser.addoption("--base_url", action="store", default="http://localhost/addressbook/index.php")