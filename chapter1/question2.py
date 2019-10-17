import unittest


def q_2(s1: str, s2: str) -> bool:
    if s1 == "":
        return True

    for i in range(len(s2)):
        if s1[0] == s2[i]:
            return q_2(s1[1:], s2)

    return False


class TestQuestion2(unittest.TestCase):

    def test_q_2(self):
        assert q_2("abcde", "edcba")
        assert not q_2("abcde", "edcbe")
