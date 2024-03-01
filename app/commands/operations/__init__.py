'''from calculator import add, subtract, multiply, divide



def perform_operation(operator, x, y):
  """Performs a mathematical operation on two numbers.

  Args:
      operator: The mathematical operation to perform (add, subtract, multiply, divide).
      x: The first number.
      y: The second number.

  Returns:
      The result of the operation, or None if the operation is invalid.
  """
  if operator == "+":
    return add(x, y)
  elif operator == "-":
    return subtract(x, y)
  elif operator == "*":
    return multiply(x, y)
  elif operator == "/":
    return divide(x, y)
  else:
    return None
'''

from app.commands.calculator import Calculator

class Operations:
  def __init__(self):
    self.calculator = Calculator()

  def perform_operation(self, operator, x, y):
    if operator == "+":
      return self.calculator.add(x, y)
    elif operator == "-":
      return self.calculator.subtract(x, y)
    elif operator == "*":
      return self.calculator.multiply(x, y)
    elif operator == "/":
      return self.calculator.divide(x, y)
    else:
      return None
