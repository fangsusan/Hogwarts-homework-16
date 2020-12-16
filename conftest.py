import pytest

from Pythoncode.calculator import Calculator


@pytest.fixture(scope="module")
def meilanzi():
    calc = Calculator()
    print("====计算开始====")
    yield calc
    print("====计算结束====")
