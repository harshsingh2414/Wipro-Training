import pytest
from src.calculation import Calculation

@pytest.fixture()
def calc():
    return Calculation
@pytest.mark.parametrize("n1,n2,exval", [(5,5,10),(-5,-5,-10),(0,5,5)])

def test_addition(calc, n1,n2,exval):
    assert calc.add(n1,n2) == exval, "addition error"

def test_subtraction(calc):

    assert calc.subtract(5, 3) == 2, "subtraction error"

def test_multiplication(calc):

    assert calc.multiply(3, 4) == 12, "multiplication error"

def test_division(calc):

    assert calc.divide(8, 2) == 4, "division error"

