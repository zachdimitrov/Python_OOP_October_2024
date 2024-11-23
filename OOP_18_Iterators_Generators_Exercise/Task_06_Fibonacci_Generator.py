def fibonacci():
    a = 0
    yield a
    b = 1
    yield b
    while True:
        yield a + b
        c = a
        a = b
        b = c + b


generator = fibonacci()
for i in range(5):
    print(next(generator))
generator = fibonacci()
for i in range(1):
    print(next(generator))
