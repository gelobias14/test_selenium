from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_python_org():
    print("Starting Python.org test...")

    service = Service(executable_path="C:/WebDriver/msedgedriver.exe")
    options = Options()
    options.use_chromium = True
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Edge(service=service, options=options)

    try:
        driver.get("https://www.python.org")
        print("Opened Python.org homepage.")

        search_box = driver.find_element(By.ID, "id-search-field")
        search_box.send_keys("Jenkins")
        search_box.submit()
        print("Submitted search query.")

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "list-recent-events"))
        )
        print("Search results visible. Test passed!")

    finally:
        driver.quit()
        print("Browser closed.")

if __name__ == "__main__":
    test_python_org()
