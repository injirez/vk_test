import pytest


def test_str_upper():
    assert "hi".upper() == "HI"


def test_str_multiply():
    assert "hi" * 4 == "hihihihi"
