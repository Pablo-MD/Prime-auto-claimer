from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import GOG_Redeemer as GOG
import os
import time as tm

# Use a navegator with only one profile
# Make sure to have your twitch account previously logged in
# Make sure you have Twitch Prime
# Make sure to have your Twitch account Linked with your Epic Games account

firefox_options = Options()
firefox_profile_path = os.path.expanduser("~") + r"\AppData\Roaming\Mozilla\Firefox\Profiles\itj3da6i.default-release"
firefox_options.add_argument("-profile")
firefox_options.add_argument(firefox_profile_path)
driver = webdriver.Firefox(options=firefox_options)

firefox_options.set_preference("dom.webdriver.enabled", False)
firefox_options.set_preference('useAutomationExtension', False)


driver.implicitly_wait(5.0)

driver.get("https://www.twitch.tv/")

# presence_of_element_located(locator) definition:
# An expectation for checking that an element is present on the DOM of a page. 
# This does not necessarily mean that the element is visible. locator - used to find the element returns the WebElement once it is located

# element_to_be_clickable(locator):
# An Expectation for checking an element is visible and enabled such that you can click it.

prime = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[1]/nav/div/div[3]/div[2]/div/div/div[1]/div/div/button')))
prime.click()

primeElements = driver.find_elements(By.CLASS_NAME, 'prime-offer')
main_window =  driver.current_window_handle
for i in range(2, len(primeElements)):
    while len(driver.window_handles) > 1:
        driver.switch_to.window(driver.window_handles[-1])
        driver.close()
    try:
        tm.sleep(1)
        driver.switch_to.window(driver.window_handles[0])
        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'/html/body/div[4]/div/div/div/div/div/div/div/div[2]/div/div/div[3]/div/div/div[1]/div[2]/div[{i}]/div/div/div[2]/div[3]/div/div/a')))
        element.click()
        if (not element.is_enabled()):
            continue
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
        driver.switch_to.window(driver.window_handles[-1])
        getButton = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/main/div/div/div/div[1]/div[2]/div/div[2]/div[3]/div[2]/div/button')
        if(getButton.is_enabled()):
            getButton.click()
            key = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/main/div/div/div/div[1]/div/div[2]/div/div[3]/div/div[1]/div/div/div[1]/div/input').get_attribute('value')
            description = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/main/div/div/div/div[1]/div/div[2]/div/div[5]/div[1]/div[2]/div/div/div/div/div[1]/span/div/div/ol/li[1]/div')
            if 'GOG' in description.text:
                GOG.redeem(key)
        else:
            key = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/main/div/div/div/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/p').text.split(": ")[-1]
            description = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/main/div/div/div/div[2]/div[2]/div/div/div/div')
            if 'GOG' in description.text:
                GOG.redeem(key)
    except Exception as error:
        print(error)
        pass


from selenium.common.exceptions import NoSuchElementException
def check_exists_by_xpath(xpath):
    try:
        webdriver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

