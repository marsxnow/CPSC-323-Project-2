class Parser:
    def __init__(self, input):
        self.input = input + "$"
        self.position = 0
        self.stack = [0]

        self.action = {
            (0, "id"): ("s", 5),
            (0, "("): ("s", 4),
            (1, "+"): ("s", 6),
            (1, "$"): ("acc", 0),
            (2, "+"): ("r", 2),
            (2, "*"): ("s", 7),
            (2, ")"): ("r", 2),
            (2, "$"): ("r", 2),
            (3, "+"): ("r", 4),
            (3, "*"): ("r", 4),
            (3, ")"): ("r", 4),
            (3, "$"): ("r", 4),
            (4, "id"): ("s", 5),
            (4, "("): ("s", 4),
            (5, "+"): ("r", 6),
            (5, "*"): ("r", 6),
            (5, ")"): ("r", 6),
            (5, "$"): ("r", 6),
            (6, "id"): ("s", 5),
            (6, "("): ("s", 4),
            (7, "id"): ("s", 5),
            (7, "("): ("s", 4),
            (8, "+"): ("s", 6),
            (8, ")"): ("s", 11),
            (9, "+"): ("r", 1),
            (9, "*"): ("s", 7),
            (9, ")"): ("r", 1),
            (9, "$"): ("r", 1),
            (10, "+"): ("r", 3),
            (10, "*"): ("r", 3),
            (10, ")"): ("r", 3),
            (10, "$"): ("r", 3),
            (11, "+"): ("r", 5),
            (11, "*"): ("r", 5),
            (11, ")"): ("r", 5),
            (11, "$"): ("r", 5),
        }

        self.goto = {
            (0, "E"): 1,
            (0, "T"): 2,
            (0, "F"): 3,
            (4, "E"): 8,
            (4, "T"): 2,
            (4, "F"): 3,
            (6, "T"): 9,
            (6, "F"): 3,
            (7, "F"): 10,
        }

        self.productions = {
            1: ("E", "E+T"),
            2: ("E", "T"),
            3: ("T", "T*F"),
            4: ("T", "F"),
            5: ("F", "(E)"),
            6: ("F", "id"),
        }

    def parse(self):
        while True:
            state = self.stack[-1]
            symbol = self.input[self.position]
            action, value = self.action.get((state, symbol), ("err", 0))
            if action == "s":
                self.stack.append(value)
                self.position += 1
            elif action == "r":
                lhs, rhs = self.productions[value]
                self.stack = self.stack[:-len(rhs)]
                self.stack.append(self.goto[(self.stack[-1], lhs)])
            elif action == "acc":
                print("Parsing succeeded")
                return
            else:
                raise Exception(f"Unexpected symbol '{symbol}' in state {state}")

# Test the parser
p = Parser("(id+id)*id")
p.parse()