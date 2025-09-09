from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def test_login_success():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.saucedemo.com/")

    # 1. Username
    username_input = driver.find_element("id", "user-name")
    username_input.send_keys("standard_user")

    # 2. Password
    password_input = driver.find_element("id", "password")
    password_input.send_keys("secret_sauce")

    # 3. Bouton Login
    login_button = driver.find_element("id", "login-button")
    login_button.click()

    # 4. Vérification
    page_title = driver.find_element("class name", "title").text
    assert page_title == "Products"

    driver.quit()
