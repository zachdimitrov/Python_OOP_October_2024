class store_results:
    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        with open("results.txt", "a+") as file:
            name = self.function.__name__
            result = self.function(*args, **kwargs)
            file.write(f"Function \"{name}\" was called. Result {result}\n")

        return result


@store_results
def add(a, b):
    return a + b


@store_results
def mult(a, b):
    return a * b


add(2, 2)
mult(6, 4)
