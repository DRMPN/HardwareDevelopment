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
        self.current_token_number = -1

        # TODO: refactor
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
            self.data_size += 1
            self.data.append(p_line)

    
    # PURPOSE:  Is there more tokens in the input?
    # RETURNS:  bool
    def hasMoreTokens(self) -> bool:
        return self.current_token_number < self.data_size - 1


    # PURPOSE:  Gets the next token from the input and makes it current token.
    # NOTE: This method should only be called if hasMoreTokens() is true.
    #       Initially there is no current token. 
    def advance(self) -> None:
        self.current_token_number += 1
        # TODO:


    # PURPOSE:  Returns the type of current token.
    # RETURNS:  token_type
    def tokenType() -> None:
        # TODO:
        #       class token_type(Enum): ...
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


if __name__ == "__main__":
    main()