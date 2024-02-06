from selenium.webdriver.common.by import By
from hands.helpers import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def oneCycle(driver):
    close_sidebar = (By.XPATH, '/html/body/div/div/div/div[1]/aside/div/header/button')
    scrollClick(driver, close_sidebar)

    open_sidebar = (By.CSS_SELECTOR, '#__nuxt > div > div > div.z-50.w-full.md\:h-full.md\:w-fit.lg\:relative.lg\:z-0 > aside > div > header > button')
    scrollClick(driver, open_sidebar)
    time.sleep(3)

    explore = (By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[1]/div[1]/div[3]/span')
    scrollClick(driver, explore)
    time.sleep(1)

    searchGP = (By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[1]/div/div')
    justClick(driver, searchGP)

    inputSearch = (By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[1]/div/div/input')
    inputText(driver, inputSearch, "sangku")
    time.sleep(3)
