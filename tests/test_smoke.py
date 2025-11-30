import pytest
from pages.google_page import GooglePage

def test_google_page_load(driver):
    google = GooglePage(driver)
    google.open()
    assert "Google" in driver.title

def test_google_search(driver):
    google = GooglePage(driver)
    google.open()
    google.search("ITLA")
    assert "ITLA" in driver.current_url  # compatible con "sorry page"

def test_google_search_invalid(driver):
    google = GooglePage(driver)
    google.open()
    google.search("asdfghjklqwertyuiop")
    assert "Google" in driver.title

def test_google_search_empty(driver):
    google = GooglePage(driver)
    google.open()
    google.search("")
    assert "Google" in driver.title
