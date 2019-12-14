import sys

import pytest

from chapter3.common import Stack
from chapter3.question5 import AscSortedStack


class TestQuestion5:
    @pytest.fixture
    def target(self):
        return AscSortedStack

    def test_it(self, target):
        instance = target()

        for even in range(0, 11, 2):
            instance.push(even)

        for odd in range(1, 11, 2):
            instance.push(odd)

        expect = list(range(0, 11))
        actual = [instance.pop().data for _ in expect]

        assert actual == expect
