import pytest
from calculator.calculator import Calculator
from calculator.shunting_yard import ShuntingYardAlgorithm
from calculator.operator_registry import OperatorRegistry
from operator import add, sub, mul, truediv

OPERATORS_MAP = {
    "+": (add, 1),
    "-": (sub, 1),
    "*": (mul, 2),
    "/": (truediv, 2),
}


@pytest.fixture
def calculator():
    operators_registry = OperatorRegistry(OPERATORS_MAP)
    converter = ShuntingYardAlgorithm(operators_registry)
    return Calculator(converter)


def test_addition(calculator):
    operands = [2, 3]
    operators = ["+"]
    result = calculator.calculate(operands, operators)
    assert result == 5


def test_subtraction(calculator):
    operands = [5, 3]
    operators = ["-"]
    result = calculator.calculate(operands, operators)
    assert result == 2


def test_multiplication(calculator):
    operands = [4, 5]
    operators = ["*"]
    result = calculator.calculate(operands, operators)
    assert result == 20


def test_division(calculator):
    operands = [10, 2]
    operators = ["/"]
    result = calculator.calculate(operands, operators)
    assert result == 5
