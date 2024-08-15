import json
import time as tm

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def _find(self, locator: tuple) -> WebElement:
        return self._driver.find_element(*locator)

    def _view(self, locator: tuple, time: int = 10):
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.visibility_of_element_located(locator))

    def _unseen(self, locator: tuple, time: int = 10):
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.invisibility_of_element_located(locator))

    def _type(self, locator: tuple, text: str, time: int = 10):
        self._view(locator, time)
        self._find(locator).send_keys(text)

    def _touch(self, locator: tuple, time: int = 15):
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.element_to_be_clickable(locator))

    def _click(self, locator: tuple):
        self._touch(locator)
        self._find(locator).click()

    def _collect(self, locator: str):
        return self._driver.find_elements(By.XPATH, locator)

    def _url_check(self, url: str, time: int = 15,):
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.url_to_be(url))

    def _save_session(self, file_name: str):
        cookies = self._driver.get_cookies()
        with open(file_name, 'w') as file:
            json.dump(cookies, file)

    def _load_session(self, file_name: str):
        with open(file_name, 'r') as file:
            cookies = json.load(file)

        for i in cookies:
            self._driver.add_cookie(i)

    def _retry(self,
               action: str,
               retry: int,
               interval: int,
               *args, **kwargs):
        """Retry action to hit flaky action
        example: self._retry("click", 3, 2, (By.XPATH, opt))"""

        attempts = 0
        while attempts < retry:
            try:
                action_method = getattr(self, f"_{action}")
                action_method(*args, **kwargs)
                break  # Exit the loop if action succeeds
            except Exception as e:
                attempts += 1
                print(f"Retry attempt {attempts} failed for {action}: {e}")
                tm.sleep(interval)  # Wait for a moment before retrying
        else:
            raise Exception(f"Failed to perform action {action} after {retry} attempts")