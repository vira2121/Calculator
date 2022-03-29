import Calculator
import pytest

@pytest.mark.parametrize("a,b,c",[(3,2,5),(4,2,6),(5,5,10),(5,5,9)])
def test_add(a,b,c):
    # x=10
    # y=20
    r=Calculator.add(a,b)
    assert r == c

@pytest.mark.parametrize("a,b,c",[(3,2,1),(4,2,2),(5,5,0),(5,5,9)])
def test_sub(a,b,c):
    # x=10
    # y=20
    r=Calculator.sub(a, b)
    assert r == c

@pytest.mark.parametrize("a,b,c",[(3,2,6),(4,2,8),(5,5,25),(5,5,9)])
def test_mult(a,b,c):
    # x=10
    # y=20
    r=Calculator.mult(a, b)
    assert r == c

@pytest.mark.parametrize("a,b,c",[(3,2,1.5),(4,2,2),(5,5,1),(5,5,9)])
def test_div(a,b,c):
    # x=10
    # y=20
    r=Calculator.div(a, b)
    assert r == c