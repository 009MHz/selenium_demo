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
@allure.story("Upload")
@allure.testcase("https://the-internet.herokuapp.com/upload", "File Uploader Page")
@allure.tag("Upload")
class TestSuccessUpload:
    @pytest.mark.ui
    @pytest.mark.positive
    @allure.title("File Uploader Page contains the correct components")
    @allure.id("TCP-FUP-01")
    @allure.tag("Initial Check")
    def test_uploader_page_components_TCP_FUP_01(self, driver):
        init = Uploader(driver)
        with allure.step("1. Navigate to the File Upload Page"):
            init.open_page()
        with allure.step("2. Validate the URL redirection"):
            init.url_contain_keyword('upload')

        with allure.step("2. Validate the Page Info"):
            init.page_title_match('File Uploader')
            init.page_info_contains('Choose a file')
            init.page_info_contains('Or, drag and drop a file')

        with allure.step("3. Validate the File Uploader components"):
            init.select_file_availability()
            init.submit_file_availability()
            init.dragging_box_availability()

    @pytest.mark.ui
    @pytest.mark.positive
    @allure.title("")
    @allure.id("TCP-FUP-02")
    @allure.tag("")
    def test_upload_file_TCP_FUP_02(self, uploader):
        with allure.step("1. Insert the file name with the extension"):
            uploader.upload_file('testFile.docx')

        with allure.step("2. Click on the submit button"):
            uploader.submit_upload()

        with allure.step("3. Verify the successful state"):
            uploader.success_title_page_availability()
            uploader.file_name_availability()

