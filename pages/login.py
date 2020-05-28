from selenium.webdriver.common.by import By


class LoginPage:

    URL = "https://parabank.parasoft.com/"

    # locators
    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//div[@id='bodyPanel']//div[3]//input[1]")

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def username(self, username):
        username_input = self.browser.find_element(*self.USERNAME_INPUT)
        username_input.send_keys(username)

    def password(self, password):
        password_input = self.browser.find_element(*self.PASSWORD_INPUT)
        password_input.send_keys(password)


    def login_button(self):
        login_button = self.browser.find_element(*self.LOGIN_BUTTON)
        login_button.click()

