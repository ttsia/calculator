from operator import add, mul, sub, truediv
from typing import Callable, Dict, Tuple


OPERATORS_MAP: Dict[str, Tuple[Callable[[float, float], float], int]] = {
    "+": (add, 1),
    "-": (sub, 1),
    "*": (mul, 2),
    "/": (truediv, 2),
}


class OperatorRegistry:
    def __init__(
        self, operators_map: Dict[str, Tuple[Callable[[float, float], float], int]]
    ):
        self.operators = operators_map

    def get_operator(self, operator: str) -> Callable[[float, float], float]:
        return self.operators.get(operator, (None, 0))[0]

    def get_precedence(self, operator: str) -> int:
        return self.operators.get(operator, (None, 0))[1]
