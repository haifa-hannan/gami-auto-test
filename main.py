from selenium import webdriver
from hands.helpers import perform_login
from test_employee.claim_point import *
from test_employee.claim_point_draft import *
from hands.helpers import *
import time

def main():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)



    try:
        driver.get("https://gamification.jesica.online/auth/login")
        perform_login(driver,"haifahannan.rosea@mailinator.com", 'password123')
        # claimPoint(driver)
        # claimPointDraft(driver)
        perform_logout(driver)

    finally:
        time.sleep(3)

if __name__ == "__main__":
    main()