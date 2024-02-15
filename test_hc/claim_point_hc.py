from selenium import webdriver
from selenium.webdriver.common.by import By
from hands.helpers import *


def claimPointHC(driver):
    pointMasterHC = (By.XPATH, '/html/body/div/div/div/div[1]/aside/div/div[1]/div[5]/a')
    scrollClick(driver, pointMasterHC)

    clickPointHC = (By.XPATH,'/html/body/div/div/div/div[2]/main/div/div/div[2]/div[1]/span[3]')
    scrollClick(driver,clickPointHC)

    clickClaimPointHC = (By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[2]/div[2]/div/div[1]/div/button')
    scrollClick(driver, clickClaimPointHC)

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



