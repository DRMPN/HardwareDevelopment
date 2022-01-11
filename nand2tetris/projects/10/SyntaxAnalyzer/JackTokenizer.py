import os
import sys

# Removes all comments and white space from the input stream 
# and breaks it into Jack-language tokens, as specified by the Jack grammar.
class JackTokenizer():


    # Opens the input file/stream and gets ready to tokenize it.
    def __init__(self, path) -> None:

        self.data = []
        self.data_size = 0

        self.current_token = None
        self.current_token_number = 0

        # TODO: add file creation and refactor?
        try:
            with open(path, 'r') as f:
                for _, line in enumerate(f):
                    self.preprocess_line(line)
        except OSError:
            sys.exit("Error")

    
    # PURPOSE:  removes Jack comments and trailing whitespaces
    # CHANGES:  data, data_size
    def preprocess_line(self, line: str) -> None:
        p_line = line.split('//')[0].split('/*')[0].strip() # remove comments
        if p_line != '':
            self.data_size += len(p_line)
            self.data += p_line

    
    # PURPOSE:  Is there more tokens in the input?
    # RETURNS:  bool
    def hasMoreTokens(self) -> bool:
        return self.current_token_number < self.data_size


    # PURPOSE:  Gets the next token from the input and makes it the current token.
    # CHANGES:  current_token, current_token_number
    # NOTE: This method should only be called if hasMoreTokens() is true.
    #       Initially there is no current token. 
    def advance(self) -> None:
        self.current_token = []
        current_char = self.data[self.current_token_number]
        
        # WHITESPACE
        if current_char.isspace():
            self.current_token_number += 1
            self.advance()
        
        # STRING_CONST
        elif current_char == '"':
            quotes = 0
            while quotes < 2:
                if current_char == '"':
                    quotes += 1
                self.current_token.append(current_char)
                self.current_token_number += 1
                current_char = self.data[self.current_token_number]
        
        # KEYWORD, IDENTIFIER or INT_CONST
        elif current_char.isalpha() or current_char.isdigit():
            while current_char.isalpha() or current_char.isdigit():
                self.current_token.append(current_char)
                self.current_token_number += 1
                current_char = self.data[self.current_token_number]
        
        # SYMBOL
        else:
            self.current_token = list(current_char)
            self.current_token_number += 1


    # PURPOSE:  Returns the type of current token.
    # RETURNS:  token_type
    def tokenType(self) -> None:
        # TODO: class token_type(Enum): ...
        
        #   keyword = ['class', 'constructor', 'function', 'method', 'field', 'static', 'var', 'int', 'char', 'boolean',
        #              'void', 'true', 'false', 'null', 'this', 'let', 'do', 'if', 'else', 'while', 'return']
        #   symbol = ['{', '}', '(', ')', '[', ']', '.', ',', ';', '+', '-', '*', '/', '&', '|', '<', '>', '=', '~']
        #   integerConstant = A decimal number in the range 0 ... 32767
        #   StringConstant =  '"' A sequence of Unicode characters not including double quote or newline '"'
        #   identifier = A sequence of letters, digits, and underscore ('_') not starting with a digit.
        pass

# keyword

# symbol

# identifyer

# intVal

# stringVal


# NOTE: placeholder
def main():
    abs_path_to_file = os.path.abspath(sys.argv[1])
    print(abs_path_to_file)
    JT = JackTokenizer(abs_path_to_file)
    for i in range(500):
        if JT.hasMoreTokens():
            JT.advance()
            print(JT.current_token)


if __name__ == "__main__":
    main()