from selenium import webdriver
from selenium.webdriver.common.by import By
from hands.helpers import *


def claimPoint(driver):
    pointMaster = (By.XPATH, '/html/body/div/div/div/div[1]/aside/div/div/div[4]/a')
    scrollClick(driver, pointMaster)

    clickPoint = (By.XPATH,'/html/body/div/div/div/div[2]/main/div/div/div[2]/div[1]/span[3]')
    scrollClick(driver,clickPoint)

    clickClaimPoint = (By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[2]/div[2]/div/div[1]/div/button')
    scrollClick(driver, clickClaimPoint)

    dropdown_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="__nuxt"]/div/div/div[2]/main/div/div/div[2]/div/div[1]/div/div/div[1]/input'))
    )
    dropdown_element.click()
    dropdown_element.send_keys("jquery")
    time.sleep(1)
    desired_option = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[2]/div/div[1]/div/div/div[2]/ul'))
    )
    ActionChains(driver).move_to_element(desired_option).click().perform()
    time.sleep(2)

    dropdown_validator_1 = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="__nuxt"]/div/div/div[2]/main/div/div/div[1]/div[2]/div[1]/div/div/div/div[1]/input'))
    )
    dropdown_validator_1.click()
    dropdown_validator_1.send_keys("firstyara")
    desired_option_validator_1 = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="multiselect-options"]'))
    )
    time.sleep(1)
    ActionChains(driver).move_to_element(desired_option_validator_1).click().perform()
    time.sleep(2)

    reward_val = (By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[2]/div/div[4]/div/div/div/div/div/input')
    scrollClick(driver,reward_val)
    inputText(driver, reward_val, "3")
    time.sleep(2)

    sendReq = (By.XPATH, '/html/body/div/div/div/div[2]/main/div/footer/button[3]')
    scrollClick(driver, sendReq)

    goBack = (By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div/div[2]/button')
    scrollClick(driver, goBack)

    backDashboard = (By.XPATH, '/html/body/div/div/div/div[1]/aside/div/div[1]/div[1]')
    scrollClick(driver,backDashboard)

def perform_logout(driver):
    disName = (By.XPATH, '/html/body/div/div/div/div[1]/aside/div/footer/div/div')
    scrollClick(driver, disName)
    time.sleep(3)

    logot = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[1]/div[3]/button[1]'))
    )
    time.sleep(2)
    logot.click()

    logotbtn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div/div[2]/button[2]'))
    )
    time.sleep(2)
    logotbtn.click()


# if __name__ == '__main__':
#     options = webdriver.ChromeOptions()
#     options.add_experimental_option("detach", True)
#     driver = webdriver.Chrome(options=options)

#     try:
#         driver.get("https://gamification.jesica.online/auth/login")
#         perform_login(driver, "aa@mailinator.com", 'password123')
#         claimPoint(driver)
#     finally:
#         time.sleep(1)