import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.sogou.com")

# 隐式等待3秒
driver.implicitly_wait(3)

web_element_sent = driver.find_element(By.ID, 'query')
# 点击输入框
web_element_sent.click()
# 输入关键字
web_element_sent.send_keys("清华大学")
time.sleep(1)
# 点击搜索的id标签
web_element_sent = driver.find_element(By.ID, 'stb').click()

time.sleep(2)
# 清空输入框
driver.quit()