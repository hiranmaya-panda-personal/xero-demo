from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class AddBankAccount:
    def __init__(self, driver):
        self.driver = driver

        # Page 1
        self.bank_name = "ANZ"
        self.add_bank_search_locator = "input#xui-searchfield-1018-inputEl"
        self.add_bank_url = "https://go.xero.com/Banking/Account/#find"
        self.choose_bank_locator = "//ul[@id='dataview-1021']/li[text() = 'ANZ (NZ)']"
        #Page 2
        self.input_account_name_locator = "input#accountname-1037-inputEl"
        self.input_account_type_locator = "//ul[@id='boundlist-1076-listEl']/li[text() = 'Other']"
        self.cont_button_locator = "//span[text()='Continue']"
        self.input_account_number_locator = "input#accountnumber-1068-inputEl"

        self.dummy_account_name = "Dummy Account Name 1.0"
        self.dummy_account_number = "111111111111"

        self.dashboard_url = 'https://go.xero.com/Dashboard/'


    def search_for_ANZ(self):
        self.driver.get(self.add_bank_url)
        add_bank_search = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,self.add_bank_search_locator)))
        add_bank_search.send_keys(self.bank_name)

        search_result = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.choose_bank_locator)))
        search_result.click()

    def add_dummy_account(self):
        add_account_name = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,self.input_account_name_locator)))
        add_account_name.send_keys(self.dummy_account_name)

        self.driver.find_element_by_css_selector('input#accounttype-1039-inputEl').click() # invoke the drop-down list
        add_account_type = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,self.input_account_type_locator)))
        add_account_type.click()

        cont_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,self.cont_button_locator)))
        cont_button.click()

        add_account_number = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,self.input_account_number_locator)))
        add_account_number.send_keys(self.dummy_account_number)

        cont_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.cont_button_locator)))
        time.sleep(5)
        cont_button.click()

    def check_if_account_is_added(self):
       check_variable = WebDriverWait(self.driver, 20).until(
           EC.visibility_of_element_located((By.XPATH, "//div/a[text()='{}']".format(self.dummy_account_name))))

       massaged_check_variable = ''.join(check_variable.text.split())
       massaged_dummy_account_name = ''.join(self.dummy_account_name.split())
       massaged_dummy_account_number = ''.join(self.dummy_account_number.split())


       try:
           assert massaged_check_variable == massaged_dummy_account_name + massaged_dummy_account_number
       except AssertionError:
           print("Assertion failed. Actual value is %s" % massaged_check_variable)



    def return_to_dashboard(self):
        self.driver.get(self.dashboard_url)