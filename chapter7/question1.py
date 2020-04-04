from random import sample
from abc import ABC, abstractclassmethod
from typing import List
import unittest
from enum import Enum
from copy import deepcopy


"""
Base Class
"""


class Card:
    last_insert_id: int = 0

    def __init__(self):
        self.id = self.aunto_increment_id()

    @classmethod
    def aunto_increment_id(cls):
        cls.last_insert_id += 1
        return cls.last_insert_id


class CardSet:
    def create_cards(self) -> List[Card]:
        raise NotImplementedError


class InvalidDeckError:
    pass


class DeckRule(ABC):
    exception: InvalidDeckError = InvalidDeckError

    @classmethod
    def validate(cls) -> None:
        if not cls._validate:
            raise cls.exception()
        return None

    @abstractclassmethod
    def _validate(cls) -> bool:
        raise NotImplementedError


class Deck:
    card_set: CardSet
    rules: List[DeckRule] = []

    def __init__(self, cards: List[Card] = []):
        self._cards = cards

    @property
    def cards(self):
        if self._cards:
            return self._cards
        self._cards = self.card_set.create_cards()
        return self.cards

    def validate(self, cards: List[Card]) -> bool:
        if self.rules:
            try:
                [rule.validate(self.cards) for rule in self.rules]
            except InvalidDeckError as e:
                raise e
        return True

    def drow_cards(self, drow_number: int = 1) -> [Card]:
        drows = self._cards[drow_number:]
        self._cards = self.cards[:drow_number]
        return drows

    def insert_top(self, inserts: List[Card]):
        inserted = inserts + self._cards
        if self.validate(inserted):
            self._cards = inserted

    def insert_bottom(self, inserts: List[Card]):
        inserted = self._cards + inserts
        if self.validate(inserted):
            self._cards = inserted

    def shuffle(self):
        self._cards = sample(self._cards)

    def shot_gun_shuffle(self):
        print("ショット・ガン・シャッフルはカードを痛めるぜ！")
        self.shuffle()


"""
Trump Class
"""


class TrumpCardType(Enum):
    NORMAL = 1
    JOKER = 2


class TrumpSuit(Enum):
    SPADE = 1
    CLUB = 2
    HEART = 3
    DIAMOND = 4


class TrumpCard(Card):
    def __init__(self, type: TrumpCardType, suit: TrumpSuit, number: int):
        super().__init__()
        self.type = type
        self.suit = suit
        self.number = number


class TrumpCardSet(CardSet):
    card_class = TrumpCard
    joker_number = 2

    @classmethod
    def create_cards(cls) -> List[TrumpCard]:
        cards = []

        for suit in TrumpSuit:
            for number in range(1, 14):
                cards.append(
                    cls.card_class(type=TrumpCardType.NORMAL, suit=suit, number=number)
                )

        if cls.joker_number:
            joker = cls.card_class(type=TrumpCardType.JOKER, suit=None, number=None)
            for _ in range(cls.joker_number):
                cards.append(deepcopy(joker))

        return cards


class TrumpCardDeck(Deck):
    card_set = TrumpCardSet


class TestTrumpCardSet(unittest.TestCase):
    def test_it(self):
        cards = TrumpCardSet.create_cards()

        assert len(cards) == 54

        assert cards[0].id == 1
        assert cards[0].suit == TrumpSuit.SPADE
        assert cards[0].number == 1

        print(cards[51].__dict__)
        assert cards[51].id == 52
        assert cards[51].suit == TrumpSuit.DIAMOND
        assert cards[51].number == 13


class TestTrumpDeck(unittest.TestCase):
    target = TrumpCardDeck()
    print(target.card_map)
    assert False


if __name__ == "__main__":
    unittest.main()
