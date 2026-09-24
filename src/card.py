from enum import Enum

class CardType(Enum):
    MONSTER = 1
    SPELL = 2
    TRAP = 3

class Card:
    def __init__(self):
        self.name
        self.card_type

class MonsterCard(Card):
    def __init__(self, name: str, rank: int, atk: int, dfc: int, effect):
        self.mode
        self.name = name
        self.card_type = CardType.MONSTER
        self.rank = rank
        self.attack = atk
        self.defense = dfc


class SpellCard(Card):
    def __init__(self, name: str, spell_type:str , effect):
        self.name = name
        self.card_type = CardType.SPELL

class TrapCard(Card):
    def __init__(self, name: str, trap_type: str, effect):
        self.name = name
        self.card_type = CardType.TRAP

