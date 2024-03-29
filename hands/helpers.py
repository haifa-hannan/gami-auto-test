from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains

def perform_login(driver, email, password):  
    email_input = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.ID, "email"))
    )
    email_input.click()
    email_input.clear()
    time.sleep(1)
    email_input.send_keys(email)

    password_input = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.ID, "password"))
    )
    password_input.click()
    password_input.clear()
    # time.sleep(1)
    password_input.send_keys(password)

    visibility = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/form/div/div[2]/div[2]/div/div'))
    )
    visibility.click()
    # time.sleep(1)

    field_get_captcha = driver.find_element(By.XPATH, '//*[@id="__nuxt"]/div/div/div[2]/form/div/div[2]/div[3]/div[1]/span').text
    driver.find_element(By.ID, "captcha").send_keys(field_get_captcha)

    button_locator = (By.CSS_SELECTOR, "#__nuxt > div > div > div.z-40.flex.h-full.w-full.items-center.justify-center > form > div > div:nth-child(2) > button")
    button = WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located(button_locator)
    )
    driver.execute_script("arguments[0].scrollIntoView();", button)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(button_locator))
    button.click()

def perform_logout(driver, locate):
    disName = (By.XPATH, '/html/body/div/div/div/div[1]/aside/div/footer/div/div')
    scrollClick(driver, disName)
    time.sleep(3)

    logot = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(locate)
    )
    time.sleep(2)
    logot.click()

    logotbtn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div/div[2]/button[2]'))
    )
    time.sleep(2)
    logotbtn.click()

def scrollClick(driver, locate, timeout=5):
    element = WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located(locate)
    )
    driver.execute_script("arguments[0].scrollIntoView();", element)
    
    WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(locate)
    )
    element.click()

def justClick(driver, locate):
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(locate)
    )
    element.click()

def inputText(driver, locate, text):
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(locate)
    )
    element.click()
    element.send_keys(text)

def clearingText(driver, locate):
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(locate)
    )
    element.click()


def selectDropdown(driver, ddLocate, clickLocate):
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(ddLocate)
    )
    element.click()
    time.sleep(1)
    desired_option = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(clickLocate)
    )
    ActionChains(driver).move_to_element(desired_option).click().perform()
    time.sleep(1)

def inputNumber(driver):
    reward_valDraft = (By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[2]/div/div[4]/div/div/div/div/div/input')
    scrollClick(driver,reward_valDraft)
    inputText(driver, reward_valDraft, "3")



def filterByTime(driver):
    daily_click = (By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[1]/div[2]/div[1]/span[1]')
    justClick(driver, daily_click)
    time.sleep(1)

    weekly_click = (By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[1]/div[2]/div[1]/span[2]')
    justClick(driver, weekly_click)
    time.sleep(1)

    monthly_click = (By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[1]/div[2]/div[1]/span[3]')
    justClick(driver, monthly_click)
    time.sleep(1)

    # filterHighLow = (By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[1]/div[2]/div[2]/button')
    # justClick(driver, filterHighLow)

    # lowest = (By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/div[2]/input')
    # justClick(driver, lowest)

    # apply = (By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[2]/div[2]/button[2]')
    # justClick(driver, apply)

    # filterHighLow2 = (By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[1]/div[2]/div[2]/button')
    # justClick(driver, filterHighLow2)
    # lowest2 = (By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/div[2]/input')
    # justClick(driver, lowest2)
    # highest = (By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/input')
    # justClick(driver, highest)
    # apply2 = (By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[2]/div[2]/button[2]')
    # justClick(driver, apply2)

    # searchbtn = (By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[1]/div[2]/div[2]/div')
    # justClick(driver, searchbtn)

    # inputSearch = (By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[1]/div[2]/div[2]/div/input')
    # inputText(driver, inputSearch, "search")

    # closeSearch = (By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[1]/div[2]/div[2]/div/svg[2]')
    # justClick(driver, closeSearch)