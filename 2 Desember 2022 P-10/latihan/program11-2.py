n = int(input('Masukkan limit ke-n fibonacci : '))
i = 0
cache = {}


def fib(n):
    if n <= 1:
        return n
    if n not in cache:
        cache[n] = fib(n - 1) + fib(n - 2)
    return cache[n]


while (i <= n):
    print(f'fibonacci({i}) = {fib(i)}')
    i += 1
