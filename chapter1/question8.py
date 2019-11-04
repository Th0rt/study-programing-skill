import unittest


def main(data: list) -> list:
    """
    行列内の、0を含む列と行の値を全て0にして返す。
    計算量 ... O(nm+n(n log n))
    """
    # 0が含まれている列を探す
    # 計算量は最悪ケースでO(n(n log n))
    zero_exist_rows = []
    for row_index, line in enumerate(data):
        # sorted()はティムソートなのでO(n log n)
        if sorted(line)[0] == 0:
            zero_exist_rows.append(row_index)

    # 0が含まれている行を探す
    # 計算量は最悪ケースで0(nm)
    zero_exist_columns = []
    for row_index in zero_exist_rows:
        for column_index, value in enumerate(data[row_index]):
            if value == 0:
                zero_exist_columns.append(column_index)

    # 行変換処理
    # O(n)
    for row_index in zero_exist_rows:
        data[row_index] = [0] * len(data[row_index])

    # 列変換処理
    # O(n)
    for column_index in zero_exist_columns:
        for row in data:
            row[column_index] = 0

    return data


class TestQuestion8(unittest.TestCase):
    def test_main(self):
        data = [
            [1, 1, 1, 1, 1],
            [1, 1, 0, 1, 0],
            [1, 1, 1, 1, 1],
            [1, 0, 1, 1, 1],
            [1, 1, 1, 1, 1],
        ]
        expect = [
            [1, 0, 0, 1, 0],
            [0, 0, 0, 0, 0],
            [1, 0, 0, 1, 0],
            [0, 0, 0, 0, 0],
            [1, 0, 0, 1, 0],
        ]
        actual = main(data)
        assert actual == expect


if __name__ == "__main__":
    unittest.main()
