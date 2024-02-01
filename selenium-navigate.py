from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains

# Initialize the WebDriver
driver = webdriver.Chrome()  # Use appropriate driver (e.g., ChromeDriver, GeckoDriver)

# 3. Navigating
driver.get("https://id-id.facebook.com/")

# 3.1. Interacting with the page
# element = driver.find_element(By.ID, "passwd-id")
# element = driver.find_element(By.NAME, "passwd")
# element = driver.find_element(By.XPATH, "//input[@id='passwd-id']")
# element = driver.find_element(By.CSS_SELECTOR, "input#passwd-id")

# element.send_keys("some text")
# element.send_keys(" and some", Keys.ARROW_DOWN)
# element.clear()

# 3.2. Filling in forms
select = Select(driver.find_element(By.XPATH, "//select[@name='name']"))
all_options = select.all_selected_options
options = select.options

# Submit form
driver.find_element(By.ID, "submit").click()

# 3.3. Drag and drop
source = driver.find_element(By.NAME, "source")
target = driver.find_element(By.NAME, "target")
action_chains = ActionChains(driver)
action_chains.drag_and_drop(source, target).perform()

# 3.4. Moving between windows and frames
driver.switch_to.window("windowName")

for handle in driver.window_handles:
    driver.switch_to.window(handle)

driver.switch_to.frame("frameName")
driver.switch_to.default_content()

# 3.5. Popup dialogs
alert = driver.switch_to.alert
# Perform actions on the alert (accept, dismiss, read contents, type into prompt)

# 3.6. Navigation: history and location
driver.get("https://id-id.facebook.com/")
driver.forward()
driver.back()

# 3.7. Cookies
driver.get("https://id-id.facebook.com/")
cookie = {'name': 'foo', 'value': 'bar'}
driver.add_cookie(cookie)
all_cookies = driver.get_cookies()

# Close the browser
driver.quit()
