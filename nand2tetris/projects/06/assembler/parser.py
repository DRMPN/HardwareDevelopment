from enum import Enum, auto


class CommandType(Enum):
    A_COMMAND = auto()
    C_COMMAND = auto()
    L_COMMAND = auto()


class Parser:


    # Opens the input file/steram and gets ready to parse it
    # TODO: maybe create a dictionary for current command?
    def __init__(self, data):
        self.current_command_num = 0
        self.current_command = ""
        self.data = data
        

    # Are there more commands in the input?
    def hasMoreCommands(self):
        return len(self.data) != 0


    # Reads the next command from the input and makes it the current command
    # TODO: add logic to parse it
    def advance(self):
        if self.hasMoreCommands():
            self.current_command = self.data[self.current_command_num]
            self.current_command_num += 1
    

    # Returns the type of the current command
    def commandType(self):
        pass


    def debug(self):
        return self.current_command

    # commandType

    # symbol

    # dest

    # comp

    # jump