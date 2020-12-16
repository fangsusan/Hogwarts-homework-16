import allure
import pytest
import yaml


@allure.feature("计算器测试模块")
class Test_Calc:

    def file_data():
        with open("./datas.yaml") as f:
            datas = yaml.safe_load(f)
            add_data = datas["add_datas"]
            sub_data = datas["sub_datas"]
            mul_data = datas["mul_datas"]
            div_data = datas["div_datas"]
            return [add_data,sub_data,mul_data,div_data]

    #   加法测试用例,第一执行
    @allure.story("加法测试用例")
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("a,b,expect",file_data()[0])
    # @pytest.fixture()
    def test_add(self,meilanzi,a,b,expect):
        assert meilanzi.add(a,b) == expect

    #   减法测试用例，最后执行
    @allure.story("减法测试用例")
    @pytest.mark.run(order=-1)
    @pytest.mark.parametrize("a,b,expect",file_data()[1])
    def test_sub(self,meilanzi,a,b,expect):
        # self.calc = Calculator()
        assert round(meilanzi.sub(a,b),2) == expect

    #  乘法测试用例，第三执行
    @pytest.mark.run(order=3)
    @allure.story("乘法测试用例")
    @pytest.mark.parametrize("a,b,expect",file_data()[2])
    def test_mul(self,meilanzi,a,b,expect):
        assert meilanzi.mul(a,b) == expect
    #
    #  除法测试用例，第二执行
    @pytest.mark.run(order=2)
    @allure.story("除法测试用例")
    @pytest.mark.parametrize("a,b,expect", file_data()[3])
    def test_div(self,meilanzi,a,b,expect):
        assert round(meilanzi.div(a, b)) == expect

