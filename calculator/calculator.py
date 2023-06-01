from typing import List


class Calculator:
    def __init__(self, calculation_strategy):
        self.calculation_strategy = calculation_strategy

    def calculate(self, operands: List[float], operators: List[str]) -> float:
        return self.calculation_strategy.execute(operands, operators)
