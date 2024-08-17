from selenium.webdriver.common.by import By


class Url:
    main = "https://the-internet.herokuapp.com/add_remove_elements/"


class PageInfo:
    title = By.CSS_SELECTOR, "div[id='content'] h3"
    wrapper = By.ID, "elements"


class Interactor:
    add = By.XPATH, "//button[normalize-space()='Add Element']"
    delete = By.CSS_SELECTOR, "div[id='elements'] .added-manually"

