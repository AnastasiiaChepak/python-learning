import runpy
from unittest.mock import Mock

import pytest

from finance_calculator import calculate_remaining, get_positive_number

@pytest.fixture
def input_values(request):
    return iter(request.param)

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

@pytest.mark.parametrize(
    "input_values, expected_message",
    [
        (["abc", "100"], "Please enter a valid number."),
        (["0", "100"], "Number must be greater than 0."),
        (["-100", "100"], "Number must be greater than 0."),
    ],
    indirect=["input_values"],
)
def test_get_positive_number_invalid_inputs(
    monkeypatch,
    capsys,
    input_values,
    expected_message,
):
    monkeypatch.setattr("builtins.input", lambda _: next(input_values))

    result = get_positive_number("Enter a number: ")
    captured = capsys.readouterr()

    assert expected_message in captured.out
    assert result == 100   

@pytest.mark.parametrize(
    "salary, expenses",
    [
        (2500, "800"),
        ("2500", 800),
    ],
)
def test_calculate_remaining_invalid_type(salary, expenses):
    with pytest.raises(TypeError):
        calculate_remaining(salary, expenses)

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

@pytest.mark.parametrize(
    "input_values, expected_message",
    [
        (["2500", "800"], "You can save money."),
        (["2500", "2500"], "Your income and expenses are equal."),
        (["2500", "3000"], "You are spending more than you earn."),
    ],
    indirect=["input_values"],
)
def test_main(input_values, expected_message, monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda _: next(input_values))

    runpy.run_path("finance_calculator.py", run_name="__main__")

    captured = capsys.readouterr()
    assert expected_message in captured.out
   