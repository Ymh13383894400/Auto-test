
#
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://ceshiren.com")

# 通过不同方式定位标签 LINK_TEXT
web_element_link = driver.find_element(By.LINK_TEXT,"热门")
print(web_element_link)

# class_name .属性值
web_element_class = driver.find_element(By.CLASS_NAME,"")
print(web_element_class)

# 元素定位出错，通过ctrl+F并且搜索Exception搜索异常问题

# ID定位 #属性值
# web_element_id = driver.find_element(By.ID,"")

#name定位
# web_element_name = driver.find_element(By.NAME,"")

# css [属性名='属性值']
# web_element_css = driver.find_element(By.CSS_SELECTOR,"")