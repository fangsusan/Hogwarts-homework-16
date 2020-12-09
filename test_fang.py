import pytest


def setup_module():
    print("======模块运行前，只执行一次=====")
def teardown_module():
    print("======模块运行后，只执行一次=====")

class TestFang(object):


    @classmethod
    def setup_class(cls):
        print("======类运行前，只执行一次=====")
    @classmethod
    def teardown_class(cls):
        print("======类运行后，只执行一次=====")

    def setup_method(self):
        print("======方法运行前，只执行一次=====")

    def teardown_method(self):
        print("======方运行后，只执行一次=====")

    @pytest.fixture()
    def test_one(self):
        print("======用例1，前置用例执行=====")

    def test_two(self):
        print("======用例2，第一个执行=====")å

    # @pytest.fixture()
    def test_three(self):
        print("======用例3，执行=====")

    def test_four(self):
        print("======用例4，执行=====")









