from selenium.webdriver.common.by import By
from hands.helpers import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def masterData(driver):
    master_data = (By.XPATH, '/html/body/div/div/div/div[1]/aside/div/div[1]/div[6]/a')
    justClick(driver, master_data)

    click_points = (By.XPATH, '/html/body/div/div/div/div[1]/aside/div/div[1]/div[6]/div/a[1]')
    justClick(driver, click_points)
    time.sleep(5)

    search_list_points = (By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[1]/div/div[1]')
    justClick(driver, search_list_points)

    input_search_list_points = (By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[1]/div/div[1]/input')
    inputText(driver, input_search_list_points, "test")

    close_search_list_points = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#__nuxt > div > div > div.relative.flex.h-full.max-w-full.flex-1.overflow-auto > main > div > div > div.flex.flex-col.md\:inline-flex.md\:flex-row.w-full.items-center.justify-between > div > div.search-container.flex.cursor-pointer.items-center.justify-between.gap-2.rounded-full.bg-white.p-2.text-sm > svg.icon.close-icon.relative.h-5.w-5.text-gray-500'))
    )
    time.sleep(1)
    close_search_list_points.click()

    click_filter_status = (By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[1]/div/div[2]/div/div/div[1]')
    active = (By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[1]/div/div[2]/div/div/div[2]/ul/li[2]')
    inactive = (By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[1]/div/div[2]/div/div/div[2]/ul/li[3]')
    selectDropdown(driver, click_filter_status, active)
    selectDropdown(driver, click_filter_status, inactive)

    