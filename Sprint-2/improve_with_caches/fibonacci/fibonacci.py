def fibonacci(n, cache=None):
    if cache is None:
        cache = {0: 0, 1: 1}

    if n in cache:
        return cache[n]

    cache[n] = fibonacci(n - 1, cache) + fibonacci(n - 2, cache)

    return cache[n]