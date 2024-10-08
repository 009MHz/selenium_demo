import allure
from selenium.webdriver.remote.webdriver import WebDriver
from pages.__base import Base
from elements.login_locators import *


class LoginPageFunction(Base):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    """Login Interaction"""
    def open_page(self):
        self._driver.get(Url.login)

    def username_insert(self, name: str):
        self._type(Interactor.username_input, name)

    def password_insert(self, password: str):
        self._type(Interactor.password_input, password)

    def click_login_button(self):
        self._click(Interactor.login_btn)

    """Login Validation"""
    def url_contain_keyword(self, keyword):
        self._url_check(Url.login)
        assert keyword in self._driver.current_url, f"❌ URL does not contain '{keyword}'"

    def page_title_match(self, expected_title: str):
        self._view(PageInfo.header)
        text_header = self._find(PageInfo.header).text
        assert expected_title == text_header, f"❌ Page title does not match '{expected_title}'"

    def page_info_contains(self, keyword):
        self._view(PageInfo.sub_header)
        text_info = self._find(PageInfo.sub_header).text
        assert keyword in text_info, f"❌ Page info does not contain '{keyword}'"

    def name_field_label_match(self, expected_label: str):
        self._view(Interactor.username_label)
        label_name = self._find(Interactor.username_label).text
        assert expected_label == label_name, f"❌ Name label does not match '{expected_label}'"

    def name_input_availability(self):
        self._touch(Interactor.username_input)
        assert self._find(Interactor.username_input).is_enabled(), "❌ Username input field is not enabled"

    def name_input_unmasked(self):
        self._touch(Interactor.username_input)
        assert self._find(Interactor.username_input).get_attribute("type") == "text", "❌ Username field is masked"

    def password_field_label_match(self, expected_label: str):
        self._view(Interactor.password_label)
        label_name = self._find(Interactor.password_label).text
        assert expected_label == label_name, f"❌ Password label does not match '{expected_label}'"

    def pass_input_availability(self):
        self._touch(Interactor.password_input)
        assert self._find(Interactor.password_input).is_enabled(), "❌ Password input field is not enabled"

    def password_input_masked(self):
        self._touch(Interactor.password_input)
        assert self._find(Interactor.password_input).get_attribute("type") == "password", "❌ User Password is unmasked"

    def login_button_availability(self):
        self._view(Interactor.login_btn)
        assert self._find(Interactor.login_btn).is_enabled(), "❌ Login button is not enabled"

    def url_post_success_contain(self, keyword):
        self._url_check(Url.post_success)
        assert keyword in self._driver.current_url, f"❌ URL does not contain '{keyword}' after login"

    def success_toast_message_contains(self, keyword):
        self._view(PageInfo.toast)
        toast_message = self._find(PageInfo.toast).text
        assert self._find(PageInfo.toast).is_displayed(), "❌ Success toast is not displayed"
        assert keyword in toast_message, f"❌ Success toast message does not contain '{keyword}'"

    def success_page_title_availability(self):
        self._view(PageInfo.header)
        header_element = self._find(PageInfo.header)
        assert header_element.is_displayed(), "❌ Success page title is not displayed"
        assert header_element.text == "Secure Area", "❌ Success page title does not match 'Secure Area'"

    def success_page_info_availability(self):
        self._view(PageInfo.sub_header)
        info_page = self._find(PageInfo.sub_header)
        assert info_page.is_displayed(), "❌ Success login sub header is not displayed"
        assert "When you are done" in info_page.text, "❌ Success login sub header does not contain the correct text"

    def logout_button_availability(self):
        self._touch(PostSuccess.logout_btn)
        logout = self._find(PostSuccess.logout_btn)
        assert logout.is_enabled(), "❌ The Logout button is not accessible"
        assert "Logout" == logout.text, "❌ The Logout button is not contains the correct text"

    def fail_toast_message_contains(self, keyword):
        self._view(PageInfo.toast)
        toast_message = self._find(PageInfo.toast).text
        assert self._find(PageInfo.toast).is_displayed(), "❌ Username fail toast message is not displayed"
        assert keyword in toast_message, f"❌ Fail toast message does not match with '{keyword}'"

    """Repeatable Custom Action"""
    def pre_action_initiate(self):
        with allure.step("▸ Navigate the login page URL"):
            self.open_page()
        with allure.step("▸ Validate the Login Page Component"):
            self.url_contain_keyword("login")
            self.page_title_match("Login Page")
            self.page_info_contains("log into the secure area")
            self.pass_input_availability()
            self.name_input_availability()
            self.name_field_label_match("Username")
            self.password_field_label_match("Password")
            self.login_button_availability()
