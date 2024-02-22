from selenium import webdriver
from hands.helpers import perform_login
from test_employee.claim_point import *
from test_employee.claim_point_draft import claimPointDraft
from test_employee.one_cycle import *
from test_hc.gameplay_library import *
from test_hc.gameplay_master import *
from test_hc.leaderboard import *
from test_hc.point_master import *
from test_hc.master_data import *
from hands.helpers import *
import time

def main():
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=2560,1440")
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)

    accounts = {'hc':{'email':'ijlal.saputra@mailinator.com','password':'password123'},
                'employee':{'email':"haifahannan.rosea@mailinator.com", 'password':'password123'},
                'test':{'email': "gamification.app@sigma.co.id", 'password':'TSigm4#2402!!'}}
    
    role = 'test'

    acc = accounts.get(role)

    try:
        driver.get("https://gamification.jesica.online/auth/login")
        if acc:
            perform_login(driver, acc['email'], acc['password'])
            time.sleep(10)
            if role == 'hc'or role == 'test':
                # barGameplyLibrary(driver)
                # time.sleep(1)
                # GameplayLibraryFilter(driver)
                # time.sleep(1)
                # barGameplayMaster(driver)
                # barLeaderBoardManagement(driver)
                # barLeaderBoardEmployee(driver)
                barPointMaster(driver)
                masterData(driver)
                # logota = (By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[1]/div[2]/div[2]/div/button[1]')
                # perform_logout(driver, logota)
            elif role == 'employee' :
                oneCycle(driver)
                claimPoint(driver)
                claimPointDraft(driver)
                logote = (By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[1]/div[3]/button[1]')
                perform_logout(driver, logote)
        else:
            None
    # except Exception as e:
    #     print(e)
    #     if "selenium.common.exceptions" in str(e):
    #         # Kesalahan terkait Selenium
    #         print("Terjadi kesalahan dalam eksekusi Selenium:", e)
    #     else:
    #         # Kesalahan lainnya dalam codingan
    #         print("Terjadi kesalahan dalam codingan:", e)

    finally:
        time.sleep(3)
        driver.close()
        

if __name__ == "__main__":
    main()