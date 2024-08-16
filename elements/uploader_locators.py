from selenium.webdriver.common.by import By


class Url:
    upload = "https://the-internet.herokuapp.com/upload"


class PageInfo:
    title = By.CSS_SELECTOR, "div[class='example'] h3"
    description = By.CSS_SELECTOR, "div[class='example'] p"
    uploaded_file_name = By.ID, "uploaded-files"


class FileUploader:
    select = By.ID, "file-upload"
    drag = By.ID, "drag-drop-upload"
    dragged_preview = By.CLASS_NAME, "dz-filename"
    dragged_mark = By.CSS_SELECTOR, "div[class='dz-success-mark'] span"
    submit = By.ID, "file-submit"

