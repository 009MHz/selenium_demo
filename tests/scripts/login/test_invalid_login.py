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
@allure.story("Login/ Invalid Login")
@allure.testcase("https://the-internet.herokuapp.com/login", "Negative Login Tests")
@allure.tag("Login", "Invalid")
class TestFailedLogin:
    @pytest.mark.ui
    @pytest.mark.negative
    @allure.title("Unsuccessful Login with Invalid Username")
    @allure.tag("Username")
    @allure.id("TCP-NGI-01")
    def test_invalid_username_TCP_NGI_01(self, login):
        with allure.step("1. Insert Invalid Username"):
            login.username_insert("invalid_username")

        with allure.step("2. Insert Valid Password"):
            login.password_insert("SuperSecretPassword!")

        with allure.step("3. Click on the Login Button"):
            login.click_login_button()

        with allure.step("4. Validate the Invalid Username State"):
            login.url_contain_keyword('/login')
            login.fail_toast_message_contains('username is invalid!')

    @pytest.mark.ui
    @pytest.mark.negative
    @allure.title("Unsuccessful Login with Invalid Password")
    @allure.tag("Password")
    @allure.id("TCP-NGI-02")
    def test_invalid_password_TCP_NGI_02(self, login):
        with allure.step("1.Insert Valid Username"):
            login.username_insert("tomsmith")

        with allure.step("2. Insert Invalid Password"):
            login.password_insert("invalid_password")

        with allure.step("3. Click on the Login Button"):
            login.click_login_button()

        with allure.step("4. Validate the Invalid Username toast"):
            login.url_contain_keyword('/login')
            login.fail_toast_message_contains('password is invalid!')

    @pytest.mark.ui
    @pytest.mark.negative
    @allure.title("Unsuccessful Login with Invalid Credentials")
    @allure.tag("Password")
    @allure.id("TCP-NGI-03")
    def test_invalid_credential_TCP_NGI_03(self, login):
        with allure.step("1.Insert Invalid Password"):
            login.password_insert("invalid_username")

        with allure.step("2.Insert Invalid Password"):
            login.password_insert("invalid_password")

        with allure.step("3.Click on the Login Button"):
            login.click_login_button()

        with allure.step("4.Validate the Invalid toast"):
            login.url_contain_keyword('/login')
            login.fail_toast_message_contains('username is invalid!')

    @pytest.mark.ui
    @pytest.mark.negative
    @allure.title("Unsuccessful Login with Empty Field")
    @allure.tag("Username", "Password")
    @allure.id("TCP-NGI-04")
    def test_empty_credentials_TCP_NGI_03(self, login):
        with allure.step("1. Click on the Login Button without input the credentials"):
            login.click_login_button()

        with allure.step("2. Validate the Invalid Username toast"):
            login.url_contain_keyword('/login')
            login.fail_toast_message_contains('username is invalid!')
