from app.commands.operations import Operations

class CalculatorCommand:
  def __init__(self, operations: Operations):
    self.operations = operations

  def execute(self, command_input):
    """
    Parses user input, extracts operator and operands, and performs the calculation.

    Args:
      command_input: String containing the user's input (e.g., "add 1 3").

    Returns:
      The result of the calculation or None if the input is invalid.
    """
    try:
      operator, *operands = command_input.lower().split()  # Split into operator and operands
      x, y = map(float, operands)  # Convert operands to numbers
      return self.operations.perform_operation(operator, x, y)
    except (ValueError, TypeError):
      print("Invalid input. Please enter a valid expression (e.g., add 2 3).")
      return None