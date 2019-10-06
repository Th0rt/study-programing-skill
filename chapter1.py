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
