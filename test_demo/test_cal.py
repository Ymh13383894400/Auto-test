import allure
import pytest
from calculator import Calculator

'''pytest 命令行指定用例执行方式
运行当前目录下所有符合收集规则的用例：执行 pytest
运行当前目录下 某个测试文件 执行： pytest xxx.py
运行当前目录下 某个测试类 执行： pytest xxx.py::类名
运行当前目录下 某个测试用例 执行： pytest xxx.py::类名::方法名

展示用例执行过程
pytest -vs 文件名。。

标记测试用例函数
@pytest.mark.div
pytest -m "div"

测试用例传递
@pytest.mark.parametrize('变量名',变量值)
def add(self, 变量名):
    ...
'''

@allure.feature("加法和除法测试")
# 测试模块
class TestCal:
    # 方法级别，前置动作，一般用于初始化赋值工作，每个函数最开始都会执行一次
    def setup(self):
        self.cal = Calculator()
        pass
    # 一般用于结尾清理工作
    def teardown(self):
        pass

    # 类级别前置动作
    def setup_class(self):
        pass
    def teardown_class(self):
        pass

    @allure.title("测试加法搜索")
    @allure.story("第一种测试用例")
    # 通过pytest将测试用例传入函数中
    @pytest.mark.parametrize('num1, num2',[
        [100, 20],
        [20, 30],
        [30, 40],
        [40, 50]
    ])
    def test_add(self, num1, num2):     # 每条的测试用例设计,变量通过列表对传入到函数自变量中
        res = self.cal.add(num1,num2)
        assert res == num1+num2

    @allure.story("第一种测试用例")
    @pytest.mark.div
    @pytest.mark.parametrize('num1, num2',[
        [100, 20],
        [20, 30],
        [30, 40],
        [40, 50]
    ])
    def test_div(self, num1, num2):
        res = self.cal.div(num1,num2)
        assert res == num1/num2


@allure.feature("矩阵加法测试")
class TestMat:
    def setup(self):
        pass
    def teardown_class(self):
        pass

    # @allure.title("用例标题")
    # @allure.story("用例场景")
    @allure.story("第一种测试用例")
    def test_add(self):
        print("第二个测试类的add方法")


