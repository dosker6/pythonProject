from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time


try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector("#num1")
    x = x_element.text
    y_element = browser.find_element_by_css_selector('#num2')
    y = y_element.text
    sum_el = str(int(x)+int(y))
    select = Select(browser.find_element_by_css_selector("#dropdown"))
    select.select_by_visible_text(sum_el)
    input1 = browser.find_element_by_class_name('btn').click()

finally:
    time.sleep (5)
    browser.quit()
