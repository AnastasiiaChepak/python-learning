import pytest
import runpy

from finance_calculator import calculate_remaining, get_positive_number
from unittest.mock import Mock

@pytest.mark.parametrize(
    "salary, expenses, expected",
    [
        (2500, 800, 1700),
        (2500, 2500, 0),
        (2500, 3000, -500),
        (0, 2500, -2500),
        (2500, 0, 2500),
        (1000000, 999999, 1),
        (1000000000, 1000000000, 0)
    ],
)

def test_calculate_remaining(salary, expenses, expected):
    result = calculate_remaining(salary, expenses)
    assert result == expected

def test_get_positive_number_invalid_input(monkeypatch, capsys):
    inputs = iter(["abc", "100"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    result = get_positive_number("Enter a number: ")
    captured = capsys.readouterr()
    assert "Please enter a valid number." in captured.out
    assert result == 100

def test_get_positive_number_zero_input(monkeypatch, capsys):
    inputs = iter(["0", "100"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    result = get_positive_number("Enter a number: ")
    captured = capsys.readouterr()
    assert "Number must be greater than 0." in captured.out
    assert result == 100

def test_get_positive_number_negative_input(monkeypatch, capsys):
    inputs = iter(["-100", "100"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    result = get_positive_number("Enter a number: ")
    captured = capsys.readouterr()
    assert "Number must be greater than 0." in captured.out
    assert result == 100    

def test_calculate_remaining_invalid_type():
    with pytest.raises(TypeError):
        calculate_remaining(2500, "800")

def test_calculate_remaining_invalid_salary_type():
    with pytest.raises(TypeError):
        calculate_remaining("2500", 800)

def test_get_positive_number_decimal_input(monkeypatch, capsys):
    inputs = iter(["100.5", "100"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    result = get_positive_number("Enter a number: ")
    captured = capsys.readouterr()
    assert "Please enter a valid number." in captured.out
    assert result == 100

def test_get_positive_number_empty_input(monkeypatch, capsys):
    inputs = iter(["", "100"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    result = get_positive_number("Enter a number: ")
    captured = capsys.readouterr()
    assert "Please enter a valid number." in captured.out
    assert result == 100

def test_get_positive_number_multiple_invalid_inputs(monkeypatch, capsys):
    mock_input = Mock(side_effect=["abc", "0", "-50", "100"])
    monkeypatch.setattr("builtins.input", mock_input)
    result = get_positive_number("Enter a number: ")
    assert mock_input.call_count == 4
    captured = capsys.readouterr()
    assert "Please enter a valid number." in captured.out
    assert captured.out.count("Number must be greater than 0.") == 2
    assert result == 100

def test_main_positive_remaining(monkeypatch, capsys):
    inputs = iter(["2500", "800"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    runpy.run_path("finance_calculator.py", run_name="__main__")
    captured = capsys.readouterr()
    assert "You can save money." in captured.out

def test_main_zero_remaining(monkeypatch, capsys):
    inputs = iter(["2500", "2500"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    runpy.run_path("finance_calculator.py", run_name="__main__")
    captured = capsys.readouterr()
    assert "Your income and expenses are equal." in captured.out        

def test_main_negative_remaining(monkeypatch, capsys):
    inputs = iter(["2500", "3000"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    runpy.run_path("finance_calculator.py", run_name="__main__")
    captured = capsys.readouterr()
    assert "You are spending more than you earn." in captured.out
   