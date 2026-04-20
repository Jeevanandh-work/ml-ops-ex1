import pytest

from src.q2_palindrome import is_palindrome


def test_palindrome_odd_length_letters() -> None:
    assert is_palindrome("madam") is True


def test_palindrome_even_length_letters() -> None:
    assert is_palindrome("abba") is True


def test_palindrome_mixed_case_with_specials() -> None:
    assert is_palindrome("A man, a plan, a canal: Panama!") is True


def test_palindrome_digits() -> None:
    assert is_palindrome("12321") is True


def test_non_palindrome() -> None:
    assert is_palindrome("python") is False


def test_palindrome_non_string_raises_type_error() -> None:
    with pytest.raises(TypeError):
        is_palindrome(12321)  # type: ignore[arg-type]
