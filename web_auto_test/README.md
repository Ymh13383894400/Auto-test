代码内容

```
auto_test
    |-test_demo
        |-cal.py
        |-test_cal.py
    |-web_auto_test
    	|-scratch.py			#爬取网页内容
    	|-test_scratch.py		#测试爬取的标题
    	|-web_control.py		#selenium控制
    	|-web_locate.py			#selenium定位元素
    	|-web_search.py			#selenium自动化搜索
        |-test_web_search.py	#测试web搜索
        |-test_web_login.py		#测试web界面登录
        |-README.md
    |-interface_auto_test
    |-README.md
    |-requirments
```





## web 浏览器控制

|                 | 操作         | 使用场景            |
| --------------- | ------------ | ------------------- |
| get             | 打开浏览器   | web自动化测试第一步 |
| refresh         | 浏览器刷新   | 模拟                |
| back            | 浏览器回退   | 模拟                |
| maximize_window | 最大化浏览器 | 模拟                |
| minimize_window | 最小化浏览器 | 模拟                |

## 常见控件定位

- ID ：By.ID
- classname ：By.CLASS_NAME
- linktext ：By.LINK_TEXT
- name ：By.NAME 



#### CSS表达式

| 标识符                      | 描述                  |
| --------------------------- | --------------------- |
| #                           | 标签中id的属性值      |
| .                           | class的属性值         |
| [属性名='属性值']           | 标签中所有属性        |
| >                           | 表示父子关系          |
| 空格                        | 表示后代关系          |
| [属性名='属性值'] [名='值'] | CSS表达式后代关系用法 |

 **注意**：如果 class 属性值中包含多个值，且中间有空格，需要把空格改为 ‘.’ 



#### css调试方式

开发者工具中使用console查找CSS表达式是否唯一

- $('[ ]')



## 常见控件交互

| 操作     | 方法            |
| :------- | :-------------- |
| 点击     | click()         |
| 输入内容 | send_keys(‘值’) |
| 清空     | clear()         |

```bash
# 输入信息到输入框中
# 点击输入框
ele = driver.find_element(By.ID, 'query').click()
# 输入关键字
ele.send_keys("华北科技学院")
# 清空输入框
ele.clear()
```



## 强制等待与隐式等待

- 强制等待：导入sleep包，使用sleep(时间)
- 隐式等待：driver.implicitly_wait(3)，表示driver在三秒钟的时间内每0.5s检查一次是否获取了数据

## Allure 测试报告

#### 配置环境

- jdk环境
- 安装allure，并配置环境
- pip install 第三方库

 下载地址：[Index of /allure/](https://download.ceshiren.com/allure/)
解压下载后在path中配置allure bin目录的完整路径
![image](https://ceshiren.com/uploads/default/original/3X/f/0/f0ff4917c67e6e57b2252108758e2c2b19f99105.png) 

在pycharm中安装`allure-pytest`第三方库

- 运行用例生成报告数据：
  `pytest -vs 测试文件 --alluredir=./result`
- 生成在线报告：
  `allure serve ./result`
- 生成静态资源文件：
  1. `allure generate ./result` ===> Report successfully generated to **allure-report**
  2. `allure open ./allure-report`

#### allure 用法

```less
@allure.feature("模块名")
class TestTestsearch():
    def setup_method(self):
        self.driver = webdriver.Chrome()
        # 最大化窗口
        self.driver.maximize_window()
        # 添加隐式等待
        self.driver.implicitly_wait(3)

    def teardown_method(self):
        self.driver.quit()

    @allure.story("用例场景")
    @allure.title("用例标题")
    def test_testsearch(self):
        with allure.step("进入了搜狗搜索的页面"):
            self.driver.get("https://www.sogou.com/")
        self.driver.find_element(By.CSS_SELECTOR, ".sec-input-box").click()
        with allure.step("输入关键字"):
            self.driver.find_element(By.ID, "query").click()
            self.driver.find_element(By.ID, "query").send_keys("华北科技学院")
        with allure.step("点击搜索按钮"):
            self.driver.find_element(By.ID, "stb").click()
        time.sleep(5)
        assert self.driver.find_element(By.CSS_SELECTOR, ".vr-title > span").text == "华北科技学院"
```

#### allure 拓展–添加截图

用法：

```lua
allure.attach(self.driver.get_screenshot_as_png(), name="搜索结果图",
                          attachment_type=allure.attachment_type.PNG)

# 参数一：body=self.driver.get_screenshot_as_png()--->使用driver的生成截图方法得到一个图片
# 参数二：name="搜索结果图" --->  输入截图名称
# 参数三：attachment_type=allure.attachment_type.PNG ---> 设置图片后缀为PNG
```