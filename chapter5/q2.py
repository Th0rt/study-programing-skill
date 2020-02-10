
def float_to_digit(n: float, output="0.", max_length=32):
    """
    0 > n >= 1 である10進数の実数nを2進数に変換する。
    ただし、桁数が32桁を超える場合は"ERROR"を出力する。

    10進数の小数nを2進数の小数へ基数変換するには以下のステップで行う。
    1. xを2倍にする。(x2とする)
    2. x2>=1の場合は、小数1桁目は1。x=x2-1として、2桁目の計算を行う。
    3. x2<1の場合は、小数1桁目は0。x=x2として、2桁目の計算を行う。
    """
    if len(output) > max_length:
        return "ERROR"

    if n == 0:
        return float(output)

    t = n*2
    if t >= 1:
        return float_to_digit(n=t-1, output=output+"1", max_length=max_length)
    else:
        return float_to_digit(n=t, output=output+"0", max_length=max_length)
