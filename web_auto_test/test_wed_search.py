import time

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://www.ceshiren.com"
class TestWebSearch:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_search(self):
        with allure.step("测试网址"):
            self.driver.get(url)
        with allure.step("点击搜索框框"):
            self.driver.find_element(By.CSS_SELECTOR, '[title="搜索"]').click()
            self.driver.find_element(By.CSS_SELECTOR, '[title="打开高级搜索"]').click()

        with allure.step("选择搜索内容"):
            self.driver.find_element(By.CSS_SELECTOR, '[aria-label="筛选条件：所有类别"]').click()
            self.driver.find_element(By.CSS_SELECTOR, '[data-name="学习笔记"]').click()
            self.driver.find_element(By.CSS_SELECTOR, '[type="button"]').click()
            time.sleep(2)

        with allure.step("获取文本内容"):
            self.driver.find_elements(By.CSS_SELECTOR, '[class="topic"] [class="ember-view"]')[0].click()
            html = self.driver.find_element(By.CSS_SELECTOR, '[class="cooked"]').text
            self.driver.back()
            time.sleep(2)
        with allure.step("获取标题，进行测试"):
            name = self.driver.find_element(By.CSS_SELECTOR, '[class="topic"] [class="ember-view"]').text
            allure.attach(self.driver.get_screenshot_as_png(), name="搜索结果图",
                          attachment_type=allure.attachment_type.PNG)
            assert name == "Linux文件处理命令"

