import unittest


def q_5(s1: str, s2: str) -> bool:
    """
    s1が1文字削除、1文字追加、1文字編集のいずれかでs2になるか判定する
    トータル計算量 ... O(n)
    """

    # 完全一致していたらTrue
    # O(1)
    if s1 == s2:
        return True

    # 文字列長の差から、どのパターンか判定する
    # -1なら追加、1なら削除、0なら編集
    diff_length = len(s1) - len(s2)

    # 文字列長が2以上違うなら、どのパターンにも該当しない
    # O(1)
    if abs(diff_length) >= 2:
        return False

    # 文字が追加されている場合(文字列長がの差分が-1)の場合は、比較の向きを逆にする
    if diff_length == -1:
        c1 = s2
        c2 = s1
    else:
        c1 = s1
        c2 = s2

    # 文字列長の差が0なら編集、-1なら追加/削除
    if diff_length == 0:
        # 編集の場合は差分が1文字だけあること
        # O(n)
        i = 0
        diff_count = False
        while i < len(c1):
            if not c1[i] == c2[i]:
                if diff_count:
                    return False
                diff_count = True
            i += 1
        return True
    else:
        # 追加/削除の場合は差分がないこと
        # O(n)
        i = 0
        diff_count = 0
        while i < len(c2):
            if not c1[i] == c2[i+diff_count]:
                if diff_count:
                    return False
                diff_count = 1
            i += 1
        return True


class TestQuestion5(unittest.TestCase):

    def test_q_5(self):
        assert q_5("pale", "pale")  # 完全一致
        assert q_5("pale", "pales")  # 追加
        assert q_5("pales", "pale")  # 削除
        assert q_5("pale", "bale")  # 編集
        assert not q_5("pale", "bales")  # 追加かつ編集
        assert not q_5("pale", "pelas")  # 追加かつ編集
        assert not q_5("pale", "bal")  # 削除かつ編集
        assert not q_5("bake", "pale")  # 2文字編集


if __name__ == "__main__":
    unittest.main()
