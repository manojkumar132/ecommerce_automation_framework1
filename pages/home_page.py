from selenium.webdriver.common.by import By

class HomePage:
    add_to_cart_btn = (By.XPATH, "//button[contains(text(), 'Add to cart')]")
    cart_icon = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self):
        self.driver.find_element(*self.add_to_cart_btn).click()

    def open_cart(self):
        self.driver.find_element(*self.cart_icon).click()
