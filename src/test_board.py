import unittest
from board import Board
from card import Card, MonsterCard, SpellCard, TrapCard

class TestBoard(unittest.TestCase):
    def test_set_card(self):
        game_board = Board()
        my_card = MonsterCard("Test Monster", 3, 200, 200, [])
        game_board.place_card(my_card, "p1", "f1")
        