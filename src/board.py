from card import Card, CardType

class Board:
       def __init__(self):
              field = {
                     "p1": {"f1": None, "f2": None, "f3": None, "f4": None, "f5": None,
                            "b1": None, "b2": None, "b3": None, "b4": None, "b5": None},
                     "p2": {"f1": None, "f2": None, "f3": None, "f4": None, "f5": None,
                            "b1": None, "b2": None, "b3": None, "b4": None, "b5": None}
                     }
              grave_yard = {"p1": [], "p2": []}

       def place_card(self, card: Card, player: str, space: str):
              if card.card_type == CardType.MONSTER:
                     if space.startswith("b"):
                            print("Monster Card cannot be placed in the back row.")
                            return
              if (card.card_type == CardType.SPELL or card.card_type == CardType.TRAP) and space.startswith("f"):
                     type = "Spell" if card.card_type == CardType.SPELL else "Trap" 
                     print(f"{type} Card cannot be placed in the front row.")
                     return
              if self.field[player][space] != None:
                     print(f"Space {space} is already occupied.")
                     return
              self.field[player][space] = card
        