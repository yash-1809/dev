from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
test_cases = [
    {"username": "", "password": "7892aaa"},
    {"username": "yash", "password": ""},
    {"username": "qwertyu", "password": "asdfghjk"},
    {"username": "qazwsx", "password": "qazwsx"}
]
driver = webdriver.Chrome()
driver.get("http://127.0.0.1:5000")
for test in test_cases:
    driver.refresh()
    time.sleep(2)
    driver.find_element(By.ID, "username").send_keys(test["username"])
    driver.find_element(By.ID, "password").send_keys(test["password"])
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    try:
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert = Alert(driver)
        print("Alert Test:", alert.text)
        alert.accept()
    except:
        print("no alert appeared")
driver.quit()



# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time

# test_cases = [
#     {"num1": "20", "num2": "39"},
#     {"num1": "18", "num2": "27"},
#     {"num1": "18", "num2": "09"},
# ]

# driver = webdriver.Chrome()
# driver.get("D:\\Dev\\devops\\add.html")

# for test in test_cases:
#     driver.refresh()
#     time.sleep(1)
    
#     driver.find_element(By.ID,"num1").send_keys(test["num1"])
#     driver.find_element(By.ID,"num2").send_keys(test["num2"])
#     driver.find_element(By.CSS_SELECTOR,"button[type='button']").click()
#     time.sleep(3)
#     res = driver.find_element(By.ID,"res").text
#     print(res)
# driver.quit()