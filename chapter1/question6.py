import unittest


def main(s: str) -> str:
    """
    オリジナルの文字列と結果文字列の文字列長を比較し、短い方を返す。
    計算量: 最悪ケースでO(n)
    """
    res = _compress_string(s)
    if len(res) < len(s):
        return res
    else:
        return s


def _compress_string(s: str, res: str = "") -> str:
    """
    文字列を先頭から個数カウント処理を行い、結果文字列を生成する。
    計算量: 最悪ケースでO(n)
    """
    if s == "":
        return res

    continues = _count_head_char_continues(s)
    return _compress_string(s=s[continues:], res=res+s[0]+str(continues))


def _count_head_char_continues(s: str) -> int:
    """
    文字列の先頭文字が連続している個数をカウントする。
    計算量: 最悪ケースで0(n)
    """

    if s == "":
        return 0

    if len(s) == 1:
        return 1

    pointer = 1
    continues = 1

    while pointer < len(s):
        if s[0] == s[pointer]:
            continues += 1
            pointer += 1
        else:
            return continues

    return continues


class TestQuestion6(unittest.TestCase):
    def test_it(self):
        assert main("aabcccccaaa") == "a2b1c5a3"  # 元の文字列より結果が短いケース
        assert main("aa") == "aa"  # 元の文字列と結果の文字列が同じケース
        assert main("a") == "a"  # 元の文字列より結果が長いケース
        assert main("") == ""

    def test_compress_string(self):
        assert _compress_string("aabcccccaaa") == "a2b1c5a3"
        assert _compress_string("aa") == "a2"
        assert _compress_string("a") == "a1"
        assert _compress_string("") == ""

    def test_count_head_char_continues(self):
        assert _count_head_char_continues("aa") == 2
        assert _count_head_char_continues("ab") == 1
        assert _count_head_char_continues("") == 0


if __name__ == "__main__":
    unittest.main()
