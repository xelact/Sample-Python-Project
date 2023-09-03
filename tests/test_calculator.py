"""Test the Calculator class."""
from sample_python_project.calculator import Calculator


class TestAddition:
    def test_addition(self):
        calculator = Calculator(2, 3)
        assert calculator.add() == 5
