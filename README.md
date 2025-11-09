E-Commerce Automation Framework

This project is a Selenium-based test automation framework built using Python and PyTest. It automates key user flows on an e-commerce demo website, including login and adding products to the cart. The framework follows the Page Object Model (POM) structure to keep the tests maintainable and easy to extend.

Features

Python + Selenium WebDriver

PyTest test runner

Page Object Model structure

Webdriver-Manager for driver setup

HTML report generation

Covered Scenarios

Login with valid credentials

Add product to cart and navigate to cart page

How to Run

Install dependencies:

pip install -r requirements.txt


Run tests:

pytest -v


Run with HTML report:

pytest --html=reports/report.html --self-contained-html -v

Project Structure
config/       -> Environment and test data
pages/        -> Page objects
tests/        -> Test scripts
utilities/    -> WebDriver setup
reports/      -> Test reports

Tech Stack

Python, Selenium, PyTest, Webdriver-Manager, PyTest-HTML

Author

Manoj Kumar J
Email: manumanoj50333@gmail.com
