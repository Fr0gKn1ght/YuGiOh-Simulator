class Card:
    def __init__(self):
        self.name
        self.card_type

    def set_card(self):
        pass

class MonsterCard(Card):
    def __init__(self, name: str, rank: int, atk: int, dfc: int, effect):
        self.mode
        self.name = name
        self.rank = rank
        self.attack = atk
        self.defense = dfc


class SpellCard(Card):
    def __init__(self, name: str, spell_type:str , effect):
        pass

class TrapCard(Card):
    def __init__(self, name: str, trap_type: str, effect):
        pass

