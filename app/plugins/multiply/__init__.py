
from app.commands import Command


class multiplyCommand(Command):
    def execute(self, x, y):
        return x * y
    