from selenium.webdriver.remote.webdriver import WebDriver
from pages.__base import Base
from elements.uploader_locators import *


class Uploader(Base):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    # Todo 1: Define uploader interaction

    # Todo 2: Define uploader action validation
