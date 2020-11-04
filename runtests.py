from selenium import webdriver
from loginpage import *
from dashboardpage import *
from bankpage import *

driver = (
    webdriver.Chrome()
)  # declaring the driver as a Global variable for clarity purposes


def login():
    driver.get("http://login.xero.com")
    login_form = Login(driver)
    login_form.login()


def visit_bank_page():
    navigate = Dashboard(driver)
    navigate.go_to_bank_page()


def add_bank_to_organisation():
    add_bank = AddBankAccount(driver)
    add_bank.search_for_ANZ()
    add_bank.add_dummy_account()
    add_bank.check_if_account_is_added()
    add_bank.return_to_dashboard()


def select_another_organisation():
    select_second_organisation = Dashboard(driver)
    select_second_organisation.open_drop_down()
    select_second_organisation.confirm_selection()
    select_second_organisation.confirm_transition_complete()


if __name__ == "__main__":
    login()

    visit_bank_page()
    add_bank_to_organisation()
    time.sleep(10)  # added for demo purposes

    select_another_organisation()

    visit_bank_page()
    add_bank_to_organisation()
    time.sleep(10)  # added for demo purposes
    driver.quit()
