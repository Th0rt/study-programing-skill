import pytest

from chapter3.question6 import AnimalShelter, Cat, Dog


class TestQuestion6:
    @pytest.fixture
    def dogs(self):
        names = ["taro", "jiro"]
        return [Dog(name) for name in names]

    @pytest.fixture
    def cats(self):
        names = ["tama", "coro"]
        return [Cat(name) for name in names]

    @pytest.fixture
    def shelter(self, dogs, cats):
        shelter = AnimalShelter()

        for dog, cat in zip(dogs, cats):
            shelter.enqueue(dog)
            shelter.enqueue(cat)

        return shelter

    def test_enqueue(self, shelter, dogs, cats):
        actual_dogs = [shelter._dog_queue.remove() for _ in dogs]
        actual_cats = [shelter._cat_queue.remove() for _ in cats]

        assert actual_dogs == dogs
        assert actual_cats == cats

    def test_dequeue_any(self, shelter, dogs, cats):
        for dog, cat in zip(dogs, cats):
            assert shelter.dequeue_any() == dog
            assert shelter.dequeue_any() == cat

    def test_dequeue_dog(self, shelter, dogs):
        for dog in dogs:
            assert shelter.dequeue_dog() == dog

    def test_dequeue_cat(self, shelter, cats):
        for cat in cats:
            assert shelter.dequeue_cat() == cat
