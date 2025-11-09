from utilities.driver_setup import get_driver
from config.config import BASE_URL, USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.home_page import HomePage

def test_add_to_cart():
    driver = get_driver()
    driver.get(BASE_URL)

    login = LoginPage(driver)
    login.login(USERNAME, PASSWORD)

    home = HomePage(driver)
    home.add_to_cart()
    home.open_cart()

    assert "cart" in driver.current_url
    driver.quit()
