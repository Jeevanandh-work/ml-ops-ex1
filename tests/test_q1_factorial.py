import pytest

from src.q1_factorial import factorial


def test_factorial_positive_value() -> None:
    assert factorial(5) == 120


def test_factorial_zero() -> None:
    assert factorial(0) == 1


def test_factorial_small_values() -> None:
    assert factorial(1) == 1
    assert factorial(3) == 6


def test_factorial_negative_raises_value_error() -> None:
    with pytest.raises(ValueError):
        factorial(-4)


def test_factorial_non_integer_raises_type_error() -> None:
    with pytest.raises(TypeError):
        factorial(3.2)
