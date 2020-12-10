import pytest

from Pythoncode.calculator import Calculator


class Test_Calc:

    def setup_class(self):
        self.calc = Calculator()
        print("计算开始")

    def teardown_class(self):
        print("计算结束")

    #   加法测试用例
    @pytest.mark.parametrize("a,b,expect",[(1,3,4),(-1,-3,-4),(0.3,0.5,0.8),(1000,2000,3000)])
    def test_add(self,a,b,expect):
        assert self.calc.add(a,b) == expect

    #   减法测试用例
    @pytest.mark.parametrize("a,b,expect",[(4,3,1),(-4,-1,-3),(3000,2000,1000)])
    def test_sub(self,a,b,expect):
        assert self.calc.sub(a,b) == expect

    # 减法测试用例特例 保留两位小数
    @pytest.mark.parametrize("a,b,expect",[(-4, -1, -3), (0.8, 0.5, 0.3)])
    def test_sub(self, a, b, expect):
        expect1 = self.calc.sub(a,b)
        assert round(expect1,1) == expect

    #  乘法测试用例
    @pytest.mark.parametrize("a,b,expect",[(1,3,3),(-1,-3,3),(0.3,0.5,0.15),(1000,2000,2000000)])
    def test_mul(self,a,b,expect):
        assert self.calc.mul(a,b) == expect

    #     除法测试用例
    @pytest.mark.parametrize("a,b,expect", [(4, 2, 2),(-4, -2, 2),(2000, 1000, 2)])
    def test_div(self, a, b, expect):
        assert self.calc.div(a, b) == expect

    #     除法测试用例-特例 保留小数位两位
    @pytest.mark.parametrize("a,b,expect", [(0.08,0.4,0.2), (20,100,0.2)])
    def test_div(self, a, b, expect):
        diva = self.calc.div(a, b)
        assert round(diva,2) == expect

