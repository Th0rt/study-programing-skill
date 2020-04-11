import unittest
from test.support import captured_stdout


class Person:
    pass


class Cusomter(Person):
    pass


class JukeBoxOwner(Person):
    pass


class Wallet:
    pass


class Coin:
    pass


class JukeBox:
    pass


class Record:
    pass


class Song:
    pass


class TestJukeBox(unittest.TestCase):
    def setUp(self):
        self.owner = JukeBoxOwner()
        self.jukebox = JukeBox(owner=owner)
        self.customer = Cusomter()

    def test_it(self):

        with captured_stdout as stdout:
            self.customer.insert_coin(self.jukebox)
            stdout_lines = stdout.getvalue.splitlines()

            assert stdout_lines[-2] == "Please Select Song!"
            assert stdout_lines[-1] == "1) 幽雅に咲かせ、墨染の桜 ～Border of Life"


if __name__ == "__main__":
    unittest.main()
