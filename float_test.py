import pytest


@pytest.mark.parametrize("x, y", [(5.3, 5.3001), (7.8, 7.7999)])
def test_float_delta(x: float, y: float):
    assert x == pytest.approx(y, 0.001)


def test_float_positive():
    assert 11092.172 >= 0
