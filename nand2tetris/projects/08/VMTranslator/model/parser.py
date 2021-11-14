from typing import List, Union
from model.command_type import CommandType


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


    # PURPOSE:  Removes all comments from a single line.
    # RETURNS:  string
    def preprocess_line(self, line: str) -> str:
        return line.split('//')[0].strip()


    # PURPOSE:  Removes comments from an input data.
    # RETURNS:  list of strings
    def preprocess_data(self, data: List[str]) -> List[str]:
        preprocessed_data = []
        for line in data:
            preprocessed_line = self.preprocess_line(line)
            # exclude strings with a length of 0 
            if preprocessed_line != '' :
                preprocessed_data.append(preprocessed_line)
        return preprocessed_data


    # PURPOSE:  Are there more commands in the input?
    # RETURNS:  boolean
    def hasMoreCommands(self) -> bool:
        return self.current_command_number < self.data_size - 1


    # PURPOSE:  Reads the next command from the input and makes it current command.
    #           Should be called only if hasMoreCommands is true. Initially there
    #           is no current command.
    # CHANGES:  self
    def advance(self) -> None:
        if self.hasMoreCommands():
            self.current_command_number += 1
            self.current_command = self.data[self.current_command_number]


    # PURPOSE:  Returns a constant representing the type of the current command.
    #           C_ARITHMETIC is returned for all the arithmetic/logical commands.
    # RETURNS:  CommandType: (C_ARITHMETIC, C_PUSH, C_POP, C_LABEL, C_GOTO, C_IF, 
    #           C_FUNCTION, C_RETURN, C_CALL).
    def commandType(self) -> CommandType:
        
        command = self.current_command.split(' ')[0]

        for _, m in CommandType.__members__.items():
            if command in m.value:
                return m


    # PURPOSE:  Returns the first argument of the current command. In the case of
    #           C_ARITHMETIC, the command itself (add, sub, etc.) is returned.
    #           Should not be called if the current command is C_RETURN.
    # RETURNS:  String or None
    def arg1(self) -> Union[str, None]:

        current_command_type = self.commandType()
        
        if current_command_type != CommandType.C_RETURN:

            if current_command_type == CommandType.C_ARITHMETIC:
                return self.current_command.split(' ')[0]
            
            else:
                return self.current_command.split(' ')[1]


    # PURPOSE:  Returns the second argument of the current command. Should be called
    #           only if the current command is C_PUSH, C_POP, C_FUNCTION, or C_CALL.
    # RETURNS: String or None
    def arg2(self) -> Union[str, None]:
        
        current_command_type = self.commandType()

        if current_command_type in [CommandType.C_PUSH, CommandType.C_POP, CommandType.C_FUNCTION, CommandType.C_CALL]:
            return self.current_command.split(' ')[2]