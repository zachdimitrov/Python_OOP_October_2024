def get_primes(numbers):
    for n in numbers:
        if n > 1:
            is_prime = True
            for i in range(2, (n//2) + 1):
                if n % i == 0:
                    is_prime = False
                    break
            if is_prime:
                yield n


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
print(list(get_primes([-2, 0, 0, 1, 1, 0])))
