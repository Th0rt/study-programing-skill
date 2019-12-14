from dataclasses import dataclass
from enum import Enum
from typing import TypeVar

from chapter3.common import Queue, QueueNode


@dataclass
class AnimalShelterQueueNode(QueueNode):
    id: int = 0


class AnimalShelterQueue(Queue):
    def add(self, id, item):
        t = AnimalShelterQueueNode(id=id, data=item)
        if self._last:
            self._last.next = t

        self._last = t

        if self._first is None:
            self._first = self._last

    def peek(self):
        return self._first


class AnimalShelter:
    def __init__(self):
        self._id_sequence = 0
        self._dog_queue = AnimalShelterQueue()
        self._cat_queue = AnimalShelterQueue()

    def enqueue(self, animal):
        if animal.type == AnimalType.DOG:
            target_queue = self._dog_queue
        elif animal.type == AnimalType.CAT:
            target_queue = self._cat_queue
        else:
            raise ValueError("!!!!! Unknown Animal !!!!!")

        target_queue.add(id=self._id_sequence, item=animal)
        self._id_sequence += 1

    def dequeue_any(self):
        if self.is_empty:
            return None
        if self._dog_queue.is_empty:
            return self._cat_queue.remove()
        if self._cat_queue.is_empty:
            return self._dog_queue.remove()

        if self._dog_queue.peek().id < self._cat_queue.peek().id:
            return self._dog_queue.remove()
        else:
            return self._cat_queue.remove()

    def dequeue_dog(self):
        return self._dog_queue.remove()

    def dequeue_cat(self):
        return self._cat_queue.remove()

    @property
    def is_empty(self):
        return self._dog_queue.is_empty and self._cat_queue.is_empty


class AnimalType(Enum):
    DOG = 0
    CAT = 1


@dataclass
class Animal:
    name: str

    @property
    def type(self):
        raise NotImplementedError


@dataclass
class Dog(Animal):
    @property
    def type(self):
        return AnimalType.DOG


@dataclass
class Cat(Animal):
    @property
    def type(self):
        return AnimalType.CAT
