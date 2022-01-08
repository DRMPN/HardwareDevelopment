

# Removes all comments and white space from the input stream 
# and breaks it into Jack-language tokens, as specified by the Jack grammar.
class JackTokenizer():


    # NOTE: create dispose() method to close input file


    # Opens the input file/stream and gets ready to tokenize it.
    def __init__(self) -> None:

        # TODO: open input file
        #       read data
        #       close file
        #       create new file .xml

        # try:
        #   self.file = open(abs_path_to_file, 'r')
        # except OSError:
        #   sys.exit()

        self.current_token = None
    
    
    # PURPOSE:  Is there more tokens in the input?
    # RETURNS:  bool
    def hasMoreTokens() -> bool:
        # TODO: https://pynative.com/python-read-specific-lines-from-a-file/
        #       https://docs.python.org/3/library/functions.html?highlight=enumerate#enumerate
        pass


    # PURPOSE:  Gets the next token from the input and makes it current token.
    # NOTE: This method should only be called if hasMoreTokens() is true.
    #       Initially there is no current token. 
    def advance() -> None:
        # TODO: preprocess data
        #       ignore comments - // or /* */ or ... code ... // comment
        #       etc
        pass


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