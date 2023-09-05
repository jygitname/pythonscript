import pytest

from python.Calc import Calc


class TestCalc:
    def setup(self):
        self.calc = Calc()

@pytest.mark.parametrize(('a','b','c'),[(3,4,7),(2.5,3.6,7.1)])
def testAdd(self,a,b,c):
        r=self.calc.calc_add(a,b)
        assert r==c


@pytest.mark.parametrize(('d','e','f'),[(6,3,2),(7,2,3.5)])
def testDiv(self,d,e,f):
        m=self.calc.calc_div(d,e)
        assert m==f
pytest.main()

