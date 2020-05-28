from selenium.webdriver.common.by import By


class RequestLoanPage:

    # locators

    REGISTER_FOR_LOAN_BUTTON = (By.XPATH, "//div[@id='mainPanel']//li[7]//a[1]")
    LOAN_AMOUNT_INPUT = (By.CSS_SELECTOR, "#amount")
    DOWN_PAYMENT_INPUT = (By.CSS_SELECTOR, "#downPayment")
    APPLY_BUTTON = (By.XPATH, "//input[@class='button']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[@id='rightPanel']//p[1]")

    def __init__(self, browser):
        self.browser = browser

    def register_for_loan_button(self):
        register_for_loan_button = self.browser.find_element(*self.REGISTER_FOR_LOAN_BUTTON)
        register_for_loan_button.click()

    def loan_amount(self, loan_amount):
        loan_amount_input = self.browser.find_element(*self.LOAN_AMOUNT_INPUT)
        loan_amount_input.send_keys(loan_amount)

    def down_payment(self, dp_amt):
        down_payment_input = self.browser.find_element(*self.DOWN_PAYMENT_INPUT)
        down_payment_input.send_keys(dp_amt)

    def apply_button(self):
        apply_button = self.browser.find_element(*self.APPLY_BUTTON)
        apply_button.click()

    def success_message(self):
        success_message = self.browser.find_element(*self.SUCCESS_MESSAGE)
        value = success_message.text

        return value




