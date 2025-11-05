import pytest
from calc_v3 import add, subtract, multiply, divide, remainder, exponent, program


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
    assert divide(8, 4) == 2
    assert divide(-1, 1) == -1
    assert divide(5, 2) == 2.5
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)


def test_remainder():
    assert remainder(10, 3) == 1
    assert remainder(-1, 1) == 0
    assert remainder(5, 2) == 1


def test_exponent():
    assert exponent(2, 3) == 8
    assert exponent(-1, 1) == -1
    assert exponent(5, 0) == 1


def test_program_addition(monkeypatch, capsys):
    inputs = iter(["1", "2", "3", "no"])  # Simulate addition (1), num1=2, num2=3, then exit
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    program()
    captured = capsys.readouterr()
    assert "5" in captured.out  # Expecting output 2 + 3 = 5


def test_program_division(monkeypatch, capsys):
    inputs = iter(["4", "10", "2", "no"])  # Simulate division: 10 / 2
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    program()
    captured = capsys.readouterr()
    assert "5.0" in captured.out  # Expecting output 10 / 2 = 5.0


def test_program_exponent_and_remainder(monkeypatch, capsys):
    inputs = iter(["6", "2", "3", "yes", "5", "10", "3", "no"])  # Simulate multiple operations
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    program()
    captured = capsys.readouterr()
    assert "8" in captured.out  # Expect 2^3 = 8
    assert "1" in captured.out  # Expect 10 % 3 = 1


def test_invalid_choice(monkeypatch, capsys):
    inputs = iter(["7", "no"])  # Simulate invalid choice
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    program()
    captured = capsys.readouterr()
    assert "Invalid input" in captured.out  # Expect "Invalid input" message


def test_invalid_decision(monkeypatch, capsys):
    inputs = iter(["1", "2", "3", "maybe"])  # Simulate invalid decision
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    program()
    captured = capsys.readouterr()
    assert "Invalid input" in captured.out  # Expect "Invalid input" message