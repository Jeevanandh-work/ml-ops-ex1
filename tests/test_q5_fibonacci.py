import pytest

from src.q5_fibonacci import fibonacci_upto


def test_fibonacci_zero_limit() -> None:
    assert fibonacci_upto(0) == [0]


def test_fibonacci_positive_limit() -> None:
    assert fibonacci_upto(1) == [0, 1, 1]
    assert fibonacci_upto(10) == [0, 1, 1, 2, 3, 5, 8]


def test_fibonacci_negative_raises_value_error() -> None:
    with pytest.raises(ValueError):
        fibonacci_upto(-2)


def test_fibonacci_non_integer_raises_type_error() -> None:
    with pytest.raises(TypeError):
        fibonacci_upto(5.5)
