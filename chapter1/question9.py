import unittest


def main(s1: str, s2: str):
    """
    s2がs1の回転文字列か判定する
    全体でO(n)
    """
    if len(s1) == len(s2) and is_substring(s1, s2 * 2):
        return True
    return False


def is_substring(s1: str, s2: str):
    return s1 in s2


class TestQuestion9(unittest.TestCase):
    def test_main(self):
        assert main("waterbottle", "erbottlewat")
        assert not main("waterbwttle", "erbottlewat")


if __name__ == "__main__":
    unittest.main()
