import pytest


def test_set_multiply():
    try:
        test_set = (1, 2, 3, 4)
        assert test_set * unknown
    except NameError:
        pass


def test_set_add():
    test_set_before = {1, 2, 3, 4}
    test_set_after = {1, 2, 3, 4, 5}
    test_set_before.add(5)
    assert test_set_before == test_set_after
