from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_gamification import use_url, login_gamification, click_element
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get("https://gamification.jesica.online/")
by = By.CSS_SELECTOR
def login_gam():
    email = ""
    pw = ""
    login_gamification(driver, email, pw)


try:
    pm_val =  "#__nuxt > div > div > div.absolute.z-50.h-full.w-fit.lg\:relative.lg\:z-0 > aside > div > div > div:nth-child(5) > a"
    click_element(driver, by, pm_val)
except ValueError:
    print("error")


try:
    cm_val = "#__nuxt > div > div > div.relative.flex.h-full.max-w-full.flex-1.overflow-auto > main > div > div > div.inline-flex.w-full.flex-col.gap-4 > div.flex.w-fit.flex-row.items-center.gap-2.rounded-lg.bg-white.p-2 > span:nth-child(3)"
    click_element(driver, by, cm_val)
except ValueError:
    print("error")


try:
    cp_val = "#__nuxt > div > div > div.relative.flex.h-full.max-w-full.flex-1.overflow-auto > main > div > div > div.inline-flex.w-full.flex-col.gap-4 > div.h-fit.w-full.rounded-lg.bg-white.p-4 > div > div.mb-6.inline-flex.w-full.flex-col.justify-start.gap-2.sm\:flex-row.sm\:items-center.sm\:justify-between > div > button"
    click_element(driver, by, cp_val)
except ValueError:
    print("error")

time.sleep(3)
driver.quit()