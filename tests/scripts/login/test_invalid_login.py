from pages.login_page import LoginPageFunction
import pytest
import allure


@pytest.fixture(scope='function')
def login(driver):
    login_page = LoginPageFunction(driver)
    login_page.open_page()
    with allure.step("1. Navigate the login page URL"):
        login_page.open_page()
    return login_page


@allure.epic("Login")
@allure.story("Login/ Invalid Login")
@allure.testcase("https://the-internet.herokuapp.com/login", "Negative Login Tests")
@allure.tag("Login", "email", "password")
class TestFailedLogin:
    @pytest.mark.ui
    @pytest.mark.negative
    @allure.title("Unsuccessful Login with Invalid Username")
    @allure.id("TCP-NGI-01")
    def test_invalid_username_TCP_NGI_01(self, login):
        with allure.step("2. Validate the Login Page Components"):
            login.url_contain_keyword("login")
            login.page_title_match("Login Page")
            login.page_info_contains("log into the secure area")
            login.name_input_availability()
            login.pass_input_availability()
            login.name_field_label_match("Username")
            login.password_field_label_match("Password")
            login.login_button_availability()

        with allure.step("3. Insert Invalid Username"):
            login.username_insert("invalid_username")

        with allure.step("4. Insert Valid Password"):
            login.password_insert("SuperSecretPassword!")

        with allure.step("5. Click on the Login Button"):
            login.click_login_button()

        with allure.step("6. Validate the Invalid Username toast"):
            # Todo: Add Username fail toast validation
            pass

    @pytest.mark.ui
    @pytest.mark.negative
    @allure.title("Unsuccessful Login with Invalid Password")
    @allure.id("TCP-NGI-02")
    def test_invalid_password_TCP_NGI_02(self, login):
        with allure.step("2. Validate the Login Page Components"):
            login.url_contain_keyword("login")
            login.page_title_match("Login Page")
            login.page_info_contains("log into the secure area")
            login.name_input_availability()
            login.pass_input_availability()
            login.name_field_label_match("Username")
            login.password_field_label_match("Password")
            login.login_button_availability()

        with allure.step("3. Insert Valid Username"):
            login.username_insert("tomsmith")

        with allure.step("4. Insert Invalid Password"):
            login.password_insert("invalid_password")

        with allure.step("5. Click on the Login Button"):
            login.click_login_button()

        with allure.step("6. Validate the Invalid Username toast"):
            # Todo: Add Password fail toast validation
            pass

    @pytest.mark.ui
    @pytest.mark.negative
    @allure.title("Unsuccessful Login with Empty Field")
    @allure.id("TCP-NGI-03")
    def test_empty_credentials_TCP_NGI_03(self, login):
        with allure.step("2. Validate the Login Page Components"):
            login.url_contain_keyword("login")
            login.page_title_match("Login Page")
            login.page_info_contains("log into the secure area")
            login.name_input_availability()
            login.pass_input_availability()
            login.name_field_label_match("Username")
            login.password_field_label_match("Password")
            login.login_button_availability()

        with allure.step("3. Click on the Login Button without input the credentials"):
            login.click_login_button()

        with allure.step("4. Validate the Invalid Username toast"):
            # Todo: Add Empty field fail toast validation
            pass
