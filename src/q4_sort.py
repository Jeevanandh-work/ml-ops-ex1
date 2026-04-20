def sort_integers(values: list[int]) -> list[int]:
    """Return a new list of integers sorted in ascending order."""
    if not isinstance(values, list):
        raise TypeError("Input must be a list")
    if not all(isinstance(item, int) for item in values):
        raise TypeError("All items in the list must be integers")

    return sorted(values)
