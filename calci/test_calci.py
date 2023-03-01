    
import pytest
from fun import add, subtract, multiply, divide

def test_addition_positive():
    result = add(10, 2)
    assert result == 12

def test_addition_negative():
    result = add(-10, -2)
    assert result == -12

def test_subtraction_positive():
    result = subtract(12, 11)
    assert result == 1

def test_subtraction_negative():
    result = subtract(-2, -11)
    assert result == 9

def test_subtraction_negative_result():
    result = subtract(10, 11)
    assert result == -1.0

def test_multiplication():
    result = multiply(6, 1)
    assert result == 6.0

def test_multiplication_by_zero():
    result = multiply(6, 0)
    assert result == 0

def test_division_positive():
    result = divide(3, 2)
    assert result == 1.5

def test_division_negative():
    result = divide(4, -2)
    assert result == -2

def test_division_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        result = divide(7,0)
    assert "division by zero" in str(e.value)