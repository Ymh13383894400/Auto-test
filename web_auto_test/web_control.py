#
import time

# 初始化driver
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

# 打开网页
driver.get("https://www.ceshiren.com")

time.sleep(1)
# 刷新浏览器页面
driver.refresh()

# 回退/选择子页面
driver.find_element(By.CSS_SELECTOR, '')
time.sleep(1)
driver.back()
time.sleep(1)

driver.minimize_window()

# 关闭浏览器
driver.quit()
