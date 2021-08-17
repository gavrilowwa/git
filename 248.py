from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
try:

    link = "http://suninjuly.github.io/explicit_wait2.html"
    driver = webdriver.Chrome()
    driver.get(link)
    WebDriverWait(driver, 13).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    driver.find_element_by_xpath("//button[@id='book']").click()

    button = driver.find_element_by_xpath("//button[@type='submit']")
    driver.execute_script("return arguments[0].scrollIntoView(true);", button)

    x_element = driver.find_element_by_xpath("//span[@id='input_value']")
    x = x_element.text
    y = calc(x)
    driver.find_element_by_css_selector("[id='answer']").send_keys(y)
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    driver.quit()