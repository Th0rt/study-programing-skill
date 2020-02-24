import unittest
from functools import reduce
import math


def exchange_bits_odd_and_even(bits):
    length = len(bin(bits)) - 2
    even_mask = create_stripe_bits(tail=0, length=length)
    odd_mask = create_stripe_bits(tail=1, length=length)

    even_bits = bits & even_mask
    odd_bits = bits & odd_mask

    return even_bits >> 1 | odd_bits << 1


def create_stripe_bits(tail, length):
    if not any((tail == 0, tail == 1)):
        raise ValueError("head bit is 1 or 0.")

    unit = 0b10 if tail == 0 else 0b01
    unit_count = length//2 if length % 2 == 0 else (length+1) // 2

    return sum([unit*4**n for n in range(unit_count)])


class TestQuestion7(unittest.TestCase):
    def test_it(self):
        assert exchange_bits_odd_and_even(0b10101010) == 0b01010101
        assert exchange_bits_odd_and_even(0b01100110) == 0b10011001

    def test_create_stripe_bits(self):
        assert create_stripe_bits(0, 8) == 0b10101010
        assert create_stripe_bits(1, 8) == 0b1010101


if __name__ == "__main__":
    unittest.main()
