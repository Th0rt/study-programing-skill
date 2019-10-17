import unittest


def q_3(s: str, l: int, prefix: str = "") -> str:
    if len(s) == 1:
        return prefix

    if s[0] == " ":
        c = "%20"
    else:
        c = s[0]

    return q_3(s=s[1:], l=l-1, prefix=prefix + c)


class TestQuestion3(unittest.TestCase):

    def test_q_3(self):
        assert q_3("Mr John Smith ", 13) == "Mr%20John%20Smith"
        assert not q_3("MrJohnSmith", 11) == "Mr%20John%20Smith"


if __name__ == "__main__":
    unittest.main()
