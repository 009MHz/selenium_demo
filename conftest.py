import os
import pytest
from browser_config import TestConfigBrowser


def pytest_addoption(parser):
    """ pytest --option variables from shell
    --browser:
        chrome= Run tests with Chrome driver.
        firefox= Run tests with Firefox driver.
        chrome-headless = Run tests with Chrome driver, headless mode.
    --env:
        dev: Run tests in dev environment (with dev data)
        test: Run tests in test environment (with test data)
        stage: Run tests in stage environment (with stage data)
    --execution_type:
        local: Run tests in your local machine.
        grid: Run tests in docker with selenium grid hub (local grid - using the docker-compose.yml)
        pipeline: Run tests in Gitlab CI.
    """
    parser.addoption('--env', action='store', default='test', help='')
    parser.addoption('--browser', help='', default='chrome')
    parser.addoption('--execution_type', help='', default='local')


def pytest_configure(config):
    os.environ["env"] = config.getoption('env')
    os.environ["browser"] = config.getoption('browser')
    os.environ["execution_type"] = config.getoption('execution_type') or 'local'


@pytest.fixture()
def driver():
    browser = os.getenv("browser")
    execution_type = os.getenv("execution_type")

    if execution_type == 'grid' or execution_type == 'pipeline':
        mode = TestConfigBrowser().select_browser()
    elif execution_type == 'local':
        mode = TestConfigBrowser().select_browser()
    else:
        raise ValueError(f"Unsupported execution type: {execution_type}")

    mode.implicitly_wait(15)
    mode.maximize_window()
    yield mode
    mode.quit()
