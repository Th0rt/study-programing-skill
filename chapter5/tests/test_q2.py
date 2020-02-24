from chapter5.q2 import float_to_digit

def test_float_to_digit1():
    assert float_to_digit(0.5) == 0.1

def test_float_to_digit2():
    assert float_to_digit(0.875) == 0.111

def test_error_float_to_digit3():
    assert float_to_digit(0.57, max_length=32) == "ERROR"
