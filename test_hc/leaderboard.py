from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from hands.helpers import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def barLeaderBoardManagement(driver):
    click_leaderboard = (By.XPATH, '/html/body/div/div/div/div[1]/aside/div/div[1]/div[4]/a')
    justClick(driver, click_leaderboard)

    click_management = (By.XPATH, '/html/body/div/div/div/div[1]/aside/div/div[1]/div[4]/div/a[1]')
    justClick(driver, click_management)

    filterByTime(driver)

    byBusinessUnit = (By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[1]/div[1]/div/span[2]')
    justClick(driver, byBusinessUnit)

    filterByTime(driver)

    byEmployeeLevel = (By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[1]/div[1]/div/span[3]')
    justClick(driver, byEmployeeLevel)

    filterByTime(driver)

    byAllEmployee = (By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[1]/div[1]/div/span[4]')
    justClick(driver, byAllEmployee)

    filterByTime(driver)
