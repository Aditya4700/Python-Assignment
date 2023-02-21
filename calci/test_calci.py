import pytest
from fun import add,subtract,multiply,divide
def test_add():
    value = add(10, 2)
    assert value == 12
    
def test_addi():
    value = add(-10, -2)
    assert value == -12


def test_subtract():
    value = subtract(12, 11)
    assert value == 1
    
def test_subtracti():
    value = subtract(-2, -11)
    assert value == 9


def test_subtract_negative():
    value = subtract(10, 11)
    assert value == -1.0


def test_multiply():
    value = multiply(6, 1)
    assert value == 6.0

def test_multipli():
    value = multiply(6, 0)
    assert value == 0


def test_divide():
    value = divide(3, 2)
    assert value == 1.5

def test_divisi():
    value = divide(4, -2)
    assert value == -2
    
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        value=divide(7,0)
    assert "division by zero" in str(e.value)    