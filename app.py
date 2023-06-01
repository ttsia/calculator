from flask import Flask, jsonify, request, render_template
from calculator.calculator import Calculator
from calculator.operator_registry import OperatorRegistry, OPERATORS_MAP
from calculator.shunting_yard import ShuntingYardAlgorithm

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()
    operands = map(float, data["operands"].split(","))
    operators = data["operators"]

    operators_registry = OperatorRegistry(OPERATORS_MAP)
    calculation_strategy = ShuntingYardAlgorithm(operators_registry)
    calculator = Calculator(calculation_strategy)
    result = calculator.calculate(operands, operators)

    color = "red" if result % 2 else "green"

    response = {"result": result, "color": color}

    return jsonify(response)


if __name__ == "__main__":
    app.run()
