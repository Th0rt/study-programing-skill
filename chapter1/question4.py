import unittest
from functools import reduce


def q_4(s: str) -> bool:
    """
    sに含まれる文字を使って回文が作れるか判定する
    O(2n+2) ≒ O(n)
    """
    # 文字列長が 1or0 ならFalse
    # O(1)
    if len(s) < 2:
        return False

    # 各文字の出現回数をmemorize
    # O(n)
    mem = {}
    for c in s.lower():
        # 空白文字列は考慮しない
        if c == " " or c == "　":
            continue
        mem[c] = mem.setdefault(c, 0) + 1

    # 奇数回出現した文字の個数をカウント
    # O(n)
    odd_char_count = reduce(lambda x, y: x + (y % 2), mem.values(), 0)

    # 文字列長が偶数の場合は、全文字が偶数回出現していなくてはならない
    # O(n)
    if sum(mem.values()) % 2 == 0:
        return odd_char_count == 0
    # 文字列長が奇数の場合は、1つだけ奇数回、他は全て偶数回出現していなくてはならない
    else:
        return odd_char_count == 1


class TestQuestion4(unittest.TestCase):

    def test_q_4(self):
        assert q_4("Tact Coa")
        assert q_4("たけや　やけた")
        assert q_4("ああ")
        assert not q_4("あかさたなはまやらわ")
        assert not q_4("")
        assert not q_4("あ")


if __name__ == "__main__":
    unittest.main()
