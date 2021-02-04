def fibonacci(n):
    if n < 0:
        raise ValueError("n must be >= 0")
    if not isinstance(n, int):
        raise ValueError("n must be exact integer")
    if n+1 == n:  # catch a value like 1e300
        raise OverflowError("n too large")
    if n <= 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
