def cache(func):
    def wrapper(n):
        if n not in wrapper.log.keys():
            wrapper.log[n] = func(n)
        return wrapper.log[n]
    wrapper.log = {}
    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(3))
print(fibonacci.log)
print(fibonacci(4))
print(fibonacci.log)
print(fibonacci(8))
print(fibonacci.log)
