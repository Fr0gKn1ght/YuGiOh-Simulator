class Board:
    def __init__(self):
        field = {
                  "p1": {"f1": None, "f2": None, "f3": None, "f4": None, "f5": None,
                         "b1": None, "b2": None, "b3": None, "b4": None, "b5": None},
                  "p2": {"f1": None, "f2": None, "f3": None, "f4": None, "f5": None,
                         "b1": None, "b2": None, "b3": None, "b4": None, "b5": None}
                }
        grave_yard = {"p1": [], "p2": []}