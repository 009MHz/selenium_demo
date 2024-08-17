import logging
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class TestConfigBrowser:
    def __init__(self):
        self.ENVIRONMENT = os.getenv("env")
        self.EXECUTION_TYPE = os.getenv("execution_type")
        self.BROWSER = os.getenv("browsers")

    def show_browser(self, options):
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-extensions")
        options.add_argument('--disable-popup-blocking')
        options.add_argument("--disable-infobar")
        options.add_argument("--start-maximized")
        return options

    def hide_browser(self, options):
        options = self.show_browser(options)
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920x1080")
        options.add_argument("--no-sandbox")  # Added for running in Docker
        options.add_argument("--disable-dev-shm-usage")  # Added for running in Docker
        options.add_argument("--disable-software-rasterizer")
        options.add_argument("--disable-features=VizDisplayCompositor")
        return options

    def firefox_options(self):
        options = FirefoxOptions()
        return self.show_browser(options)

    def chrome_options(self):
        options = ChromeOptions()
        return self.show_browser(options)

    def edge_options(self):
        options = EdgeOptions()
        return self.show_browser(options)

    def chrome_headless(self):
        options = ChromeOptions()
        return self.hide_browser(options)

    def firefox_headless(self):
        options = FirefoxOptions()
        return self.hide_browser(options)

    def edge_headless(self):
        options = EdgeOptions()
        return self.hide_browser(options)

    def set_options(self):
        browser = self.BROWSER
        options = None

        option_mapping = {
            'firefox': self.firefox_options,
            'firefox-headless': self.firefox_headless,
            'chrome': self.chrome_options,
            'chrome-headless': self.chrome_headless,
            'edge-headless': self.edge_headless,
            'edge': self.edge_options,
        }

        if browser in option_mapping:
            options = option_mapping[browser]()
            logging.info(f"Setting capabilities for {browser}...")
        else:
            raise ValueError(f"Unsupported browser: {browser}")

        return options

    def set_command_executor(self):
        browser = self.BROWSER
        execution_type = self.EXECUTION_TYPE
        command_executor = None

        if execution_type == 'grid':
            command_executor = 'http://127.0.0.1:4444/wd/hub'
        elif execution_type == 'pipeline':
            if browser == 'chrome' or browser == 'chrome-headless':
                command_executor = 'http://selenium__standalone-chrome:4444/wd/hub'
            elif browser == 'firefox' or browser == 'firefox-headless':
                command_executor = 'http://selenium__standalone-firefox:4444/wd/hub'
            elif browser == 'edge' or browser == 'edge-headless':
                command_executor = 'http://selenium__standalone-edge:4444/wd/hub'

        logging.info(f"Getting command executor for {browser}...")
        logging.info(f"Tests will be run in {command_executor}")
        return command_executor

    def select_browser(self):
        browser = self.BROWSER
        execution_type = self.EXECUTION_TYPE
        driver = None

        if execution_type == 'local':
            if browser == 'firefox':
                driver = webdriver.Firefox(
                    service=FirefoxService(GeckoDriverManager().install()),
                    options=self.set_options())
            elif browser == 'firefox-headless':
                driver = webdriver.Firefox(
                    service=FirefoxService(GeckoDriverManager().install()),
                    options=self.set_options())
            elif browser == 'chrome':
                driver = webdriver.Chrome(
                    service=ChromeService(ChromeDriverManager().install()),
                    options=self.set_options())
            elif browser == 'chrome-headless':
                driver = webdriver.Chrome(
                    service=ChromeService(ChromeDriverManager().install()),
                    options=self.set_options())
            elif browser == 'edge':
                driver = webdriver.Edge(
                    service=EdgeService(EdgeChromiumDriverManager().install()),
                    options=self.set_options())
            elif browser == 'edge-headless':
                driver = webdriver.Edge(
                    service=EdgeService(EdgeChromiumDriverManager().install()),
                    options=self.set_options())
            else:
                raise ValueError(f'--browser="{browser}" is not defined in conftest.py file')

        elif execution_type == 'grid' or execution_type == 'pipeline':
            driver = webdriver.Remote(command_executor=self.set_command_executor(),
                                      options=self.set_options())

        logging.info(f"Setting {execution_type} driver with {browser}...")
        return driver
