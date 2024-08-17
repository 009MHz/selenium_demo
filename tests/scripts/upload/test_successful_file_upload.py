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
@allure.tag("Upload")
@pytest.mark.uploader
class TestSuccessUploadBySelect:
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
    @allure.title("Successful File Upload Validation")
    @allure.id("TCP-FUP-02")
    @allure.tag("Upload", "Success")
    @pytest.mark.parametrize("file_name", ['testFile.docx'])
    def test_upload_file_TCP_FUP_02(self, uploader, file_name):
        with allure.step("1. Insert the file name with the extension"):
            uploader.upload_file(file_name)

        with allure.step("2. Click on the submit button"):
            uploader.submit_upload()

        with allure.step("3. Verify the successful state"):
            uploader.url_contain_keyword('upload')
            uploader.success_title_page_match('File Uploaded!')
            uploader.file_name_availability(file_name)

    @pytest.mark.ui
    @pytest.mark.positive
    @allure.title("File Upload Documents Test")
    @allure.id("TCP-FUP-03")
    @allure.tag( "Success", "Doc Files")
    @pytest.mark.parametrize("file_name", ['testFile.docx', 'testFile.pdf'])
    def test_upload_file_docs_TCP_FUP_03(self, uploader, file_name):
        uploader.upload_file_runner(file_name)

    @pytest.mark.ui
    @pytest.mark.positive
    @allure.title("File Upload Images Test")
    @allure.id("TCP-FUP-04")
    @allure.tag("Success", "Image Files")
    @pytest.mark.parametrize("file_name", ['testFile.png', 'testFile.jpeg'])
    def test_upload_file_image_TCP_FUP_04(self, uploader, file_name):
        uploader.upload_file_runner(file_name)

    @pytest.mark.ui
    @pytest.mark.positive
    @allure.title("File Upload Data Test")
    @allure.id("TCP-FUP-05")
    @allure.tag("Success", "Data Files")
    @pytest.mark.parametrize("file_name", ['testFile.csv', 'testFile.xlsx'])
    def test_upload_file_spreadsheet_TCP_FUP_05(self, uploader, file_name):
        uploader.upload_file_runner(file_name)

    @pytest.mark.ui
    @pytest.mark.positive
    @allure.title("File Upload Video Test")
    @allure.id("TCP-FUP-06")
    @allure.tag("Success", "Video Files")
    @pytest.mark.parametrize("file_name", ['testFile.mp4', 'testFile.webm'])
    def test_upload_file_video_TCP_FUP_06(self, uploader, file_name):
        uploader.upload_file_runner(file_name)
