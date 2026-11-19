from card import Card
import random

class Deck:
    def __init__(self, cards: list[Card]):
        self.cards = cards

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self, count: int) -> list[Card] | None:
        if len(self.cards < count):
            return None #Deck is out of cards, loss condition.
        drawn_cards = self.cards[-count:]
        del self.cards[-count:]
        return drawn_cards

    def add_card(self, card: Card):
        self.cards.append(card)

    def remove_card(self, idx: int):
        del self.cards[idx]