from deck import Deck
from board import Board

class Player:
    def __init__(self, id: str, deck: Deck, life: int):
        self.player_id = id
        self.life_points = life
        self.deck = deck
        self.my_turn = False
        self.hand = []

    def draw_cards(self, num):
        drawn = self.deck.draw(num)
        if drawn != None:
            self.hand.extend(drawn)
        else:
            pass #TODO: Implement notification that the player's deck is out of cards

    def discard(self, board: Board, cards: list[int]):
        discarded = []
        for i in range(len(cards)-1, -1, -1):
            discarded.append(self.hand[cards[i]])
            del self.hand[cards[i]]
        board.grave_yard[self.player_id].extend(discarded)