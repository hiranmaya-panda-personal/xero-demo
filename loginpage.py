from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Login:
    def __init__(self, driver):
        self.driver = driver

        self.email = "hiranmaya.panda@gmail.com"
        self.password = "Tambeh-8xurgu-zojrit"

        self.username_locator = "input#email"
        self.password_locator = "input#password"

        self.login_button = "submitButton"


    def login(self):
        inpt_element1 = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.username_locator)))
        inpt_element1.send_keys(self.email)

        inpt_element2 = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.password_locator)))
        inpt_element2.send_keys(self.password)

        btn_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, self.login_button)))
        btn_element.click()

        url_after_login = WebDriverWait(self.driver, 20).until(EC.url_matches("https://go.xero.com/Dashboard/"))
        assert url_after_login == True, "something failed during login"