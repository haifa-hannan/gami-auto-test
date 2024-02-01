from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get("https://gamification.jesica.online/auth/login")

def use_url(driver, url):
    driver.get(url)

email = WebDriverWait(driver, 3).until(
    EC.presence_of_element_located((By.ID, "email"))
)
email.click()
time.sleep(3)
email.clear()
time.sleep(3)
email.send_keys("haifahannan.rosea@mailinator.com")

password = WebDriverWait(driver, 3).until(
    EC.presence_of_element_located((By.ID, "password"))
)
password.click()
password.clear()
time.sleep(3)
password.send_keys("password123")

# time.sleep(5)
# driver.find_element(By.ID, "email").send_keys("")
# driver.find_element(By.ID, "password").send_keys("")
# Find field captcha
field_get_captcha = driver.find_element(By.XPATH, '//*[@id="__nuxt"]/div/div/div[2]/form/div/div[2]/div[3]/div[1]/span').text
# Enter the text into the 'captcha' input field
driver.find_element(By.ID, "captcha").send_keys(field_get_captcha)

button_locator = (By.CSS_SELECTOR, "#__nuxt > div > div > div.z-40.flex.h-full.w-full.items-center.justify-center > form > div > div:nth-child(2) > button")
button = WebDriverWait(driver, 3).until(
    EC.visibility_of_element_located(button_locator)
)
# Scroll into view
driver.execute_script("arguments[0].scrollIntoView();", button)
# Wait for the button to be clickable (timeout after 10 seconds)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable(button_locator))
# Click the button
button.click()
    


# Rest of your code...
# button_pm_locator = (By.XPATH, '//*[@id="__nuxt"]/div/div/div[1]/aside/div/div/div[5]/a') #HC
button_pm_locator = (By.XPATH, '/html/body/div/div/div/div[1]/aside/div/div/div[4]/a')#employee
button_pm = WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located(button_pm_locator)
)
time.sleep(3)
button_pm.click()


# button_cm_locator = (By.XPATH,'//*[@id="__nuxt"]/div/div/div[2]/main/div/div/div[2]/div[1]/span[3]')
button_cm_locator = (By.XPATH,'/html/body/div/div/div/div[2]/main/div/div/div[2]/div[1]/span[3]')
button_cm = WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located(button_cm_locator)
)
time.sleep(3)
button_cm.click()


# button_cp_locator = (By.XPATH, '//*[@id="__nuxt"]/div/div/div[2]/main/div/div/div[2]/div[2]/div/div[1]/div/button')
button_cp_locator = (By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[2]/div[2]/div/div[1]/div/button')
button_cp = WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located(button_cp_locator)
)
driver.execute_script("arguments[0].scrollIntoView();", button_cp)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable(button_cp_locator))
time.sleep(3)
button_cp.click()


dropdown_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="__nuxt"]/div/div/div[2]/main/div/div/div[2]/div/div[1]/div/div/div[1]/input'))
)
# Use the Select class to interact with the dropdown
dropdown_element.click()
# Type into the dropdown before selecting an option
dropdown_element.send_keys("jquery")
time.sleep(1)  # Add a delay if needed

# Locate the desired option within the dropdown (you may need to adjust the XPath)
desired_option = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[2]/div/div[1]/div/div/div[2]/ul'))
)
# Click on the desired option to select it
ActionChains(driver).move_to_element(desired_option).click().perform()


dropdown_validator_1 = WebDriverWait(driver, 3).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="__nuxt"]/div/div/div[2]/main/div/div/div[1]/div[2]/div[1]/div/div/div/div[1]/input'))
)
dropdown_validator_1.click()
dropdown_validator_1.send_keys("firstyara")
# Locate the desired option within the dropdown (you may need to adjust the XPath)
desired_option_validator_1 = WebDriverWait(driver, 3).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="multiselect-options"]'))
)
time.sleep(1)
# Click on the desired option to select it
ActionChains(driver).move_to_element(desired_option_validator_1).click().perform()


# dropdown_validator_2 = WebDriverWait(driver, 3).until(
#     EC.presence_of_element_located((By.XPATH, '//*[@id="__nuxt"]/div/div/div[2]/main/div/div/div[1]/div[2]/div[2]/div/div/div/div[1]/input'))
# )
# dropdown_validator_2.click()
# dropdown_validator_2.send_keys("bagus")
# # Select the desired option from the dropdown (you may need to adjust the XPath)
# desired_option_validator_2 = WebDriverWait(driver, 3).until(
#     EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[1]/div[2]/div[2]/div/div[1]/div/div[2]/ul'))
# )
# time.sleep(1)
# # Click on the desired option to select it
# ActionChains(driver).move_to_element(desired_option_validator_2).click().perform()

reward_val = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[2]/div/div[4]/div/div/div/div/div/input'))
)
reward_val.click()
reward_val.send_keys('3')


send_req = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/main/div/footer/button[3]'))
)
driver.execute_script("arguments[0].scrollIntoView();", send_req)
time.sleep(2)
send_req.click()

go_back = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div/div[2]/button'))
)
go_back.click()
# time.sleep(5)
# driver.quit()