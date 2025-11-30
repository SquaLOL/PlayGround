from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Edge()

try:
    driver.get('https://google.com')

    search_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )

    assert search_input.get_attribute("value") == ""

    search_input.send_keys('selene')
    search_input.send_keys(Keys.RETURN)

    target_text = 'User-oriented WEB UI browser test in Python'
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#search"), target_text)
    )
    print("Test passed successfully!")

finally:
    driver.quit()
