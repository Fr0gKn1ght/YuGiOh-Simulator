from deck import Deck

class Player:
    def __init__(self, id: str, deck: Deck, life: int):
        self.player_id = id
        self.life_points = life
        self.deck = deck
        self.hand = []

    def draw_cards(self, num):
        self.hand.extend(self.deck.draw(num))

    def discard(self, cards: list[str]):
        pass #TO DO: Implement function to discard card from hand to the graveyard.