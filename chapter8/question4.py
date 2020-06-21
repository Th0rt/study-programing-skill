import unittest

"""
(1, 2, 3)

(,)
1 (2, 3) = (1,) (1, 2) (1, 2, 3) ...
2 (3,) = (2,) (2, 3)
3 (,) = (3,)
"""

def get_power_set(x, ret=()):
    if len(x) == 0:
        return ((),) + ret
    n = get_series(x=x[0], y=x[1:])
    return get_power_set(x[1:], ret=ret+n)


def get_series(x, y, p=1, ret=()):
    if len(y) == 0:
        return ((x,),) + ret

    n = (x,) + y[:p]

    if p == len(y):
        return get_series(x, y[1:], p=1, ret=ret + (n,))
    else:
        return get_series(x, y, p=p + 1, ret=ret + (n,))


class TestMain(unittest.TestCase):
    def test_get_power_set(self):
        assert get_power_set((1, 2, 3)) == ((), (1,), (1, 2), (1, 2, 3), (1, 3), (2,), (2, 3), (3,))

    def test_get_series(self):
        assert get_series(1, (2, 3, 4)) == ((1,), (1, 2), (1, 2, 3), (1, 2, 3, 4), (1, 3), (1, 3, 4), (1, 4))
