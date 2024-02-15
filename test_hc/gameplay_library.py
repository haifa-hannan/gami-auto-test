from selenium.webdriver.common.by import By
from hands.helpers import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def barGameplyLibrary(driver):
    time.sleep(3)
    close_sidebarHC = (By.XPATH, '/html/body/div/div/div/div[1]/aside/div/header/button')
    scrollClick(driver, close_sidebarHC)
    
    open_sidebarHC = (By.CSS_SELECTOR, '#__nuxt > div > div > div.z-50.w-full.md\:h-full.md\:w-fit.lg\:relative.lg\:z-0 > aside > div > header > button')
    scrollClick(driver, open_sidebarHC)
    time.sleep(3)

    exploreHC = (By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[1]/div[1]/div[3]/span')
    scrollClick(driver, exploreHC)
    time.sleep(1)

    searchGPHC = (By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[1]/div/div')
    justClick(driver, searchGPHC)

    inputSearch = (By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[1]/div/div/input')
    inputText(driver, inputSearch, "test")

    closeSearch = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#__nuxt > div > div > div.relative.flex.h-full.max-w-full.flex-1.overflow-auto > main > div > div > div.inline-flex.w-full.flex-col.justify-start.gap-2.sm\:flex-row.sm\:items-center.sm\:justify-between > div > div > svg:nth-child(3)'))
    )
    closeSearch.click()
    time.sleep(3)

def GameplayLibraryFilter(driver):
    filterbtn = (By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[1]/div/button')
    justClick(driver, filterbtn)
    employeeReq = (By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div[1]/input')
    justClick(driver, employeeReq)
    applybtn = (By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[2]/div[2]/button[2]')
    justClick(driver, applybtn)
    time.sleep(3)

    filterbtn2 = (By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[1]/div/button')
    justClick(driver, filterbtn2)
    hcInput = (By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div[2]/input')
    justClick(driver, hcInput)
    applybtn2 = (By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[2]/div[2]/button[2]')
    justClick(driver, applybtn2)
    time.sleep(3)

    filterbtn3 = (By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[1]/div/button')
    justClick(driver, filterbtn3)
    systemGenerate = (By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div[3]/input')
    justClick(driver, systemGenerate)
    applybtn3 = (By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[2]/div[2]/button[2]')
    justClick(driver, applybtn3)
    time.sleep(3)

    filterbtn12 = (By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[1]/div/button')
    justClick(driver, filterbtn12)
    employeeReq12 = (By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div[1]/input')
    justClick(driver, employeeReq12)
    hcInput12 = (By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div[2]/input')
    justClick(driver, hcInput12)
    applybtn12 = (By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[2]/div[2]/button[2]')
    justClick(driver, applybtn12)
    time.sleep(3)

    filterbtn13 = (By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[1]/div/button')
    justClick(driver, filterbtn13)
    employeeReq13 = (By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div[1]/input')
    justClick(driver, employeeReq13)
    systemGenerate13 = (By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div[3]/input')
    justClick(driver, systemGenerate13)
    applybtn13 = (By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[2]/div[2]/button[2]')
    justClick(driver, applybtn13)
    time.sleep(3)

    filterbtn23 = (By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[1]/div/button')
    justClick(driver, filterbtn23)
    hcInput23 = (By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div[2]/input')
    justClick(driver, hcInput23)
    systemGenerate23 = (By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div[3]/input')
    justClick(driver, systemGenerate23)
    applybtn23 = (By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[2]/div[2]/button[2]')
    justClick(driver, applybtn23)
    time.sleep(3)

    filterbtn123r = (By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[1]/div/button')
    justClick(driver, filterbtn123r)
    employeeReq123r = (By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div[1]/input')
    justClick(driver, employeeReq123r)
    hcInput123r = (By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div[2]/input')
    justClick(driver, hcInput123r)
    systemGenerate123r = (By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div[3]/input')
    justClick(driver, systemGenerate123r)
    resetFilter = (By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[2]/div[2]/button[1]')
    justClick(driver, resetFilter)
    time.sleep(3)
    
    filterbtn123 = (By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[1]/div/button')
    justClick(driver, filterbtn123)
    employeeReq123 = (By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div[1]/input')
    justClick(driver, employeeReq123)
    hcInput123 = (By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div[2]/input')
    justClick(driver, hcInput123)
    systemGenerate123 = (By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div[3]/input')
    justClick(driver, systemGenerate123)
    applybtn123 = (By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[2]/div[2]/button[2]')
    justClick(driver, applybtn123)
    time.sleep(3)

