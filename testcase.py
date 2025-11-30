from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Initialize the browser (Chrome is used as default)
driver = webdriver.Edge()

try:
    # 1. Open the URL
    driver.get('https://google.com')

    # 2. Find the search field by name="q"
    # We use WebDriverWait to ensure the element is ready before interacting
    search_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )

    # Equivalent to .should(be.blank)
    # We check that the current value of the input is an empty string
    assert search_input.get_attribute("value") == ""

    # 3. Type query and press Enter
    search_input.send_keys('selene')
    search_input.send_keys(Keys.RETURN)

    # 4. Check results
    # Equivalent to browser.element('#search').should(have.text(...))
    # We wait until the element with ID 'search' contains the specific text
    target_text = 'User-oriented WEB UI browser test in Python'
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#search"), target_text)
    )

    print("Test passed successfully!")

finally:
    # Always close the browser, even if errors occur
    driver.quit()
