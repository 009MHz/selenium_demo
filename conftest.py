import pytest
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.safari.webdriver import WebDriver as SafariDriver

def pytest_addoption(parser):
    parser.addoption(
        "--browsers", action="store", default="chrome", help="Comma-separated list of browsers to run tests on: chrome, firefox, edge, safari"
    )
    parser.addoption(
        "--headless", action="store_true", help="Run tests in headless mode"
    )

@pytest.fixture(scope="session", params=None)
def driver(request):
    browser = request.param.lower()
    headless = request.config.getoption("--headless")

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-extensions")
        options.add_argument('--disable-popup-blocking')
        options.add_argument("--disable-infobar")
        options.add_argument("--start-maximized")
        if headless:
            options.add_argument("--headless=new")
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1920x1080")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-extensions")
        options.add_argument('--disable-popup-blocking')
        options.add_argument("--disable-infobar")
        options.add_argument("--start-maximized")
        if headless:
            options.add_argument("--headless=new")
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1920x1080")
        driver = webdriver.Firefox(service=FirefoxService(), options=options)

    elif browser == "edge":
        options = webdriver.EdgeOptions()
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-extensions")
        options.add_argument('--disable-popup-blocking')
        options.add_argument("--disable-infobar")
        options.add_argument("--start-maximized")
        if headless:
            options.add_argument("--headless=new")
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1920x1080")
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)

    elif browser == "safari":
        if headless:
            raise ValueError("Safari does not support headless mode")
        driver = SafariDriver()

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    yield driver
    driver.quit()

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

def pytest_report_header(config):
    return f"Running tests on {config.getoption('--browsers')} browser(s)"
