from selenium import webdriver
from hands.helpers import perform_login
from test_employee.claim_point import *
from test_employee.claim_point_draft import claimPointDraft
from test_employee.one_cycle import *
from hands.helpers import *
import time

def main():
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=2560,1440")
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)

    accounts = {'hc':{'email':'ijlal.saputra@yopmail.com','password':'password123'},
                'employee':{'email':"haifahannan.rosea@yopmail.com", 'password':'password123'}}
    
    role = 'employee'

    acc = accounts.get(role)

    try:
        driver.get("https://gamification.jesica.online/auth/login")
        if acc:
            perform_login(driver, acc['email'], acc['password'])
            if role == 'hc':
                oneCycle(driver)
            elif role == 'employee':
                perform_logout(driver)
        else:
            None

    finally:
        time.sleep(3)
        driver.close()
        

if __name__ == "__main__":
    main()