
def fibonacci(n: int, fib_cache: dict[int, int] = {0: 0, 1: 1}) -> int:
    if n <= 1:
        return n
    #check if already calc this num.
    if n in fib_cache:
        return fib_cache[n]
    # if not in cache, calculate it, store it, and return
    fib_cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return fib_cache[n]
