from board import Board
from card import Card
from deck import Deck
from player import Player
from enum import Enum

class Phase(Enum):
    DRAW = 0
    MAIN_1 = 1
    BATTLE =  2
    MAIN_2 = 3
    END = 4 

class Game:
    def __init__(self, player_1, player_2, first):
        self.turns = 0 #Number of turn passed since the game began.
        self.players = [player_1, player_2]
        #TO DO: Implement state machine to determine which player's turn it is and what phase the turn is on.