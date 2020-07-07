import unittest
from typing import List




def hanoi():
    t1 = [1, 2, 3]
    t2 = []
    t3 = []

    t2.append(t1[0])
    t1 = t1[1:]

    print(t1, t2, t3)


def move_circle(from_tower: List, to_tower: List):
    c = from_tower.pop(0)
    to_tower.append(c)


class TowerManager:
    def __init__(self, circle_count: int):
        circles = [Circle(size=n) for n in range(1, circle_count+1)]
        self.first_tower = Tower(id=1, circles=circles)
        self.second_tower = Tower(id=2, circles=[])
        self.third_tower = Tower(id=3, circles=[])


class Tower:
    """ 塔 """
    id: int
    circles: List["Circle"]

    def __init__(self, id: int, circles: []):
        self.id = id
        self.circles = circles

    def empty(self):
        return len(self.circles) == 0

    def circle_count(self):
        return len(self.circles)

    def top_circle(self):
        return self.circles[0]

    def stack_circle(self, circle: "Circle"):
        if self.top_circle().can_stack(circle):
            self.circles.append(circle)
            circle.tower = self
        else:
            raise ValueError(
                f"The circle can't stack."
                f"tower_id: {self.id},"
                f"top_circle_size: {self.top_circle().size}"
                f"stack_circle_size: {circle.size}"
            )

class Circle:
    """ 円盤 """
    size: int
    tower: Tower

    def __init__(self, size, tower: Tower =None):
        self.size = size
        self.tower = tower

    def can_stack(self, circle: "Circle"):
        return self.size > circle.size


class TestMain(unittest.TestCase):
    def test_init(self):
        f = TowerManager(circle_count=3)
        assert f.first_tower.circle_count() == 3
        assert f.first_tower.top().size == 1
        assert f.second_tower.empty()
        assert f.third_tower.empty()


if __name__ == '__main__':
    hanoi()

