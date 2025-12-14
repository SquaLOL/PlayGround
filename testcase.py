import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

options = webdriver.EdgeOptions()

# Снижение риска капчи
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Edge(options=options)

try:
    driver.get("https://www.google.com")

    # Ждём поле ввода
    search_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )

    time.sleep(1)  # небольшая задержка — ведём себя как человек

    search_input.send_keys("selene python")
    search_input.send_keys(Keys.RETURN)

    # Ждём появления результатов
    results = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "search"))
    )

    # Проверка текста на странице
    assert "Selene" in results.text or "selene" in results.text

    print("Test passed successfully!")

finally:
    driver.quit()
