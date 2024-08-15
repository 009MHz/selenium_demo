from pages.login_page import LoginPageFunction
import pytest
import allure


@allure.epic("Login")
@allure.story("Login/ Success Login")
@allure.testcase("https://the-internet.herokuapp.com/login", "TCP_LGI_01")
@allure.tag("Login", "email", "password")
class TestSuccessLogin:
    @pytest.mark.ui
    @pytest.mark.positive
    @allure.title("Successful Login with Correct Credentials")
    @allure.id("TCP-LGI-01")
    def test_TCP_LGI_01(self, driver):
        login = LoginPageFunction(driver)
        with allure.step("1. Navigate the login page URL"):
            login.open_page()

        with allure.step("2. Validate the Login Page Component"):
            login.url_contain_keyword("login")
            login.page_title_match("Login Page")
            login.page_info_contains("log into the secure area")
            login.pass_input_availability()
            login.name_input_availability()
            login.name_field_label_match("Username")
            login.password_field_label_match("Password")
            login.login_button_availability()

        with allure.step("3. Insert Valid username on the respective field "):
            login.username_insert("tomsmith")

        with allure.step("4. Insert Valid password on the respective field "):
            login.password_insert("SuperSecretPassword!")

        with allure.step("5. Click on the Login Button"):
            login.click_login_button()

        with allure.step("6. Validate the Success Login Redirection"):
            login.url_post_success_contain("/secure")

        with allure.step("7. Validate the Success Login Page"):
            login.url_post_success_contain("/secure")
            login.success_toast_message_contains("You logged into")
            login.success_page_title_availability()
            login.success_page_info_availability()
            login.logout_button_availability()
