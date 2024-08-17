import pytest
from browser_config import BrowserManager


def pytest_addoption(parser):
    parser.addoption(
        "--browsers",
        action="store",
        default="chrome",
        help="Comma-separated list of browsers to run tests on: chrome, firefox, edge, safari")

    parser.addoption(
        "--headless",
        action="store_true",
        help="Run tests in headless mode")


@pytest.fixture(scope="session", params=None)
def driver(request):
    browser = request.param.lower()
    headless = request.config.getoption("--headless")

    browser_manager = BrowserManager(browser, headless)
    driver_instance = browser_manager.create_webdriver()

    yield driver_instance
    driver_instance.quit()


def pytest_generate_tests(metafunc):
    # Get the list of browsers specified in the command line options
    browsers = metafunc.config.getoption('browsers').split(',')
    # Generate a separate test for each browser
    if 'driver' in metafunc.fixturenames:
        metafunc.parametrize('driver', browsers, scope='session', indirect=True)


@pytest.fixture(autouse=True)
def _browser_per_test(request, driver):
    if request.cls is not None:
        request.cls.driver = driver
