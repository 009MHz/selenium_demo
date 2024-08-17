import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
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


def get_browser_options(browser_name, headless):
    """Configure and return the appropriate WebDriver options based on the browser name and mode."""
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
    elif browser_name == "firefox":
        options = webdriver.FirefoxOptions()
    elif browser_name == "edge":
        options = webdriver.EdgeOptions()
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    options.add_argument("--disable-notifications")
    options.add_argument("--disable-extensions")
    options.add_argument('--disable-popup-blocking')
    options.add_argument("--disable-infobar")

    if headless:
        if browser_name == "firefox":
            options.add_argument("--headless")
        else:  # Chrome and Edge
            options.add_argument("--headless=new")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920x1080")
    else:
        options.add_argument("--start-maximized")

    return options


def create_webdriver(browser_name, headless):
    """Create and return a WebDriver instance based on the browser name."""
    options = get_browser_options(browser_name, headless)

    if browser_name == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    elif browser_name == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(), options=options)
    elif browser_name == "edge":
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)
    elif browser_name == "safari":
        if headless:
            raise ValueError("Safari does not support headless mode")
        driver = SafariDriver()
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    # Maximize the window for Firefox if not in headless mode
    if browser_name == "firefox" and not headless:
        driver.maximize_window()

    return driver


@pytest.fixture(scope="session", params=None)
def driver(request):
    browser = request.param.lower()
    headless = request.config.getoption("--headless")
    driver_instance = create_webdriver(browser, headless)
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


# def pytest_report_header(config):
#     return f"Running tests on {config.getoption('--browsers')} browser(s)"
