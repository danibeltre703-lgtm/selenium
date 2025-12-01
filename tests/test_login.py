import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://thinking-tester-contact-list.herokuapp.com/"


VALID_EMAIL = "danibeltre703@gmail.com"
VALID_PASSWORD = "Dbeltr3"
INVALID_PASSWORD = "clave_incorrecta"


def _hacer_login(driver, email, password):
    driver.get(BASE_URL)

    driver.find_element(By.ID, "email").clear()
    driver.find_element(By.ID, "email").send_keys(email)

    driver.find_element(By.ID, "password").clear()
    driver.find_element(By.ID, "password").send_keys(password)

    driver.find_element(By.ID, "submit").click()


def test_login_exitoso(driver):
    """Camino feliz: login con credenciales válidas."""
    _hacer_login(driver, VALID_EMAIL, VALID_PASSWORD)

    
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "add-contact"))  
    )

    assert "Add a New Contact" in driver.page_source


def test_login_fallido(driver):
    """Prueba negativa: password incorrecto muestra error."""
    _hacer_login(driver, VALID_EMAIL, INVALID_PASSWORD)

    WebDriverWait(driver, 10).until(
        lambda d: "Incorrect username or password" in d.page_source
                  or "incorrect" in d.page_source.lower()
    )

    assert "incorrect" in driver.page_source.lower()
