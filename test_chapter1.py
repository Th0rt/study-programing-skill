import unittest
import chapter1


class TestChapter1(unittest.TestCase):
    def test_q_1(self):
        assert chapter1.q_1("abcd")
        assert not chapter1.q_1("aaaa")

    def test_q_2(self):
        assert chapter1.q_2("abcde", "edcba")
        assert not chapter1.q_2("abcde", "edcbe")

    def test_q_3(self):
        assert chapter1.q_3("Mr John Smith ", 13) == "Mr%20John%20Smith"
        assert not chapter1.q_3("MrJohnSmith", 11) == "Mr%20John%20Smith"

    def test_q_4(self):
        assert chapter1.q_4("Tact Coa")
        assert chapter1.q_4("たけややけた")
        assert chapter1.q_4("ああ")
        assert not chapter1.q_4("あかさたなはまやらわ")
        assert not chapter1.q_4("")
        assert not chapter1.q_4("あ")


if __name__ == "__main__":
    unittest.main()
