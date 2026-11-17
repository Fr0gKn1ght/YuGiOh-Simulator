from board import Board
from card import Card
from deck import Deck
from player import Player
from enum import Enum

class Turn(Enum):
    PLAYER_1 = 0
    PLAYER_2 = 1

class State(Enum):
    GAME_START = 0
    DRAW_PHASE = 1
    MAIN_PHASE_1 = 2
    BATTLE_PHASE =  3
    MAIN_PHASE_2 = 4
    END_PHASE = 5
    GAME_OVER = 6

class Game:
    def __init__(self, player_1: Player, player_2: Player, first: Turn):
        self.turns = 0 #Number of turn passed since the game began.
        self.players = [player_1, player_2]
        #TODO: Implement state machine to determine which player's turn it is and what phase the turn is on.
        self.active_player = first
        self.state = State.GAME_START

    def change_state(self, next: State | None):
        match self.state:
            case State.GAME_START:
                pass
            case State.DRAW_PHASE:
                pass
            case State.MAIN_PHASE_1:
                pass
            case State.BATTLE_PHASE:
                pass
            case State.MAIN_PHASE_2:
                pass
            case State.END_PHASE:
                self.active_player = Turn.PLAYER_2 if self.active_player == Turn.PLAYER_1 else Turn.PLAYER_1

    def next_turn(self):
        #TODO: Implement functionality to change player attributes depending on which player's turn it currently is.
        pass