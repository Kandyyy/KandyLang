
LBRAC = "LBRAC"
RBRAC = "BRAC"
PLUS = "PLUS"

class Token:
    def __init__(self, token_type, value=None):
        self.token_type = token_type
        self.value = value

    def __repr__(self) -> str:
        if self.value != None:
            return f"{self.token_type}:{self.value}"
        else:
            return "No value"


class Lexer:
    def __init__(self, char):
        self.char = char
        self.current_char = None
        self.current_pos = -1

    def advance(self):
        self.current_pos+=1
        if self.current_pos < len(self.char):
            self.current_char = self.char[self.current_pos]
        else:
            self.current_char = None

    def make_tokens(self):
        self.advance()
        tokens = []
        while self.current_char != None:
            if self.current_char == " \t":
                self.advance()
            if self.current_char == "+":
                tokens.append(Token(PLUS, self.current_char))
                self.advance()
        return tokens

def run(char):
    lexer = Lexer(char)
    tokens = lexer.make_tokens()
    return tokens

print(Token(PLUS))