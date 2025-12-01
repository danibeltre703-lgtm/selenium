
import pytest
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager



def pytest_runtest_makereport(item, call):
    if "driver" in item.fixturenames and call.when == "call":
        item._test_has_failed = call.excinfo is not None



@pytest.fixture
def driver(request):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=options
    )

    yield driver

 
    test_failed = getattr(request.node, "_test_has_failed", False)

    if test_failed:
        screenshots_dir = Path("screenshots")
        screenshots_dir.mkdir(exist_ok=True)

        file_name = screenshots_dir / f"{request.node.name}.png"
        driver.save_screenshot(str(file_name))

    driver.quit()
