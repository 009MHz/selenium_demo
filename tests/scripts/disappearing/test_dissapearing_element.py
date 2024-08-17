from pages.disappearing_page import Disappearance
import pytest
import allure


@pytest.fixture(scope='function')
def diss(driver):
    miss_el = Disappearance(driver)
    miss_el.pre_action_initiate()
    return miss_el


@allure.epic("Disappearing")
@allure.story("Disappearing/ Action")
@allure.testcase("https://the-internet.herokuapp.com/add_remove_elements/", "Element Disappearance")
@allure.tag("Disappearance")
@pytest.mark.disappearance
class TestDismissedElement:
    @pytest.mark.ui
    @pytest.mark.positive
    @allure.title("Dismissed Initial Page Validation")
    @allure.tag("Initial")
    @allure.id("TCP-MEP-01")
    def test_initial_element_state_TCP_MEP_01(self, driver):
        init = Disappearance(driver)
        with allure.step("1. Navigate the Dismissed page"):
            init.open_page()

        with allure.step("1.Verify that the current page url contains 'add_remove' "):
            init.url_contain_keyword("add_remove_elements")

        with allure.step("2. Verify that the Element state on the current page"):
            init.page_title_match("Add/Remove Elements")
            init.add_button_availability()
            init.del_button_unavailability()

    @pytest.mark.ui
    @pytest.mark.positive
    @allure.title("Validate the additional element after click on the Add button")
    @allure.tag("Add")
    @allure.id("TCP-MEP-02")
    def test_adding_delete_element_TCP_MEP_02(self, diss):
        with allure.step("1. Click on the Add button"):
            diss.click_add_element()

        with allure.step("2. Verify that the Delete element existence"):
            diss.del_button_existence()

    @pytest.mark.ui
    @pytest.mark.positive
    @allure.title("Validate the additional element after click on the Add button")
    @allure.tag("Delete")
    @allure.id("TCP-MEP-03")
    def test_deleting_added_element_TCP_MEP_03(self, diss):
        with allure.step("1. Click on the Add button"):
            diss.click_add_element()

        with allure.step("2. Verify that the Delete element existence"):
            diss.del_button_existence()

        with allure.step("3. Click on the delete button"):
            diss.click_delete_button()

        with allure.step("4. Verify that the Delete element removal"):
            diss.del_button_unavailability()

    @pytest.mark.ui
    @pytest.mark.positive
    @allure.title("Validate multiple interactions element")
    @allure.tag("Add", "Delete")
    @allure.id("TCP-MEP-04")
    def test_multiple_action_TCP_MEP_04(self, diss):
        with allure.step("1. Click on the Add button several times"):
            diss.multiple_additions_check(5)

        with allure.step("2. Click on the Delete button several times"):
            diss.multiple_deletions_check(3)
