from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    driver = webdriver.Chrome()
    driver.get(link)

    # Ваш код, который заполняет обязательные поля
    button = driver.find_element_by_xpath("//button[@type='submit']").click()
    
    new_window = driver.window_handles[1]
    print(new_window)
    driver.switch_to.window(new_window)


    x_element = driver.find_element_by_xpath("//span[@id='input_value']")
    x = x_element.text
    y = calc(x)

    option1 = driver.find_element_by_css_selector("[id='answer']").send_keys(y)
    driver.find_element_by_xpath("//button[@type='submit']").click()

    time.sleep(1)
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    driver.quit()