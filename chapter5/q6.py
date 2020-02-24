import unittest
from functools import reduce


def count_different_bits(num1, num2):
    """
    num1からnum2に変換するbit数を出力す
    XOR取って折り畳むだけ
    """

    diff = num1 ^ num2
    return reduce(lambda x, y: x+int(y), bin(diff)[2:], 0)


class TestQuestion6(unittest.TestCase):
    def test_it(self):
        assert count_different_bits(29, 15) == 2
        assert count_different_bits(29, 0) == 4


if __name__ == "__main__":
    unittest.main()
