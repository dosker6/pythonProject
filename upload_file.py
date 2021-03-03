from selenium import webdriver
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_name('firstname')
    input1.send_keys('Ivan')
    input2 = browser.find_element_by_name('lastname')
    input2.send_keys('Ivanov')
    input3 = browser.find_element_by_name('email')
    input3.send_keys("пошелнахуй@ru")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "kkk.txt"# получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, file_name)  # добавляем к этому пути имя файла
    element = browser.find_element_by_id('file')
    element.send_keys(file_path)
    button = browser.find_element_by_class_name('btn').click()

finally:
    time.sleep(10)
    browser.quit()
