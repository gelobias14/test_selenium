from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path="C:/WebDriver/msedgedriver.exe")
options = Options()
options.use_chromium = True
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")
options.add_argument("--no-sandbox")  # sometimes needed on Jenkins
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Edge(service=service, options=options)

try:
    driver.get("https://www.python.org")
    search_box = driver.find_element(By.ID, "id-search-field")
    search_box.send_keys("Jenkins")
    search_box.submit()

    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "list-recent-events"))
    )
    print("Search results visible. Test passed!")

finally:
    driver.quit()
