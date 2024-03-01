'''def add(x, y):
  """Adds two numbers together.

  Args:
      x: The first number.
      y: The second number.

  Returns:
      The sum of x and y.
  """
  return x + y

def subtract(x, y):
  """Subtracts one number from another.

  Args:
      x: The first number.
      y: The second number.

  Returns:
      The difference of x and y.
  """
  return x - y

def multiply(x, y):
  """Multiplies two numbers together.

  Args:
      x: The first number.
      y: The second number.

  Returns:
      The product of x and y.
  """
  return x * y

def divide(x, y):
  """Divides one number by another.

  Args:
      x: The first number (dividend).
      y: The second number (divisor).

  Returns:
      The quotient of x and y, or None if y is zero.
  """
  if y == 0:
    return None
  return x / y'''

class Calculator:
  def add(self, x, y):
    return x + y

  def subtract(self, x, y):
    return x - y

  def multiply(self, x, y):
    return x * y

  def divide(self, x, y):
    if y == 0:
      return None
    return x / y
