def factorial(n: int) -> int:
    """Return n! for a non-negative integer n.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is negative.
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Factorial is undefined for negative numbers")

    result = 1
    for value in range(2, n + 1):
        result *= value
    return result
