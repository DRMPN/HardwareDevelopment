import sys
from enum import Enum, auto


class LexicalElement(Enum):
    KEYWORD = auto()
    SYMBOL = auto()
    IDENTIFIER = auto()
    INT_CONST = auto()
    STRING_CONST = auto()


# Removes all comments and white space from the input stream 
# and breaks it into Jack-language tokens, as specified by the Jack grammar.
class JackTokenizer():


    # Opens the input file/stream and gets ready to tokenize it.
    def __init__(self, path) -> None:

        self.data = []
        self.data_size = 0

        self.current_token = None
        self.current_token_number = 0

        # TODO: maybe refactor?
        try:
            with open(path, 'r') as f:
                for _, line in enumerate(f):
                    self.preprocess_line(line)
        except OSError:
            sys.exit(f"Unable to open {path}")

    
    # PURPOSE:  removes Jack comments and trailing whitespaces
    # CHANGES:  data, data_size
    # BUG:  DOESN'T REMOVE BLOCK COMMENTS
    #       IN SQUARE DIRECTORY
    def preprocess_line(self, line: str) -> None:
        # TODO: line.startswith('//') etc
        p_line = line.split('//')[0].split('/*')[0].strip() # remove comments
        if p_line != '':
            self.data_size += len(p_line)
            self.data += p_line

    
    # PURPOSE:  Is there more tokens in the input?
    # RETURNS:  bool
    def hasMoreTokens(self) -> bool:
        return self.current_token_number < self.data_size


    # PURPOSE:  Gets the next token from the input and makes it the current token.
    # NOTE: This method should only be called if hasMoreTokens() is true.
    #       Initially there is no current token. 
    # CHANGES:  current_token, current_token_number
    def advance(self) -> None:
        self.current_token = str()
        current_char = self.data[self.current_token_number]
        # WHITESPACE
        if current_char.isspace():
            self.current_token_number += 1
            self.advance()
        # STRING_CONST
        elif current_char == '"':
            quotes = 0
            while quotes < 2:
                if current_char == '"': quotes += 1
                self.current_token += current_char
                self.current_token_number += 1
                current_char = self.data[self.current_token_number]
        # KEYWORD, IDENTIFIER or INT_CONST
        elif current_char.isalpha() or current_char.isdigit():
            while current_char.isalpha() or current_char.isdigit() or current_char == '_':
                self.current_token += current_char
                self.current_token_number += 1
                current_char = self.data[self.current_token_number]
        # SYMBOL
        else:
            self.current_token = current_char
            self.current_token_number += 1


    # PURPOSE:  Returns the type of current token.
    # RETURNS:  token_type
    def tokenType(self) -> LexicalElement:
        # STRING_CONST
        if self.current_token[0] == '"': return LexicalElement.STRING_CONST
        # INT_CONST in range 0 ... 32767
        elif self.current_token[0].isdigit(): return LexicalElement.INT_CONST
        # KEYWORD, IDENTIFIER
        elif self.current_token[0].isalpha():
            keyword = ['class', 'constructor', 'function', 'method', 'field', 'static', 'var', 'int', 'char', 'boolean',
                        'void', 'true', 'false', 'null', 'this', 'let', 'do', 'if', 'else', 'while', 'return']
            if self.current_token in keyword: return LexicalElement.KEYWORD
            else: return LexicalElement.IDENTIFIER
        # SYMBOL
        else: return LexicalElement.SYMBOL


    # PURPOSE:  Returns the keyword which is the current token. 
    # NOTE: Should be called only when tokenType() is KEYWORD
    # RETURNS:  string
    def keyWord(self) -> str:
        return self.current_token


    # PURPOSE:  Returns the character which is the current token. 
    # NOTE: Should be called onlywhen tokenType() is SYMBOL.
    # RETURNS:  char
    def symbol(self) -> chr:
        if self.current_token == '<': return '&lt;'
        elif self.current_token == '>': return '&gt;'
        elif self.current_token == '"': return '&quot;'
        elif self.current_token == '&': return '&amp;'
        else: return self.current_token


    # PURPOSE:  Returns the identifier which is the current token. 
    # NOTE: Should be called onlywhen tokenType() is IDENTIFIER.
    # RETURNS:  string
    def identifier(self) -> str:
        return self.current_token


    # PURPOSE:  Returns the integer value of the current token. 
    # NOTE: Should be called only when tokenType() is INT_CONST.
    # RETURNS:  int
    def intVal(self) -> int:
        return int(self.current_token)


    # Returns the string value of the currenttoken, without the double quotes.
    # NOTE: Should be called only when tokenType() is STRING_CONST.
    def stringVal(self) -> str:
        return self.current_token[1:-1]