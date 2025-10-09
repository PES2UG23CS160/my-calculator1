"""
Command Line Interface for Calculator
Example: python src/cli.py add 5 3
"""

import sys
import click
from calculator import add, subtract, multiply, divide, power, square_root

@click.command()
@click.argument("operation")
@click.argument("num1", type=float)
@click.argument("num2", type=float, required=False)
def calculate(operation, num1, num2=None):
    """Simple calculator CLI"""

    try:
        # Unary operations
        if operation in ["square_root", "sqrt"]:
            result = square_root(num1)

        # Binary operations
        else:
            if num2 is None:
                click.echo("Error: This operation requires two numbers.")
                sys.exit(1)

            if operation == "add":
                result = add(num1, num2)
            elif operation == "subtract":
                result = subtract(num1, num2)
            elif operation == "multiply":
                result = multiply(num1, num2)
            elif operation == "divide":
                result = divide(num1, num2)
            elif operation == "power":
                result = power(num1, num2)
            else:
                click.echo(f"Unknown operation: {operation}")
                sys.exit(1)

        click.echo(f"Result: {result}")

    except ZeroDivisionError:
        click.echo("Error: Division by zero is not allowed.")
        sys.exit(1)
    except Exception as e:
        click.echo(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    # Pylint false positive: Click injects args at runtime
    calculate()  # pylint: disable=no-value-for-parameter
