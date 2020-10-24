import pytest

from pythoncode.calculator import Calculator

def test_a():
    print("test case a")

class TestCalc:
    def setup_class(self):
        print("计算开始")
        self.calc = Calculator()

    def teardown_class(self):
        print("计算结束")

    @pytest.mark.parametrize('a,b,expect',
        [
            [1, 1, 2],
            [100, 100, 200],
            [0.1, 0.1, 0.2],
            [-1, -1, -2],
            [1, 0, 1],
            [-1, 1, 0],
            [0.9999999999, 0, 0.9999999999],
            [-1.1, 1, -0.1]

        ]
        #, ids=['int_case','bignum_case','flast_case','minus_case','zero_case']
    )
    def test_add(self, a, b, expect):
        result = self.calc.add(a, b)
        assert result == expect



    @pytest.mark.parametrize('a,b,expect',
            [
                [100, 100, 1],
                [100, -1, -100],
                [1, 0, ''],
                [0, 100, 0],
                [0.1, 0.2, 0.5],
                [0.1, 0.02, 5],
                [-1, -1, 1],
                [1, 3, 0.3],
                [1, '', 0.3]

            ]
            # , ids=['整数相除','整数除以负数','除数为0','被除数为0','小数相除','小数相除为整数','负负得正','除不尽']
                             )
    def test_dev(self,a,b,expect):
        result=self.calc.div(a,b)
        assert result == expect
    # def test_add1(self):

    #     #calc=Calculator()
    #     result = self.calc.add(100,100)
    #     assert result == 200
    #
    # def test_add2(self):
    #     #calc=Calculator()
    #     result = self.calc.add(0.1,0.1)
    #     assert result == 0.2