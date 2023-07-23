from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")
    submit = browser.find_element(By.XPATH, '/html/body/form/div/div/button').click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element(By.XPATH, '//*[@id="answer"]')
    input1.send_keys(y)
    submit1 = browser.find_element(By.XPATH, '/html/body/form/div/div/button').click()
finally:
    time.sleep(50)
    browser.quit()

