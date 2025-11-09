from utilities.driver_setup import get_driver
from config.config import BASE_URL, USERNAME, PASSWORD
from pages.login_page import LoginPage

def test_valid_login():
    driver = get_driver()
    driver.get(BASE_URL)

    login = LoginPage(driver)
    login.login(USERNAME, PASSWORD)

    assert "inventory" in driver.current_url
    driver.quit()
