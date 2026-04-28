import pytest
from fuel import convert, gauge


def test_convert_valid():
    assert convert("1/4") == 25
    assert convert("3/4") == 75
    assert convert("1/1") == 100
