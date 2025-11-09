from selenium.webdriver.common.by import By

class LoginPage:
    username = (By.ID, "user-name")
    password = (By.ID, "password")
    login_btn = (By.ID, "login-button")

    def __init__(self, driver):
        self.driver = driver

    def login(self, u, p):
        self.driver.find_element(*self.username).send_keys(u)
        self.driver.find_element(*self.password).send_keys(p)
        self.driver.find_element(*self.login_btn).click()
