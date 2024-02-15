from selenium.webdriver.common.by import By
from hands.helpers import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

inputs_title = ["sele-1", "sele-2", "sele-3", "sele-4", "sele-5", "sele-6", "sele-7", "sele-8", "sele-9", "sele-10", "sele-11"]

inputs_desc = ["Description sele-1", "Description sele-2", "Description sele-3", "Description sele-4", "Description sele-5", "Description sele-6", "Description sele-7", "Description sele-8", "Description sele-9", "Description sele-10", "Description sele-11"]

game_master_buttons = ["/html/body/div/div/div/div[2]/main/div/div/div[2]/footer/button[1]", "/html/body/div/div/div/div[2]/main/div/div/div[2]/footer/button[2]", "/html/body/div/div/div/div[2]/main/div/div/div[2]/footer/button[3]"]

def barGameplayMaster(driver):
    game_master = (By.XPATH, '/html/body/div/div/div/div[1]/aside/div/div[1]/div[3]/a')
    scrollClick(driver, game_master)

    add_new_game = (By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[1]/div/button[2]')
    justClick(driver, add_new_game)

    click_title = (By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[2]/div[1]/div[1]/div/div')
    justClick(driver, click_title)

    for input_title_text in inputs_title:

        input_title = (By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[2]/div[1]/div[1]/div/div/input')
        inputText(driver, input_title, input_title_text)

    generated_by = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[2]/div[1]/div[2]/div/div/div'))
    )
    generated_by.click()
    desired_option = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[2]/div[1]/div[2]/div/div/div/div[2]/ul/li[3]'))
    )
    ActionChains(driver).move_to_element(desired_option).click().perform()
    time.sleep(2)

    choose_thumbnail = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[2]/div[1]/div[3]/div/div/input'))
    )
    choose_thumbnail.send_keys("C:/Users/HP/Downloads/download (1).jpg")

    for input_description_text in inputs_desc:

        input_description = (By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[2]/div[1]/div[4]/div/div[2]')
        inputText(driver, input_description, input_description_text)

    for buttons_game in game_master_buttons:
        click_button = (By.XPATH, buttons_game)
        justClick(driver, click_button)