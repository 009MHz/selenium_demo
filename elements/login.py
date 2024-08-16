from selenium.webdriver.common.by import By


class Url:
    login = "https://the-internet.herokuapp.com/login"
    post_success = "https://the-internet.herokuapp.com/secure"


class PageInfo:
    header = By.XPATH, "//div[@id='content']//h2"
    sub_header = By.CLASS_NAME, "subheader"
    toast = By.ID, "flash"
    header = By.TAG_NAME, "h2"
    sub_header = By.CLASS_NAME, "subheader"


class Interactor:
    email_label = By.CSS_SELECTOR, "label[for='username']"
    email_input = By.ID, "username"
    pass_label = By.CSS_SELECTOR, "label[for='password']"
    pass_input = By.ID, "password"
    login_btn = By.XPATH, "//button[@type='submit']"


class PostSuccess:
    logout_btn = By.CSS_SELECTOR, ".button.secondary.radius"
