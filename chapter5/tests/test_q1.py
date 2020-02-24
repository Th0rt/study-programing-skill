import pytest
from chapter5.q1 import insert_bit


def test_insert_bit():
    n = 0b10000100000
    m = 0b10011
    i = 2
    j = 6
    assert insert_bit(n, m, i, j) == bin(0b10001001100)
