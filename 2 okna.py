import math
import time

from selenium import webdriver


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    first_window = browser.window_handles[0]
    button1 = browser.find_element_by_class_name('btn').click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    input = browser.find_element_by_id('answer').send_keys(y)
    button2 = browser.find_element_by_class_name('btn').click()
   



finally:
    time.sleep(5)
    browser.quit()