import allure
import os
from selenium.common import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from pages.__base import Base
from elements.uploader_locators import *


class Uploader(Base):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    """Page Interaction"""
    def open_page(self):
        self._driver.get(Url.upload)

    def upload_file(self, file_name: str):
        initial_path = os.path.abspath(os.path.join("..", "data", "attachment", file_name))
        if not os.path.exists(initial_path):
            raise FileNotFoundError(f"File not found: {initial_path}")

        self._find(FileUploader.select).send_keys(initial_path)

    def submit_upload(self):
        self._click(FileUploader.submit)

    """Page Validation"""
    def url_contain_keyword(self, keyword):
        self._url_check(Url.upload)
        self._url_check(Url.upload)
        assert keyword in self._driver.current_url, f"❌ URL does not contain '{keyword}'"

    def page_title_match(self, expected_title: str):
        self._view(PageInfo.title)
        text_header = self._find(PageInfo.title).text
        assert expected_title == text_header, f"❌ Page title does not match '{expected_title}'"

    def page_info_contains(self, keyword):
        self._view(PageInfo.description)
        text_info = self._find(PageInfo.description).text
        assert keyword in text_info, f"❌ Page info does not contain '{keyword}'"

    def select_file_availability(self):
        self._view(FileUploader.select)
        assert self._find(FileUploader.select).is_enabled(), "❌ 'Choose File' button is not accessible"

    def submit_file_availability(self):
        self._view(FileUploader.submit)
        assert self._find(FileUploader.submit).is_enabled(), "❌ 'Upload' button is not accessible"

    def dragging_box_availability(self):
        self._view(FileUploader.drag)
        assert self._find(FileUploader.drag).is_enabled(), "❌ Dragging box is not accessible"

        file_preview = self._find(FileUploader.dragged_preview)
        assert not file_preview.is_displayed(), "❌ The File Name preview should not be exist"

        file_marker = self._find(FileUploader.dragged_mark)
        assert not file_marker.is_displayed(), "❌ The File Name marker should not be exist"

    def success_title_page_match(self, page_title: str):
        self._view(PageInfo.title)
        text_header = self._find(PageInfo.title).text
        assert page_title == text_header, f"❌ Page title does not match 'File Uploaded'"

    def file_name_availability(self, file_name: str):
        self._view(PageInfo.title)
        actual_name = self._find(PageInfo.uploaded_file_name).text
        assert file_name == actual_name, f"❌ Page title does not match 'File Uploaded'"

    def err_page_title_match(self, keyword: str):
        self._view(PageInfo.err_page)
        err_title = self._find(PageInfo.err_page).text
        assert keyword == err_title, f"❌ Page title does not match 'Internal Server Error'"

    def err_page_file_preview_not_exist(self):
        self._view(PageInfo.err_page)
        try:
            file_preview = self._find(PageInfo.uploaded_file_name)
            assert not file_preview.is_displayed(), "❌ File preview detected on the error page"
        except NoSuchElementException:
            pass

    """Repeatable Custom Action"""
    def pre_action_initiate(self):
        with allure.step("▸ Navigate to the File Upload Page"):
            self.open_page()
        with allure.step("▸ Validate File Upload Page Components"):
            self.url_contain_keyword('upload')
            self.select_file_availability()
            self.submit_file_availability()
            self.dragging_box_availability()
            
    def upload_file_runner(self, file_name):
        with allure.step("1. Insert the file name with the extension"):
            self.upload_file(file_name)

        with allure.step("2. Click on the submit button"):
            self.submit_upload()

        with allure.step("3. Verify the successful state"):
            self.url_contain_keyword('upload')
            self.success_title_page_match('File Uploaded!')
            self.file_name_availability(file_name)
