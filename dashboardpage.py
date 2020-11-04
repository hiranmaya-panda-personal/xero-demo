from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Dashboard:
    def __init__(self, driver):
        self.driver = driver

        self.drop_down_locator = "#header > header > div > div.xrh-appmenucontainer > button"
        self.organization_2 = "//*[@id='header']/header/div/div[1]/div/div[2]/div[3]/ol/li[1]/a"
        self.accounting_bank_tab_url = "https://go.xero.com/Bank/BankAccounts.aspx"
        self.bank_page_header = "span#title"

        self.header_locator = '#root > div > div > header > div > h1'


    def go_to_bank_page(self):
        self.driver.get(self.accounting_bank_tab_url)
        bank_span_header = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,self.bank_page_header)))
        assert bank_span_header.text == "Bank accounts", "something failed in dashboard to bank page navigation"


    def open_drop_down(self):
        org_drop_down = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,self.drop_down_locator)))
        org_drop_down.click()

    def confirm_selection(self):
        second_org_selector = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,self.organization_2)))
        second_org_selector.click()

    def confirm_transition_complete(self):
        organisation_header = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,self.header_locator)))
        assert organisation_header.text == "Trial Run 2", "something went wrong in org transition"