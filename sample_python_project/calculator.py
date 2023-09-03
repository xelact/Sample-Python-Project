"""A simple calculator module."""


class Calculator:
    """A simple calculator class.

    :param num1: The first number
    :param num2: The second number
    """

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        """Add two numbers together.

        :return: The sum of the two numbers
        """
        return self.num1 + self.num2
