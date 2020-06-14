import unittest

def detect_magic_index(origin, searching=None, pointer=0):
    if searching is None:
        searching = origin

    if len(searching) == 0:
        return None

    index = len(searching) // 2
    value = searching[index]

    print(f"original list:{origin}")
    print(f"search list:{searching}")
    print(f"index:{index}, pointer: {pointer}, value:{value}")

    if index == value:
        return value

    if index > value:
        print(f"index:{index} > value:{value}\n")
        return detect_magic_index(origin, searching=searching[index + 1:], pointer=pointer+index)

    if index < value:
        print(f"index:{index} < value:{value}, next: {searching[:index]}\n")
        return detect_magic_index(origin, searching=searching[:index], pointer=pointer+index)


class TestDetectMagicIndex(unittest.TestCase):
    def test_1(self):
        l = [0, 1, 2, 3, 4]
        actual = detect_magic_index(l)
        print(actual)
        assert actual == 2

    def test_2(self):
        l = [1, 2, 3, 4, 4]
        actual = detect_magic_index(l)
        print(actual)
        assert actual == 4


if __name__ == '__main__':
    unittest.main()
