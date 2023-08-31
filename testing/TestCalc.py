import pytest

from python.Calc import Calc


class TestCalc():
    def setup(self):
        self.calc = Calc()
@pytest.mark.parametrize('a','b','c',[()])
    def testAdd(self):
        r=self.calc.calc_add(3,4)
        assert 7==r

    def testDiv(self):
        d=self.calc.calc_div(6,3)
        assert 2==d

if __name__ == "__main__" :
    pytest.main(['-vs','TestCalc.py::TestCalc::testDiv'])
