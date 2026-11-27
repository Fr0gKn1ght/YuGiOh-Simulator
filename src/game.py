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

        self.active_player = first
        self.state = State.GAME_START
        self.board = Board(player_1.player_id, player_2.player_id)

        self.command_queue = []

    def change_state(self, next: State | None):
        match self.state:
            case State.GAME_START:
                for i in range(len(self.players)):
                    self.players[i].deck.draw(5)
                self.state = State.DRAW_PHASE
                return
            case State.DRAW_PHASE:
                match next:
                    case State.GAME_OVER:
                        self.state = next
                    case _:
                        self.state = State.MAIN_PHASE_1 #Draw Phase always progresses to Main Phase 1 if a game_over state has not been acheived.
                return
            case State.MAIN_PHASE_1:
                match next:
                    case State.BATTLE_PHASE:
                        pass
                    case State.END_PHASE:
                        self.next_turn()
                    case _:
                        pass #Invalid state requested
            case State.BATTLE_PHASE:
                match next:
                    case State.MAIN_PHASE_2:
                        pass
                    case State.END_PHASE:
                        self.next_turn()
                    case _:
                        pass #Invalid state requested
            case State.MAIN_PHASE_2:
                match next:
                    case State.END_PHASE:
                        pass
                    case _:
                        pass #Invalid state requested
            case State.END_PHASE:
                self.next_turn()
            case _:
                return 

    def get_state(self):
        return self.state

    def next_turn(self):
        self.players[self.active_player].my_turn = False
        self.active_player = Turn.PLAYER_2 if self.active_player == Turn.PLAYER_1 else Turn.PLAYER_1
        self.players[self.active_player].my_turn = True
        
    def update(self):
        while(self.command_queue):
            pass