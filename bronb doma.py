from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    sell = WebDriverWait(browser, 25).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    button1 = browser.find_element_by_id('book').click()
    button2 = browser.find_element_by_id('solve')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button2)
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    input = browser.find_element_by_id('answer').send_keys(y)
    button3 = browser.find_element_by_id('solve').click()

finally:
    time.sleep(5)
    browser.quit()