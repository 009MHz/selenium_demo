from pages.upload_page import Uploader
import pytest
import allure


@pytest.fixture(scope='function')
def uploader(driver):
    upload_page = Uploader(driver)
    upload_page.open_page()
    upload_page.pre_action_initiate()
    return upload_page


@allure.epic("Uploader")
@allure.story("Upload/ Select File")
@allure.testcase("https://the-internet.herokuapp.com/upload", "File Uploader Page")
@allure.tag("Upload", "Failed")
class TestFailUploadBySelect:
    @pytest.mark.ui
    @pytest.mark.negative
    @allure.title("No File Upload Error Validation")
    @allure.id("TCN-FUP-01")
    def test_upload_file_TCP_FUP_02(self, uploader):
        with allure.step("1. Click on the submit button without insert any files"):
            uploader.submit_upload()

        with allure.step("2. Verify the Error state"):
            uploader.url_contain_keyword('upload')
            uploader.err_page_title_match('Internal Server Error')
            uploader.err_page_file_preview_not_exist()