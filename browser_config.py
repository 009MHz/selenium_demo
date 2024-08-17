from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.safari.webdriver import WebDriver as SafariDriver


class BrowserManager:
    def __init__(self, browser_name, headless):
        self.browser_name = browser_name.lower()
        self.headless = headless

    def get_browser_options(self):
        """Configure and return the appropriate WebDriver options based on the browser name and mode."""
        if self.browser_name == "chrome":
            options = webdriver.ChromeOptions()
        elif self.browser_name == "firefox":
            options = webdriver.FirefoxOptions()
        elif self.browser_name == "edge":
            options = webdriver.EdgeOptions()
        else:
            raise ValueError(f"Unsupported browser: {self.browser_name}")

        options.add_argument("--disable-notifications")
        options.add_argument("--disable-extensions")
        options.add_argument('--disable-popup-blocking')
        options.add_argument("--disable-infobar")

        if self.headless:
            if self.browser_name == "firefox":
                options.add_argument("--headless")
            else:
                options.add_argument("--headless=new")
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1920x1080")
        else:
            options.add_argument("--start-maximized")

        return options

    def create_webdriver(self):
        """Create and return a WebDriver instance based on the browser name."""
        options = self.get_browser_options()

        if self.browser_name == "chrome":
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        elif self.browser_name == "firefox":
            driver = webdriver.Firefox(service=FirefoxService(), options=options)
        elif self.browser_name == "edge":
            driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)
        elif self.browser_name == "safari":
            if self.headless:
                raise ValueError("Safari does not support headless mode")
            driver = SafariDriver()
        else:
            raise ValueError(f"Unsupported browser: {self.browser_name}")

        # Maximize the window for Firefox if not in headless mode
        if self.browser_name == "firefox" and not self.headless:
            driver.maximize_window()

        return driver
