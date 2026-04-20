import pytest

from src.q3_prime import is_prime


def test_known_prime_numbers() -> None:
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(29) is True


def test_known_non_prime_numbers() -> None:
    assert is_prime(4) is False
    assert is_prime(9) is False
    assert is_prime(100) is False


def test_negative_zero_and_one_are_not_prime() -> None:
    assert is_prime(-7) is False
    assert is_prime(0) is False
    assert is_prime(1) is False


def test_prime_non_integer_raises_type_error() -> None:
    with pytest.raises(TypeError):
        is_prime(11.5)
