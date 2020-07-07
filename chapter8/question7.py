import unittest
from typing import List


def make_patterns(x: str, res: List[str] = None, i: int = 0):
    if res is None:
        x = eject_multi(x)
        res = []

    if i == len(x):
        return res

    res = _make_patterns(res, x)
    return make_patterns(x, res, i=i+1)


def eject_multi(x: str, res: str = "", memo: dict = None) -> str:
    if len(x) == 0:
        return res

    if memo is None:
        memo = {}

    if memo.get(x[0]):
        return eject_multi(x[1:], res, memo)
    else:
        memo[x[0]] = True
        res += x[0]
        return eject_multi(x[1:], res, memo)


def _make_patterns(x: List[str], y: str, res: list = None):
    if res is None:
        res = []

    if len(x) == 0:
        if len(res) == 0:
            return _make_pattern("", y)
        return res

    res = res + _make_pattern(x[0], y)
    return _make_patterns(x[1:], y, res)


def _make_pattern(x: str, y: str, res: list = None) -> List[str]:
    if res is None:
        res = []

    if len(y) == 0:
        return res

    if y[0] not in x:
        res.append(x+y[0])

    return _make_pattern(x, y[1:], res)


class TestMain(unittest.TestCase):
    def test_it(self):
        res = make_patterns("いろは")
        print(res)
        assert res == ["いろは", "いはろ", "ろいは", "ろはい", "はいろ", "はろい"]

    def test_it2(self):
        res = make_patterns("いろはい")
        print(res)
        assert res == ["いろは", "いはろ", "ろいは", "ろはい", "はいろ", "はろい"]

    def test_make_patterns(self):
        res = _make_patterns([], "いろは")
        assert res == ["い", "ろ", "は"]

    def test_make_patterns2(self):
        res = _make_patterns(["い", "ろ", "は"], "いろは")
        assert res == ["いろ", "いは", "ろい", "ろは", "はい", "はろ"]

    def test_make_pattern_1(self):
        res = _make_pattern("", "いろは")
        assert res == ["い", "ろ", "は"]

    def test_make_pattern_2(self):
        res = _make_pattern("い", "いろは")
        assert res == ["いろ", "いは"]

    def test_make_pattern_3(self):
        res = _make_pattern("い", "いろはい")
        assert res == ["いろ", "いは"]


if __name__ == '__main__':
    unittest.main()
