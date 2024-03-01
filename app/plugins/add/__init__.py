import sys
from app.commands import Command


class addCommand(Command):
    def execute(self, x, y):
        return x + y
    