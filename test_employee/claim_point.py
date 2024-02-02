from selenium import webdriver
from selenium.webdriver.common.by import By
from helpers.helpers import *


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

def claimPointDraft(driver):
    pointMaster = (By.XPATH, '/html/body/div/div/div/div[1]/aside/div/div/div[4]/a')
    scrollClick(driver, pointMaster)

    clickPoint = (By.XPATH,'/html/body/div/div/div/div[2]/main/div/div/div[2]/div[1]/span[3]')
    scrollClick(driver,clickPoint)

    clickClaimPoint = (By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[2]/div[2]/div/div[1]/div/button')
    scrollClick(driver, clickClaimPoint)

    dropdown_elementDraft = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="__nuxt"]/div/div/div[2]/main/div/div/div[2]/div/div[1]/div/div/div[1]/input'))
    )
    dropdown_elementDraft.click()
    dropdown_elementDraft.send_keys("sangku")
    time.sleep(1)
    desired_optionDraft = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[2]/div/div[1]/div/div/div[2]/ul'))
    )
    ActionChains(driver).move_to_element(desired_optionDraft).click().perform()

    dropdown_validator_1Draft = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="__nuxt"]/div/div/div[2]/main/div/div/div[1]/div[2]/div[1]/div/div/div/div[1]/input'))
    )
    dropdown_validator_1Draft.click()
    dropdown_validator_1Draft.send_keys("firstyara")
    desired_option_validator_1Draft = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="multiselect-options"]'))
    )
    time.sleep(1)
    ActionChains(driver).move_to_element(desired_option_validator_1Draft).click().perform()

    dropdown_criteriaDraft1 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[2]/div/div[4]/div/div[1]/div/div/div/div/div[1]'))
    )
    dropdown_criteriaDraft1.click()
    # dropdown_elementDraft.send_keys("jquery")
    time.sleep(1)
    desired_option_criteria1 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[2]/div/div[4]/div/div[1]/div/div/div/div/div[2]/ul/li[2]'))
    )
    ActionChains(driver).move_to_element(desired_option_criteria1).click().perform()
    time.sleep(2)

    dropdown_criteriaDraft = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[2]/div/div[4]/div/div[1]/div/div/div/div/div[1]'))
    )
    dropdown_criteriaDraft.click()
    # dropdown_elementDraft.send_keys("jquery")
    time.sleep(1)
    desired_option_criteria = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[2]/div/div[4]/div/div[1]/div/div/div/div/div[2]/ul/li[1]'))
    )
    ActionChains(driver).move_to_element(desired_option_criteria).click().perform()
    time.sleep(2)

    reward_valDraft = (By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[2]/div/div[4]/div/div/div/div/div/input')
    scrollClick(driver,reward_valDraft)
    inputText(driver, reward_valDraft, "3")

    radio1 = (By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[2]/div/div[4]/div/div[3]/div/div/div[1]/input')
    scrollClick(driver, radio1)
    time.sleep(1)

    radio2 = (By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[2]/div/div[4]/div/div[3]/div/div/div[2]/input')
    scrollClick(driver, radio2)
    time.sleep(1)

    radio3 = (By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[2]/div/div[4]/div/div[3]/div/div/div[3]/input')
    scrollClick(driver, radio3)
    time.sleep(1)

    radio4 = (By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[2]/div/div[4]/div/div[3]/div/div/div[4]/input')
    scrollClick(driver, radio4)
    time.sleep(1)

    saveDraft = (By.XPATH, '/html/body/div/div/div/div[2]/main/div/footer/button[2]')
    scrollClick(driver, saveDraft)

    goBackDraft = (By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div/div[2]/button')
    scrollClick(driver, goBackDraft)


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