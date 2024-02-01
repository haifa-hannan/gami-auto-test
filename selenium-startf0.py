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

# Scroll into view
driver.execute_script("arguments[0].scrollIntoView();", button)

# Wait for the button to be clickable (timeout after 10 seconds)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable(button_locator))

# Click the button
button.click()
driver.quit()
# Rest of your code...

# driver.find_element(By.ID, "form-username").send_keys("230761603741")
# driver.find_element(By.ID, "form-password").send_keys("besokdeh")

# button_login_locator = (By.CSS_SELECTOR, "btn.btn-block.btn-primary")
# button_login = WebDriverWait(driver, 10).until(
#     EC.visibility_of_any_elements_located(button_login_locator)
# )

# # driver.execute_script("arguments[0].scrollIntoView();", button_login)

# WebDriverWait(driver, 10).until(EC.element_to_be_clickable(button_login_locator))


# button_login.click()

# driver.quit()