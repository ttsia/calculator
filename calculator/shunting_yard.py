from itertools import zip_longest
from typing import List, Union
from .operator_registry import OperatorRegistry


class ShuntingYardAlgorithm:
    def __init__(self, operators_registry: OperatorRegistry):
        self._operators_registry = operators_registry

    def _convert_to_rpn(self, operands: List[float], operators: List[str]) -> List[str]:
        output_queue: List[str] = []
        operator_stack: List[str] = []

        for operand, operator in zip_longest(operands, operators, fillvalue=""):
            if operand:
                output_queue.append(str(operand))

            if operator:
                # While there are operators on the stack with greater precedence, pop them to the output queue
                while operator_stack and self._operators_registry.get_precedence(
                    operator
                ) <= self._operators_registry.get_precedence(operator_stack[-1]):
                    output_queue.append(operator_stack.pop())
                operator_stack.append(operator)

        # Pop any remaining operators from the stack to the output queue
        output_queue.extend(operator_stack[::-1])
        return output_queue

    def _evaluate_rpn_expression(self, rpn_expression: List[str]) -> float:
        operand_stack: List[Union[float, int]] = []

        for token in rpn_expression:
            if token in self._operators_registry.operators:
                # If the token is an operator, pop two operands from the stack, perform the operation, and push the result back to the stack
                right_operand = operand_stack.pop()
                left_operand = operand_stack.pop()
                operation = self._operators_registry.get_operator(token)
                result = operation(left_operand, right_operand)
                operand_stack.append(result)
            else:
                # If the token is an operand, push it to the stack
                operand_stack.append(float(token))

        return operand_stack[0]

    def execute(self, operands: List[float], operators: List[str]) -> float:
        rpn_expression = self._convert_to_rpn(operands, operators)
        return self._evaluate_rpn_expression(rpn_expression)
