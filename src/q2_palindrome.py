def is_palindrome(text: str) -> bool:
    """Check palindrome status ignoring case and non-alphanumeric characters."""
    if not isinstance(text, str):
        raise TypeError("Input must be a string")

    normalized = "".join(char.lower() for char in text if char.isalnum())
    return normalized == normalized[::-1]
