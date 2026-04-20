import pytest

from src.q4_sort import sort_integers


def test_sort_empty_list() -> None:
    assert sort_integers([]) == []


def test_sort_singleton_list() -> None:
    assert sort_integers([7]) == [7]


def test_sort_unsorted_list() -> None:
    assert sort_integers([5, 1, 4, 2]) == [1, 2, 4, 5]


def test_sort_with_repeated_elements() -> None:
    assert sort_integers([3, 1, 3, 2, 2]) == [1, 2, 2, 3, 3]


def test_sort_already_sorted_list() -> None:
    assert sort_integers([1, 2, 3]) == [1, 2, 3]


def test_sort_non_list_raises_type_error() -> None:
    with pytest.raises(TypeError):
        sort_integers("1,2,3")  # type: ignore[arg-type]


def test_sort_non_integer_item_raises_type_error() -> None:
    with pytest.raises(TypeError):
        sort_integers([1, "2", 3])  # type: ignore[list-item]
