import unittest
from typing import List
import sys
import io
from contextlib import redirect_stdout


class Wallet:

    def __init__(self, credit: int = 0):
        self.creadit = credit

    def pay(self, value):
        if value > self.creadit:
            return ValueError()
        else:
            self.creadit -= value
            return value


class Person:
    def __init__(self, wallet: Wallet):
        self.wallet = wallet

    def pay(self, target):
        print(target)
        return target.receipt(self.wallet.pay(target.credit_value))


class Cusomter(Person):
    pass


class JukeBoxOwner(Person):
    pass


class Song:
    pass


class Record:
    pass


class JukeBox:
    credit_value: int = 1

    def __init__(self, owner: JukeBoxOwner, records: List[Record] = []):
        self.owner = owner
        self.records = records
        self.gain = 0

    def receipt(self, credit_value):
        self.gain += self.credit_value
        print("select song!")


class TestJukeBox(unittest.TestCase):
    def setUp(self):
        self.owner = JukeBoxOwner(wallet=Wallet())
        self.jukebox = JukeBox(owner=self.owner)
        self.customer = Cusomter(wallet=Wallet(credit=2))
        self.stdout = io.StringIO()

    def test_it(self):

        with redirect_stdout(self.stdout):
            self.customer.pay(self.jukebox)

        stdout = self.stdout.getvalue().splitlines()
        assert stdout[1] == "select song!"


if __name__ == "__main__":
    unittest.main()
