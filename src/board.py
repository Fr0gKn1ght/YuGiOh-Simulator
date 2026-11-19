from card import Card, CardType
# Represents the game board, including the playing field where monsters, spells and traps are layed out, as well as the player graveyards.
# May also store the player decks + hands in the future for ease of use.
class Board:
       def __init__(self,p1: str ,p2: str):
              self.field = {
                     p1: {"f1": None, "f2": None, "f3": None, "f4": None, "f5": None,
                            "b1": None, "b2": None, "b3": None, "b4": None, "b5": None},
                     p2: {"f1": None, "f2": None, "f3": None, "f4": None, "f5": None,
                            "b1": None, "b2": None, "b3": None, "b4": None, "b5": None}
                     }
              self.grave_yard = {p1: [], p2: []}

       # Place card on a requested spot on the board.
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

       # Retrieve a card on the board.
       def get_card(self, player: str, space: str):
              return self.field[player][space]
       # Send a card from the field to the graveyard.
       def to_graveyard(self, player: str, space: str):
              card = self.field[player][space]
              self.grave_yard[player].append(card)
              self.field[player][space] = None
       
       #Retreives a card from the graveyard, removing it in the process.
       def retrieve_card(self, player: str, name: str):
              card = None
              for i in range(len(self.grave_yard[player])):
                     if self.grave_yard[player][i].name == name:
                            card = self.grave_yard[player][i]
                            del self.grave_yard[player][i]
                            return card
              return None #Could not find the requested card

        