import unittest


def q_1(s: str, c: str = None) -> bool:
    if s == "":
        return True

    for i in range(len(s)):
        if c == s[i]:
            return False

    return q_1(s=s[1:], c=s[0])


class TestQuestion1(unittest.TestCase):
    def test_q_1(self):
        assert q_1("abcd")
        assert not q_1("aaaa")


if __name__ == "__main__":
    unittest.main()
