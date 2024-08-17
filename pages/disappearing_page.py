import allure
from selenium.webdriver.remote.webdriver import WebDriver
from pages.__base import Base
from elements.disappearing_locators import *


class Disappearance(Base):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    """Test Interaction"""
    def open_page(self):
        self._driver.get(Url.main)

    def click_add_element(self):
        self._click(Interactor.add)

    def click_delete_button(self):
        self._click(Interactor.delete)

    def add_multiple_elements(self, count: int):
        for _ in range(count):
            self.click_add_element()

    def delete_multiple_elements(self, count: int):
        for _ in range(count):
            self.click_delete_button()

    """Test Validation"""
    def url_contain_keyword(self, keyword):
        self._url_check(Url.main)
        assert keyword in self._driver.current_url, f"❌ URL does not contain '{keyword}'"

    def page_title_match(self, expected_title: str):
        self._view(PageInfo.title)
        text_header = self._find(PageInfo.title).text
        assert expected_title == text_header, f"❌ Page title does not match '{expected_title}'"

    def add_button_availability(self):
        self._view(Interactor.add)
        assert self._find(Interactor.add).is_enabled(), f"❌ The Add Element button is not interactable"
        assert "Add Element" == self._find(Interactor.add).text, f"❌ Add button text doesn't display as 'Add Element'"

    def del_button_unavailability(self):
        delete_btn = len(self._driver.find_elements(*Interactor.delete))
        assert delete_btn == 0, f"❌ The Delete button is detected on initial state"

    def del_button_existence(self):
        delete_btn = self._driver.find_elements(*Interactor.delete,)
        assert len(delete_btn) != 0, f"❌ The Delete button doesn't exist"

    def multiple_additions_check(self, expected_count: int):
        initial_count = len(self._driver.find_elements(*Interactor.delete))

        self.add_multiple_elements(expected_count)
        final_count = len(self._driver.find_elements(*Interactor.delete))
        assert final_count == initial_count + expected_count, f"❌ The added element doesn't match"

    def multiple_deletions_check(self, delete_count: int):
        initial_count = len(self._driver.find_elements(*Interactor.delete))

        self.delete_multiple_elements(delete_count)
        final_count = len(self._driver.find_elements(*Interactor.delete))
        assert final_count == initial_count - delete_count, f"❌ The deleted element doesn't match"

    """Repeatable Custom Action"""
    def pre_action_initiate(self):
        with allure.step("▸ Navigate to the Add/Remove Elements Page"):
            self.open_page()
        with allure.step("▸ Validate Page Components"):
            self.url_contain_keyword("add_remove_elements")
            self.page_title_match("Add/Remove Elements")
            self.add_button_availability()
