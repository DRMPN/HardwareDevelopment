# parser module
# parses each VM command into its lexical elements
from re import sub
from typing import List


# TODO: implement commandType class


# PURPOSE:  Handles the parsing of a single .vm file
#           Reads a VM command, parses the command line into its lexical
#           components, and provides convenient access to these components
#           Ignores all white space and comments
class Parser():

    # PURPOSE:  Opens the input file/stream and gets ready to parse it.
    # CHANGES:  self
    def __init__(self, data: List[str]) -> None:

        self.data = self.preprocess_data(data)
        self.data_size = len(self.data)

        self.current_command = None
        self.current_command_number = -1


    # PURPOSE:  Removes all white spaces and comments from a single line.
    # RETURNS:  string
    def preprocess_line(self, line: str) -> str:
        return sub("\s","", line).split('//')[0]


    # PURPOSE:  Removes all white spaces and comments from a data.
    # RETURNS:  list of strings
    def preprocess_data(self, data: List[str]) -> List[str]:
        pass


    # PURPOSE:  Are there more commands in the input?
    # RETURNS:  boolean
    def hasMoreCommands(self) -> bool:
        pass


    # PURPOSE:  Reads the next command from the input and makes it current command.
    #           Should be called only if hasMoreCommands is true. Initially there
    #           is no current command.
    # CHANGES:  self
    def advance(self) -> None:
        pass


    # PURPOSE:  Returns a constant representing the type of the current command.
    #           C_ARITHMETIC is returned for all the arithmetic/logical commands.
    # RETURNS:  class_name (C_ARITHMETIC, C_PUSH, C_POP, C_LABEL, C_GOTO, C_IF, 
    #           C_FUNCTION, C_RETURN, C_CALL).
    def commandType(self) -> None:
        pass


    # PURPOSE:  Returns the first argument of the current command. In the case of
    #           C_ARITHMETIC, the command itself (add, sub, etc.) is returned.
    #           Should not be called if the current command is C_RETURN.
    # RETURNS:  String
    def arg1(self) -> str:
        pass


    # PURPOSE:  Returns the second argument of the current command. Should be called
    #           only if the current command is C_PUSH, C_POP, C_FUNCTION, or C_CALL.
    # RETURNS: String
    def arg2(self) -> str:
        pass