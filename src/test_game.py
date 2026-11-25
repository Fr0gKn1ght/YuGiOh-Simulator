import unittest
from player import Player
from deck import Deck
from card import MonsterCard
from game import Game, Turn, State

class TestGame(unittest.TestCase):

    test_card = MonsterCard("Test", 1, 100, 100, None)
    test_deck = [test_card, test_card, test_card, test_card, test_card]
    p1 = Player("P1", Deck(test_deck), 8000)
    p2 = Player("P2", Deck([test_deck]), 8000)

    def test_game_start(self):
        game = Game(self.p1, self.p2, Turn.PLAYER_1)
        self.assertEqual(game.get_state(), State.GAME_START)

    def test_change_state(self):
        game = Game(self.p1, self.p2, Turn.PLAYER_1)
        game.change_state(State.DRAW_PHASE)
        self.assertEqual(game.get_state(), State.DRAW_PHASE)