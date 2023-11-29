class Parser:
    def __init__(self, input):
        self.input = input
        self.position = 0

    def consume(self, expected):
        if self.position < len(self.input) and self.input[self.position] == expected:
            self.position += 1
        else:
            raise Exception(f"Expected '{expected}' but got '{self.input[self.position]}'")

    def parse_E(self):
        self.parse_T()
        while self.position < len(self.input) and self.input[self.position] == '+':
            self.consume('+')
            self.parse_T()

    def parse_T(self):
        self.parse_F()
        while self.position < len(self.input) and self.input[self.position] == '*':
            self.consume('*')
            self.parse_F()

    def parse_F(self):
        if self.position < len(self.input) and self.input[self.position] == '(':
            self.consume('(')
            self.parse_E()
            self.consume(')')
        elif self.position < len(self.input) and self.input[self.position].isalpha():
            self.consume(self.input[self.position])
        else:
            raise Exception(f"Unexpected character '{self.input[self.position]}'")

    def parse(self):
        self.parse_E()
        if self.position < len(self.input):
            raise Exception(f"Unexpected end of input")

# Test the parser
p = Parser("id+id*id")
p.parse()
print("Parsing succeeded")