from selenium import webdriver
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element_by_id('answer').send_keys(y)
    checkbox_robot = browser.find_element_by_css_selector('#robotCheckbox').click()
    button = browser.find_element_by_css_selector('#robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    button2 = browser.find_element_by_class_name('btn').click()


finally :
    time.sleep(10)
    browser.quit()