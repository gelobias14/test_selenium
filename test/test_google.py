from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def test_google_search():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")

    # Handle consent popup if it exists
    try:
        consent_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'I agree') or contains(., 'Accept all')]"))
        )
        consent_button.click()
    except TimeoutException:
        pass  # no consent popup, continue

    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Jenkins Selenium Test")
    search_box.submit()

    # Wait for search results
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div#search"))
    )

    assert "Jenkins Selenium Test" in driver.title
    driver.quit()
