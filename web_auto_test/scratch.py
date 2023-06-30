# 导入selenium函数库
import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestScratch:
    def execute_script(self, i):
        # 每次执行滚动窗口，保证selenium找到对应链接
        length = 200 * i
        self.driver.execute_script(f"window.scrollTo(0,{length})")
        time.sleep(1)

    def scratch_ceshiren(self):
        # 进入网址
        self.driver.get("https://www.ceshiren.com/")
        # 点击搜索框
        self.driver.find_element(By.CSS_SELECTOR, '[class="fa d-icon d-icon-search svg-icon svg-node"]').click()
        # 选中高级搜索
        self.driver.find_element(By.CSS_SELECTOR, '[class="fa d-icon d-icon-sliders-h svg-icon svg-node"]').click()

        # 选中搜索页面的搜索框，输入搜索内容，并进入
        self.driver.find_element(By.CSS_SELECTOR, '[placeholder="搜索"]').click()
        self.driver.find_element(By.CSS_SELECTOR, '[placeholder="搜索"]').send_keys("selenium")
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, '[class="search-bar"] > [aria-label="搜索"]').click()
        time.sleep(1)

        for i in range(self.epoch):
            # 选择点击的元素
            self.driver.find_elements(By.CSS_SELECTOR, '[class="topic"] [class="search-link"]')[i].click()
            # 保存文本内容，注意不同页面的标签不同，使用不同的标签值定位
            try:
                self.htmls[i] = self.driver.find_element(By.CSS_SELECTOR, '[class="cooked inline-footnotes"]').text
            except:
                self.htmls[i] = self.driver.find_element(By.CSS_SELECTOR, '[class="cooked"]').text
            # time.sleep(2)
            self.driver.back()

            # 每次返回页面执行页面滚动，滚动值同i值变化
            self.execute_script(i)
            print(i)
            # print(htmls[i])
        time.sleep(1)

