import logging
import os
from selenium import webdriver
import chromedriver_autoinstaller


class TestConfigBrowser:
    def __init__(self):
        self.ENVIRONMENT = os.getenv("env")
        self.EXECUTION_TYPE = os.getenv("execution_type")
        self.BROWSER = os.getenv("browser")
        chromedriver_autoinstaller.install()

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
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--no-sandbox")  # Added for running in Docker
        options.add_argument("--disable-dev-shm-usage")  # Added for running in Docker
        options.add_argument("--remote-debugging-port=9222")  # Added for running in Docker
        return options

    def firefox_options(self):
        return self.show_browser(webdriver.FirefoxOptions())

    def chrome_options(self):
        return self.show_browser(webdriver.ChromeOptions())

    def edge_options(self):
        return self.show_browser(webdriver.EdgeOptions())

    def chrome_headless(self):
        return self.hide_browser(webdriver.ChromeOptions())

    def firefox_headless(self):
        return self.hide_browser(webdriver.FirefoxOptions())

    def edge_headless(self):
        return self.hide_browser(webdriver.EdgeOptions())

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
                driver = webdriver.Firefox()
            elif browser == 'firefox-headless':
                driver = webdriver.Firefox(options=self.set_options())
            elif browser == 'chrome':
                driver = webdriver.Chrome(options=self.set_options())
            elif browser == 'chrome-headless':
                driver = webdriver.Chrome(options=self.set_options())
            elif browser == 'edge':
                driver = webdriver.Edge(options=self.set_options())
            elif browser == 'edge-headless':
                driver = webdriver.Edge(options=self.set_options())
            else:
                raise ValueError(f'--browser="{browser}" is not defined in conftest.py file')
        elif execution_type == 'grid':
            driver = webdriver.Remote(command_executor=self.set_command_executor(),
                                      options=self.set_options())
        elif execution_type == 'pipeline':
            driver = webdriver.Remote(command_executor=self.set_command_executor(),
                                      options=self.set_options())
        logging.info(f"Setting {execution_type} driver with {browser}...")
        return driver
