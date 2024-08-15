from pages.login_page import LoginPageFunction
import pytest
import allure


@allure.epic("Login")
@allure.story("Login/ Success Login")
@allure.testcase("https://the-internet.herokuapp.com/login", "TCP-NGI-01")
@allure.tag("Login", "email", "password")
class TestSuccessLogin:
    @pytest.mark.ui
    @pytest.mark.negative
    @allure.title("Unsuccessful Login with invalid Credentials")
    @allure.id("TCP-NGI-01")
    def test_TCP_NGI_01(self, driver):
        login = LoginPageFunction(driver)
        with allure.step("1. Navigate the login page URL"):
            login.open_page()

