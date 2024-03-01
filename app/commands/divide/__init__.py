import sys
from app.commands import Command


class divideCommand(Command):
    def execute(self, x, y):
        return x / y
    sys.exit("Exiting...")