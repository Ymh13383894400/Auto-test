import time
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
usr = 'manage'
pwd = 'manage123'
url = 'https://litemall.hogwarts.ceshiren.com/'

class TestWebLogin():
    def setup_method(self):
        self.web = webdriver.Chrome()
        self.web.maximize_window()

    def teardown_methed(self):
        self.web.close()

    def test_login(self):
        with allure.step('进入登入页面'):
            self.web.get(url)
        allure.attach(self.web.get_screenshot_as_png(), name="登入页面", attachment_type=allure.attachment_type.PNG)
        with allure.step('输入账号密码'):
            el1 = self.web.find_element(By.XPATH,'//*[@id="app"]/div/form/div[2]/div/div/input')
            el1.clear()
            el1.send_keys(usr)
            el2 = self.web.find_element(By.XPATH,'//*[@id="app"]/div/form/div[3]/div/div/input')
            el2.clear()
            el2.send_keys(pwd)
        with allure.step('登入'):
            self.web.find_element(By.XPATH,'//*[@id="app"]/div/form/button/span').click()
            time.sleep(5)
        allure.attach(self.web.get_screenshot_as_png(), name="用户页面", attachment_type=allure.attachment_type.PNG)
        assert self.web.find_element(By.XPATH,'//*[@id="tags-view-container"]/div/div[1]/div/span').text == '首页'

if __name__ == '__main__':
    pytest.main()