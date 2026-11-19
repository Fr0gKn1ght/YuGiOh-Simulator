from deck import Deck

class Player:
    def __init__(self, id: str, deck: Deck, life: int):
        self.player_id = id
        self.life_points = life
        self.deck = deck
        self.hand = []

    def draw_cards(self, num):
        drawn = self.deck.draw(num)
        if drawn != None:
            self.hand.extend(drawn)
        else:
            pass #TODO: Implement notification that the player's deck is out of cards

    def discard(self, cards: list[str]):
        pass #TODO: Implement function to discard card from hand to the graveyard.