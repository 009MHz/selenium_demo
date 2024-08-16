from pages.login_page import LoginPageFunction
import pytest
import allure


@pytest.fixture(scope='function')
def login(driver):
    login_page = LoginPageFunction(driver)
    login_page.open_page()
    with allure.step("1. Navigate the login page URL"):
        login_page.open_page()
    with allure.step("2. Validate the Login Page Component"):
        login_page.url_contain_keyword("login")
        login_page.page_title_match("Login Page")
        login_page.page_info_contains("log into the secure area")
        login_page.pass_input_availability()
        login_page.name_input_availability()
        login_page.name_field_label_match("Username")
        login_page.password_field_label_match("Password")
        login_page.login_button_availability()
    return login_page


@allure.epic("Login")
@allure.story("Login/ Success Login")
@allure.testcase("https://the-internet.herokuapp.com/login", "Positive Login")
@allure.tag("Login")
class TestSuccessLogin:
    @pytest.mark.ui
    @pytest.mark.positive
    @allure.title("Username input is not masked by dot")
    @allure.tag("masking", "username")
    @allure.id("TCP-LGI-01")
    def test_password_masking_TCP_LGI_01(self, login):
        with allure.step("3. Insert Any character in the username input field "):
            login.username_insert("T|-|!s I5 Sp#ci@l TeXt UserN@m3")

        with allure.step("4. Validate the masked character by check the input type"):
            login.name_input_unmasked()

    @pytest.mark.ui
    @pytest.mark.positive
    @allure.title("User password is masked by dot")
    @allure.tag("masking", "password")
    @allure.id("TCP-LGI-02")
    def test_password_masking_TCP_LGI_02(self, login):
        with allure.step("3. Insert Any character in the password input field "):
            login.password_insert("T|-|!s I5 Sp#ci@l TeXt P4sSw012D")

        with allure.step("4. Validate the masked character by check the input type"):
            login.password_input_masked()

    @pytest.mark.ui
    @pytest.mark.positive
    @allure.title("Successful Login with Correct Credentials")
    @allure.tag("password", "username", "success login")
    @allure.id("TCP-LGI-03")
    def test_success_login_TCP_LGI_03(self, login):
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


