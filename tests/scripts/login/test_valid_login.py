from pages.login_page import LoginPageFunction
import pytest
import allure


@pytest.fixture(scope='function')
def login(driver):
    login_page = LoginPageFunction(driver)
    login_page.open_page()
    login_page.pre_action_initiate()
    return login_page


@allure.epic("Login")
@allure.story("Login/ Success Login")
@allure.testcase("https://the-internet.herokuapp.com/login", "Positive Login")
@allure.tag("Login", "Valid")
class TestSuccessLogin:
    @pytest.mark.ui
    @pytest.mark.positive
    @allure.title("User password is masked by dot")
    @allure.tag("Masking", "Password")
    @allure.id("TCP-LGI-01")
    def test_username_unmasked_TCP_LGI_01(self, login):
        with allure.step("3. Insert Any character in the password input field "):
            login.password_insert("T|-|!s I5 Sp#ci@l TeXt P4sSw012D")

        with allure.step("4. Validate the masked character by check the input type"):
            login.password_input_masked()

    @pytest.mark.ui
    @pytest.mark.positive
    @allure.title("Username input is not masked by dot")
    @allure.tag("Masking", "Username")
    @allure.id("TCP-LGI-02")
    def test_password_masking_TCP_LGI_02(self, login):
        with allure.step("3. Insert Any character in the username input field "):
            login.username_insert("T|-|!s I5 Sp#ci@l TeXt UserN@m3")

        with allure.step("4. Validate the masked character by check the input type"):
            login.name_input_unmasked()

    @pytest.mark.ui
    @pytest.mark.positive
    @allure.title("Successful Login with Correct Credentials")
    @allure.tag("Success login")
    @allure.id("TCP-LGI-03")
    def test_success_login_TCP_LGI_03(self, login):
        with allure.step("3. Insert Valid username on the respective field"):
            login.username_insert("tomsmith")

        with allure.step("4. Insert Valid password on the respective field"):
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


