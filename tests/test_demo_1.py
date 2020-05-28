import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
import pytest


# set the driver instance
driver = webdriver.Chrome()

# browse to the endpoint
driver.get("https://parabank.parasoft.com/")


# set the implicit wait time
driver.implicitly_wait(10)

# maximise the window
driver.maximize_window()

# Arrange
# Login to application
driver.find_element_by_name("username").send_keys("Paul")
driver.find_element_by_name("password").send_keys("12345")
driver.find_element_by_xpath("//div[@id='bodyPanel']//div[3]//input[1]").click()


# Action
# Request Loan
driver.find_element_by_xpath("//div[@id='mainPanel']//li[7]//a[1]").click()
driver.find_element_by_css_selector("#amount").send_keys("100")
driver.find_element_by_css_selector("#downPayment").send_keys("50")
driver.find_element_by_xpath("//input[@class='button']").click()

# assert
# confirm loan request was successful
expected_message = "Congratulations, your loan has been approved."

# expected_message = "hello."


actual_message = driver.find_element_by_xpath("//div[@id='rightPanel']//p[1]").text
print(actual_message)

assert actual_message == expected_message

driver.quit()


