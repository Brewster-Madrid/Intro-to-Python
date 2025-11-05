import pytest
from unittest.mock import patch
import importlib
import calc_v1

importlib.reload(calc_v1)

from calc_v1 import add, subtract, multiply, divide, remainder, exponent, program


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2


def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(-1, 1) == -2
    assert subtract(-1, -1) == 0


def test_multiply():
    assert multiply(3, 7) == 21
    assert multiply(-1, 1) == -1
    assert multiply(-1, -1) == 1


def test_divide():
    assert divide(10, 2) == 5
    assert divide(-1, 1) == -1
    assert divide(-1, -1) == 1
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)


def test_remainder():
    assert remainder(10, 3) == 1
    assert remainder(-1, 1) == 0
    assert remainder(-1, -1) == 0


def test_exponent():
    assert exponent(2, 3) == 8
    assert exponent(-1, 1) == -1
    assert exponent(-1, -1) == -1


@patch("builtins.input", side_effect=["1", "5", "3"])  # Mock user input: choice=1, num1=5, num2=3
@patch("builtins.print")  # Mock print to capture output
def test_program_addition(mock_print, mock_input):
    program()  # Run the program function
    mock_print.assert_called_with(8)  # Since add(5,3) should return 8, assert this was printed