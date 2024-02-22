from selenium.webdriver.common.by import By
from hands.helpers import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def barPointMaster(driver):

# ===================== point history =============    
    pointMasterBtn = (By.XPATH, '/html/body/div/div/div/div[1]/aside/div/div[1]/div[5]/a')
    justClick(driver, pointMasterBtn)

    search_point_history = (By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[2]/div[2]/div[1]/div/div[1]')
    justClick(driver, search_point_history)

    input_search_ph = (By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[2]/div[2]/div[1]/div/div[1]/input')
    inputText(driver, input_search_ph, "test")

    close_search_ph = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#__nuxt > div > div > div.relative.flex.h-full.max-w-full.flex-1.overflow-auto > main > div > div > div.flex.w-full.flex-col.gap-4 > div.h-full.w-full.rounded-lg.bg-white.p-4 > div.flex.flex-col.md\:inline-flex.md\:flex-row.md\:items-center.w-full.justify-between > div > div.search-container.flex.cursor-pointer.items-center.justify-between.gap-2.rounded-full.bg-white.p-2.border.text-sm > svg.icon.close-icon.relative.h-5.w-5.text-gray-500'))
    )
    time.sleep(1)
    close_search_ph.click()

    click_filter_status_active = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[2]/div[2]/div[1]/div/div[2]/div/div'))
    )
    click_filter_status_active.click()
    time.sleep(1)
    active = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div[2]/ul/li[2]'))
    )
    ActionChains(driver).move_to_element(active).click().perform()
    time.sleep(1)

    click_filter_status_expired = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[2]/div[2]/div[1]/div/div[2]/div/div'))
    )
    click_filter_status_expired.click()
    time.sleep(1)
    expired = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div[2]/ul/li[3]'))
    )
    ActionChains(driver).move_to_element(expired).click().perform()
    time.sleep(1)

    # click_filter_status = (By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[2]/div[2]/div[1]/div/div[2]/div/div')
    # active = (By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div[2]/ul/li[2]')
    # expired = (By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div[2]/ul/li[3]')
    # selectDropdown(driver, click_filter_status,active)
    # selectDropdown(driver, click_filter_status,expired)
    

# =============== point badges =================

    badges_history = (By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[2]/div[1]/span[2]')
    justClick(driver, badges_history)

    search_badges = (By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[2]/div[2]/div[1]/div/div')
    justClick(driver, search_badges)

    input_search_badges = (By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[2]/div[2]/div[1]/div/div/input')
    inputText(driver, input_search_badges, "test")

    close_search_badges = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#__nuxt > div > div > div.relative.flex.h-full.max-w-full.flex-1.overflow-auto > main > div > div > div.flex.w-full.flex-col.gap-4 > div.h-full.w-full.rounded-lg.bg-white.p-4 > div.flex.flex-col.md\:inline-flex.md\:flex-row.md\:items-center.w-full.justify-between > div > div > svg.icon.close-icon.relative.h-5.w-5.text-gray-500'))
    )
    time.sleep(1)
    close_search_badges.click()

# ================= claim points =================

    claim_points = (By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[2]/div[1]/span[3]')
    justClick(driver, claim_points)

    search_claim_points = (By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[2]/div[2]/div/div[1]/div/div[1]')
    justClick(driver, search_claim_points)

    input_search_cm = (By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[2]/div[2]/div/div[1]/div/div[1]/input')
    inputText(driver, input_search_cm, "test")

    close_search_cm = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#__nuxt > div > div > div.relative.flex.h-full.max-w-full.flex-1.overflow-auto > main > div > div > div.flex.w-full.flex-col.gap-4 > div.h-full.w-full.rounded-lg.bg-white.p-4 > div > div.mb-6.inline-flex.w-full.flex-col.justify-start.gap-2.sm\:flex-row.sm\:items-center.sm\:justify-between > div > div.flex.max-w-full.cursor-pointer.items-center.justify-between.gap-2.rounded-full.bg-white.px-2\.5.md\:p-2.border.border-gray-300.py-0 > svg:nth-child(3)'))
    )
    time.sleep(1)
    close_search_cm.click()

    # click_filter_status_draft = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[2]/div[2]/div/div[1]/div/div[2]/div/div'))
    # )
    # click_filter_status_draft.click()
    # time.sleep(1)
    # draft = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[2]/div[2]/div/div[1]/div/div[2]/div/div/div[2]/ul/li[2]'))
    # )
    # ActionChains(driver).move_to_element(draft).click().perform()
    # time.sleep(1)

    # click_filter_status_waiting = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[2]/div[2]/div/div[1]/div/div[2]/div/div'))
    # )
    # click_filter_status_waiting.click()
    # time.sleep(1)
    # waiting = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[2]/div[2]/div/div[1]/div/div[2]/div/div/div[2]/ul/li[3]'))
    # )
    # ActionChains(driver).move_to_element(waiting).click().perform()
    # time.sleep(1)

    # click_filter_status_approved = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[2]/div[2]/div/div[1]/div/div[2]/div/div'))
    # )
    # click_filter_status_approved.click()
    # time.sleep(1)
    # approved = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[2]/div[2]/div/div[1]/div/div[2]/div/div/div[2]/ul/li[4]'))
    # )
    # ActionChains(driver).move_to_element(approved).click().perform()
    # time.sleep(1)

    # click_filter_status_rejected = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[2]/div[2]/div/div[1]/div/div[2]/div/div'))
    # )
    # click_filter_status_rejected.click()
    # time.sleep(1)
    # rejected = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[2]/div[2]/div/div[1]/div/div[2]/div/div/div[2]/ul/li[5]'))
    # )
    # ActionChains(driver).move_to_element(rejected).click().perform()
    # time.sleep(1)

    click_filter_status_claim_points = (By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[2]/div[2]/div/div[1]/div/div[2]/div/div')
    draft = (By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[2]/div[2]/div/div[1]/div/div[2]/div/div/div[2]/ul/li[2]')
    waiting = (By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[2]/div[2]/div/div[1]/div/div[2]/div/div/div[2]/ul/li[3]')
    approved = (By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[2]/div[2]/div/div[1]/div/div[2]/div/div/div[2]/ul/li[4]')
    rejected = (By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[2]/div[2]/div/div[1]/div/div[2]/div/div/div[2]/ul/li[5]')
    selectDropdown(driver, click_filter_status_claim_points,draft)
    selectDropdown(driver, click_filter_status_claim_points,waiting)
    selectDropdown(driver, click_filter_status_claim_points,approved)
    selectDropdown(driver, click_filter_status_claim_points,rejected)

# ======== point approval =============

    point_approval = (By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[2]/div[1]/span[4]')
    justClick(driver, point_approval)

    search_point_approval = (By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[2]/div[2]/div[1]/div/div[1]')
    justClick(driver, search_point_approval)

    input_search_pa = (By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[2]/div[2]/div[1]/div/div[1]/input')
    inputText(driver, input_search_pa, "test")

    close_search_pa = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#__nuxt > div > div > div.relative.flex.h-full.max-w-full.flex-1.overflow-auto > main > div > div > div.flex.w-full.flex-col.gap-4 > div.h-full.w-full.rounded-lg.bg-white.p-4 > div.flex.w-full.flex-col.justify-between.md\:inline-flex.md\:flex-row.md\:items-center > div > div.search-container.flex.cursor-pointer.items-center.justify-between.gap-2.rounded-full.bg-white.p-2.border.text-sm > svg.icon.close-icon.relative.h-5.w-5.text-gray-500'))
    )
    time.sleep(1)
    close_search_pa.click()

    click_filter_status_approved_pa = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[2]/div[2]/div[1]/div/div[2]/div/div'))
    )
    click_filter_status_approved_pa.click()
    time.sleep(1)
    approved_pa = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div[2]/ul/li[2]'))
    )
    ActionChains(driver).move_to_element(approved_pa).click().perform()
    time.sleep(1)

    click_filter_status_rejected_pa = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[2]/div[2]/div[1]/div/div[2]/div/div'))
    )
    click_filter_status_rejected_pa.click()
    time.sleep(1)
    rejected_pa = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div[2]/ul/li[3]'))
    )
    ActionChains(driver).move_to_element(rejected_pa).click().perform()
    time.sleep(1)

    click_filter_status_need_validation_pa = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[2]/div[2]/div[1]/div/div[2]/div/div'))
    )
    click_filter_status_need_validation_pa.click()
    time.sleep(1)
    need_validation_pa = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div[2]/ul/li[4]'))
    )
    ActionChains(driver).move_to_element(need_validation_pa).click().perform()
    time.sleep(1)

    click_filter_status_draft_pa = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[2]/div[2]/div[1]/div/div[2]/div/div'))
    )
    click_filter_status_draft_pa.click()
    time.sleep(1)
    need_draft_pa = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div[2]/ul/li[5]'))
    )
    ActionChains(driver).move_to_element(need_draft_pa).click().perform()
    time.sleep(1)

# ========== input point ============

    input_point = (By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[2]/div[1]/span[5]')
    justClick(driver, input_point)

    click_search_input_point = (By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[2]/div[2]/div/div[1]/div/div[1]')
    justClick(driver, click_search_input_point)

    input_search_ip = (By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[2]/div[2]/div/div[1]/div/div[1]/input')
    inputText(driver, input_search_ip, "test")

    close_search_ip = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#__nuxt > div > div > div.relative.flex.h-full.max-w-full.flex-1.overflow-auto > main > div > div > div.flex.w-full.flex-col.gap-4 > div.h-full.w-full.rounded-lg.bg-white.p-4 > div > div.inline-flex.items-center.justify-between.gap-2 > div > div.flex.max-w-full.cursor-pointer.items-center.justify-between.gap-2.rounded-full.bg-white.px-2\.5.md\:p-2.py-0.border > svg:nth-child(3)'))
    )
    time.sleep(1)
    close_search_ip.click()

    click_filter_status_draft_ip = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[2]/div[2]/div/div[1]/div/div[2]/div/div'))
    )
    click_filter_status_draft_ip.click()
    time.sleep(1)
    draft_ip = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[2]/div[2]/div/div[1]/div/div[2]/div/div/div[2]/ul/li[2]'))
    )
    ActionChains(driver).move_to_element(draft_ip).click().perform()
    time.sleep(1)

    click_filter_status_submitted = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[2]/div[2]/div/div[1]/div/div[2]/div/div'))
    )
    click_filter_status_submitted.click()
    time.sleep(1)
    submitted = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[2]/div[2]/div/div[1]/div/div[2]/div/div/div[2]/ul/li[3]'))
    )
    ActionChains(driver).move_to_element(submitted).click().perform()
    time.sleep(1)

    click_filter_status_revoke = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[2]/div[2]/div/div[1]/div/div[2]/div/div'))
    )
    click_filter_status_revoke.click()
    time.sleep(1)
    revoke = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[2]/div[2]/div/div[1]/div/div[2]/div/div/div[2]/ul/li[4]'))
    )
    ActionChains(driver).move_to_element(revoke).click().perform()
    time.sleep(1)

# ======= input point: add new point =============

    add_new_point = (By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[2]/div[2]/div/div[1]/div/a')
    justClick(driver, add_new_point)

    employee_name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[1]/div[2]/div/div/div/div/div[1]/input'))
    )
    employee_name.click()
    employee_name.send_keys("first")
    time.sleep(1)
    name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[1]/div[2]/div/div/div/div/div[2]/ul'))
    )
    ActionChains(driver).move_to_element(name).click().perform()

    gameplay = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[2]/div/div[1]/div/div/div[1]/input'))
    )
    gameplay.click()
    gameplay.send_keys("sele")
    time.sleep(1)
    search_gameplay = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[2]/div/div[1]/div/div/div[2]/ul'))
    )
    ActionChains(driver).move_to_element(search_gameplay).click().perform()

    option_click = (By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[2]/div/div[4]/div/div/div/div/div[1]/input')
    justClick(driver, option_click)

    save_as_draft = (By.XPATH, '/html/body/div/div/div/div[2]/main/div/footer/button[2]')
    justClick(driver, save_as_draft)

    just_click_ok = (By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div/div[2]/button')
    justClick(driver, just_click_ok)