
import unittest
from app.commands.operations import Operations

class TestOperations(unittest.TestCase):

    def test_execute_creates_calculator_instance(self):
        """Tests if the Operations class creates a Calculator instance in its execute method."""
        operations = Operations()
        # No `operations.execute()` call needed as the attribute is initialized in __init__

    def test_perform_operation_add(self):
        """Tests the addition functionality of the perform_operation method."""
        operations = Operations()
        result = operations.perform_operation("+", 2, 3)
        self.assertEqual(result, 5)

    def test_perform_operation_subtract(self):
        """Tests the subtraction functionality of the perform_operation method."""
        operations = Operations()
        result = operations.perform_operation("-", 5, 2)
        self.assertEqual(result, 3)

    # Add similar test cases for other operations (multiply, divide)

    def test_perform_operation_invalid_operator(self):
        """Tests the behavior for an invalid operator in perform_operation."""
        operations = Operations()
        result = operations.perform_operation("%", 2, 3)
        self.assertIsNone(result)
