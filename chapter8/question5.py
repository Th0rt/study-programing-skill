import unittest


def factorial(x, y, z=1):
    if y == 0:
        return z
    n = x
    while n > 0:
        z = z << 1
        if n == 1:
            z -= 1
            n = 0
        else:
            n -= 2
    return factorial(x, y-1, z=z)


class TestMain(unittest.TestCase):
    def test_it(self):
        assert factorial(3, 3) == 27



def min_product(a, b):
    if a < b:
        smaller = a
        bigger = b
    else:
        smaller = b
        bigger = a
    return min_product_helper(smaller, bigger)


def min_product_helper(smaller, bigger):
    if smaller == 0:
        return 0
    elif smaller == 1:
        return bigger

    s = smaller // 2
    side1 = min_product_helper(s, bigger)
    side2 = side1
    if smaller % 2 == 1:
        side2 = min_product_helper(smaller - s, bigger)

    return side1 + side2

