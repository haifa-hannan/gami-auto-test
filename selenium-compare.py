from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get("https://gate.um.ac.id/")

button_locator = (By.CSS_SELECTOR, '.btn.btn-secondary.text-white.font-weight-medium')
button = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(button_locator)
)

driver.execute_script("arguments[0].scrollIntoView();", button)

WebDriverWait(driver, 10).until(EC.element_to_be_clickable(button_locator))

button.click()