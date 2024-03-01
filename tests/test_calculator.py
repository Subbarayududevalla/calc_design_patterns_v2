import unittest
from app.commands.calculator import Calculator
import unittest

class TestCalculator(unittest.TestCase):

  def test_add(self):
    """Tests the addition functionality of the Calculator class."""
    calculator = Calculator()
    result = calculator.add(2, 3)
    self.assertEqual(result, 5)

  def test_subtract(self):
    """Tests the subtraction functionality of the Calculator class."""
    calculator = Calculator()
    result = calculator.subtract(5, 2)
    self.assertEqual(result, 3)

  def test_multiply(self):
    """Tests the multiplication functionality of the Calculator class."""
    calculator = Calculator()
    result = calculator.multiply(2, 4)
    self.assertEqual(result, 8)

  def test_divide_by_zero(self):
    """Tests the division by zero behavior of the Calculator class."""
    calculator = Calculator()
    result = calculator.divide(10, 0)
    self.assertIsNone(result)

  def test_divide(self):
    """Tests the division functionality of the Calculator class."""
    calculator = Calculator()
    result = calculator.divide(6, 2)
    self.assertEqual(result, 3)

if __name__ == "__main__":
  unittest.main()

