from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_open_saucedemo():
    # Lance Chrome automatiquement avec le bon driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Ouvre le site cible
    driver.get("https://www.saucedemo.com/")

    # Vérifie que le titre de la page contient "Swag Labs"
    assert "Swag Labs" in driver.title

    # Ferme le navigateur
    driver.quit()
