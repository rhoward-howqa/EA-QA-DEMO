
import time

from pages.login import LoginPage
from pages.request_loan import RequestLoanPage


def test_register_for_loan(browser):

    username = "Paul"
    password = "12345"
    loan_amount = "100"
    dp_amount = "50"
    message = "Congratulations, your loan has been approved."

    login_page = LoginPage(browser)
    request_loan_page = RequestLoanPage(browser)

    # given logged in user want to request a loan
    login_page.load()
    login_page.username(username)
    login_page.password(password)
    login_page.login_button()
    request_loan_page.register_for_loan_button()


    # when the user complete request loan form with acceptable values
    request_loan_page.loan_amount(loan_amount)
    request_loan_page.down_payment(dp_amount)

    request_loan_page.apply_button()

    # then te user is successfully registered

    actual_message = request_loan_page.success_message()
    print(actual_message)

    assert request_loan_page.success_message() == message

    time.sleep(5)
