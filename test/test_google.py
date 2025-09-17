import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    """Fixture to initialize and quit Edge WebDriver."""
    service = Service(executable_path="C:/WebDriver/msedgedriver.exe")
    options = Options()
    options.use_chromium = True
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Edge(service=service, options=options)
    yield driver
    driver.quit()


def test_python_org_title(driver):
    """Test 1: Verify Python.org title contains 'Python'."""
    driver.get("https://www.python.org")
    assert "Python" in driver.title
    print("✅ Test 1 Passed: Title contains 'Python'")


def test_python_org_search(driver):
    """Test 2: Perform a search for 'Jenkins' and check results page."""
    driver.get("https://www.python.org")
    search_box = driver.find_element(By.ID, "id-search-field")
    search_box.send_keys("Python")
    search_box.submit()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "list-recent-events"))
    )
    assert "Search" in driver.title
    print("✅ Test 2 Passed: Search results loaded")


def test_python_org_downloads(driver):
    """Test 3: Verify that 'Downloads' link is visible."""
    driver.get("https://www.python.org")
    downloads_link = driver.find_element(By.LINK_TEXT, "Downloads")
    assert downloads_link.is_displayed()
    print("✅ Test 3 Passed: Downloads link is visible")
