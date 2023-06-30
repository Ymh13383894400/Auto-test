# 导入selenium函数库
import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

htmls = [
    'selenium-Selenium 1 (Selenium RC)',
    'selenium-The Selenium Browser Automation Project',
    'selenium-Selenium 浏览器自动化项目'
]


@allure.feature("'https://www.ceshiren.com'网址内容搜索测试")
class TestWebSearch:
    def setup_method(self):
        # 打开浏览器
        self.epoch = 3
        self.htmls = ['1', '2', '3', '4', '5']
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def teardown_method(self):
        self.driver.quit()


    @allure.title("爬取页面内容功能测试")
    @pytest.mark.parametrize('result', htmls)
    def test_scratch(self, result):
        with allure.step("进入网页，打开搜索链接"):
            # 进入网址
            self.driver.get("https://www.ceshiren.com/")
            # 点击搜索框
            self.driver.find_element(By.CSS_SELECTOR, '[class="fa d-icon d-icon-search svg-icon svg-node"]').click()
            # 选中高级搜索
            self.driver.find_element(By.CSS_SELECTOR, '[class="fa d-icon d-icon-sliders-h svg-icon svg-node"]').click()

        with allure.step("选中搜索内容，并且搜索"):
            # 选中搜索页面的搜索框，输入搜索内容，并进入
            self.driver.find_element(By.CSS_SELECTOR, '[placeholder="搜索"]').click()
            self.driver.find_element(By.CSS_SELECTOR, '[placeholder="搜索"]').send_keys("selenium")
            time.sleep(1)
            self.driver.find_element(By.CSS_SELECTOR, '[class="search-bar"] > [aria-label="搜索"]').click()
            time.sleep(1)

        with allure.step("获取搜索页面内容"):
            # 选择点击的元素
            els = self.driver.find_elements(By.CSS_SELECTOR, '[class="topic"] [class="search-link"]')
            all_result = [x.text for x in els]
            allure.attach(self.driver.get_screenshot_as_png(), name="搜索结果图", attachment_type=allure.attachment_type.PNG)
            assert result in all_result