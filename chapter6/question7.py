from random import randint

# 具体的なシミュレーション例はchapter6_question7.ipynbを参照


def simulate(famiry_size=0):
    """
    famiry_sizeの家族数におけるシミュレーションを1回行う。
    """

    children, female = 0, 0

    for _ in range(0, famiry_size):
        while True:
            i = randint(1, 10)

            children += 1
            # 乱数が偶数なら、女子が生まれたと判定する
            if i % 2 == 0:
                female += 1
                break

    return round(female / children, 3)


def simulate_multipule(trial_number: int, max_famiry_size: int):
    """
    1からmax_famiry_sizeまでの各家族数のケースをtrial_number回シミュレーションし、
    各回の女児率、平均女児率、標準偏差を返す。
    """

    result = {}

    for famiry_count in range(1, max_famiry_size + 1):

        # 各試行における子供の総数に対する女児の比率
        values = [simulate(famiry_count) for _ in range(trial_number)]

        # 女子率の平均
        average = round(sum(values) / trial_number, 3)

        # 女子率の分散
        varience = sum([(value - average) ** 2 / trial_number for value in values])

        # 女子率の平均偏差
        standard_deviation = varience ** 0.5

        result[famiry_count] = dict(
            values=values, average=average, standard_deviation=standard_deviation,
        )

    return result
