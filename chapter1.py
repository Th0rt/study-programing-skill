from functools import reduce


def q_1(s: str, c: str = None) -> bool:
    if s == "":
        return True

    for i in range(len(s)):
        if c == s[i]:
            return False

    return q_1(s=s[1:], c=s[0])


def q_2(s1: str, s2: str) -> bool:
    if s1 == "":
        return True

    for i in range(len(s2)):
        if s1[0] == s2[i]:
            return q_2(s1[1:], s2)

    return False


def q_3(s: str, l: int, prefix: str = "") -> str:
    if len(s) == 1:
        return prefix

    if s[0] == " ":
        c = "%20"
    else:
        c = s[0]

    return q_3(s=s[1:], l=l-1, prefix=prefix + c)


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
    # O(1)
    if sum(mem.values()) % 2 == 0:
        return odd_char_count == 0
    # 文字列長が奇数の場合は、1つだけ奇数回、他は全て偶数回出現していなくてはならない
    else:
        return odd_char_count == 1
