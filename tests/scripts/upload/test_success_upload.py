from pages.upload_page import Uploader
import pytest
import allure


@allure.epic("Uploader")
@allure.story("Upload/ Success Upload")
@allure.testcase("https://the-internet.herokuapp.com/upload", "TCP_FUP_01")
@allure.tag("Upload", "Files")
class TestSuccessUpload:
    @pytest.mark.ui
    @pytest.mark.positive
    @allure.title("Successful File Upload")
    @allure.id("TCP-FUP-01")
    def test_success_login_TCP_LGI_01(self, driver):
        pass
