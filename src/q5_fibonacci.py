def fibonacci_upto(limit: int) -> list[int]:
    """Return Fibonacci numbers less than or equal to limit."""
    if not isinstance(limit, int):
        raise TypeError("Input must be an integer")
    if limit < 0:
        raise ValueError("Limit must be non-negative")
    if limit == 0:
        return [0]

    sequence = [0, 1]
    while sequence[-1] + sequence[-2] <= limit:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence
