from functools import reduce


class Calculator:

    @staticmethod
    def add(*args):
        return reduce((lambda x, y: x + y), args)

    @staticmethod
    def multiply(*args):
        return reduce((lambda x, y: x * y), args)

    @staticmethod
    def divide(*args):
        #try:
        return reduce((lambda x, y: x / y), args)
        #except ZeroDivisionError:
        #    return "Cannot divide by Zero"

    @staticmethod
    def subtract(*args):
        return reduce((lambda x, y: x - y), args)
