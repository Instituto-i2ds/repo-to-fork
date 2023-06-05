def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib = [0, 1]
        for i in range(2, n):
            fib.append(fib[i-1] + fib[i-2])
        return fib

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def primeList(N):
    
    primes = []
    for i in range(2, N):
        if is_prime(i):
            primes.append(i)
    return primes


if __name__ == '__main__':
    print(f'fibonacci : {fibonacci(15)}')
    print(f'primos: {primeList(50)}')
