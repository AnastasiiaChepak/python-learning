import pytest

from finance_calculator import calculate_remaining, get_positive_number

@pytest.mark.parametrize(
    "salary, expenses, expected",
    [
        (2500, 800, 1700),
        (2500, 2500, 0),
        (2500, 3000, -500),
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
   