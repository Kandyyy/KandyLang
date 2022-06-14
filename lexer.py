import re
DIGITS = "0123456789"

class Error:
    def __init__(self, error,details) -> None:
        self.error = error
        self.details = details
    
    def print_string(self) -> str:
        return f"{self.error}: {self.details}"

class IllegalCharError(Error):
    def __init__(self, details) -> None:
        super().__init__("Illegal Character", details)

class Token:
    def __init__(self, token_type, value=None):
        self.token_type = token_type
        self.value = value

    def __repr__(self) -> str:
        x = [self.token_type,self.value]
        if self.value != None:
            return str(tuple(x))
        else:
            return str(tuple(x))


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

    def generateNums(self):
        nums = ""
        decimal = 0
        while self.current_char != None and self.current_char in DIGITS or self.current_char == ".":
            if self.current_char == ".":
                if decimal == 0:
                    decimal+=1
                else:
                    print("Incorrect decimal dot placement")
                    break
            nums+=self.current_char
            self.advance()
        return Token("INT",int(nums)) if decimal == 0 else Token("FLOAT",float(nums))
    
    def generateSymbols(self):
        symbol = ""
        while self.current_char!=None and re.match("[_a-zA-Z0-9]",self.current_char):
            symbol+=self.current_char
            self.advance()
        return Token("SYMBOL",symbol)

    def make_tokens(self):
        self.advance()
        tokens = []
        while self.current_char != None:
            if self.current_char in " \n":
                self.advance()
            if self.current_char in "+-*/":
                tokens.append(Token(self.current_char))
                self.advance()
            elif self.current_char in "(){},;:[]=":
                tokens.append(Token(self.current_char))
                self.advance()
            elif self.current_char in DIGITS:
                tokens.append(self.generateNums())
                self.advance()
            elif re.match("[_a-zA-Z]",self.current_char):
                tokens.append(self.generateSymbols())
                self.advance()
            else:
                charError = IllegalCharError(self.current_char)
                return [], charError
        return tokens,None

def run(char):
    lexer = Lexer(char)
    tokens, error = lexer.make_tokens()
    return tokens, error
