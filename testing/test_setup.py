

def setup_module():
    print("setup_module")

def teardown_module():
    print("teardown_module")

def test_case1():
    print("case1")


def setup_function():
    print("资源准备 setup function")

def teardown_function():
    print("资源销毁 teardown_function")


class TestDemo:

    #执行类前后分别执行 setup_class teardown_class
    def setup_class(self):
        print("testdemo setup_class")

    def teardown_class(self):
        print("testdemo teardown_class")
#每个类里面的方法分别执行setup teardown
    def setup(self):
        print("testdemo setup")

    def teardown(self):
        print("testdemo teardown")

    def test_demp1(self):
        print("test demo1")
    def test_demo2(self):
        print("test demo2")

class TestDemo1:

    #执行类前后分别执行 setup_class teardown_class
    def setup_class(self):
        print("testdemo1 setup_class")

    def teardown_class(self):
        print("testdemo1 teardown_class")
#每个类里面的方法分别执行setup teardown
    def setup(self):
        print("testdemo1 setup")

    def teardown(self):
        print("testdemo1 teardown")

    def test_demp1(self):
        print("test demo1")
    def test_demo2(self):
        print("test demo2")