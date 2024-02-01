from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the WebDriver
driver = webdriver.Chrome()  # Replace with the appropriate driver (e.g., ChromeDriver, GeckoDriver)

# Open Facebook login page
driver.get("https://www.facebook.com/")

# Find and interact with elements on the page

# Wait for the email input field to be present
email_input = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.ID, "email"))
)

# Wait for the password input field to be present
password_input = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.ID, "pass"))
)

# Wait for the login button to be present
login_button = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.NAME, "login"))
)

# Enter email and password
email_input.send_keys("your_email@example.com")
password_input.send_keys("your_password")

# Click on the login button
login_button.click()

# Wait for the login to complete (adjust the condition based on the actual behavior of the page)

# Wait until the URL contains "https://www.facebook.com/"
WebDriverWait(driver, 10).until(
    EC.url_contains("https://www.facebook.com/")
)

# Close the browser
driver.quit()
