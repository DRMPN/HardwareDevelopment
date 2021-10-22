from re import sub
from enum import Enum, auto

# TODO: comment
class CommandType(Enum):
    A_COMMAND = auto()
    C_COMMAND = auto()
    L_COMMAND = auto()


class Parser:
    # PURPOSE: TODO: comment
        # Opens the input file/steram and gets ready to parse it
    # ASSUMES: data is not None
    # TODO: maybe create a dictionary for current command?
    def __init__(self, data):
        
        self.data = self.preprocess(data)
        self.data_size = len(self.data) - 1
        
        self.current_command = None
        self.current_command_number = -1
    

    # PURPOSE: Removes whitespaces and comments from a single line
    # ASSUMES: line is a string encoded with ASCII
    # RETURNS: String
    def preprocess_line(self, line):
        # remove all whitespaces then split on comment symbol
        return sub("\s","", line).split('//')[0]


    # PURPOSE: Removes whitespaces and comments from an input data
    # RETURNS: List of Strings
    # CHANGES: self
    def preprocess(self, data):
        ppsd_data = []
        for l in data:
            ppsd_l = self.preprocess_line(l)
            # exclude strings with a length of 0 
            if ppsd_l != '' :
                ppsd_data.append(ppsd_l)
        return ppsd_data


    # PURPOSE: Are there more commands in the input?
    # RETURNS: Boolean
    def hasMoreCommands(self):
        return self.current_command_number < self.data_size


    # PURPOSE: Reads the next command from the input and makes it the current command
    # CHANGES: self
    def advance(self):
        if self.hasMoreCommands():
            self.current_command_number += 1
            self.current_command = self.data[self.current_command_number]
    

    # PURPOSE: Returns the type of the current command
    # RETURNS: CommandType
    def commandType(self):
        if self.current_command is not None:
            if self.current_command[0] == "0":
                return CommandType.A_COMMAND
            elif self.current_command[0] == "1":
                return CommandType.C_COMMAND
            else:
                return CommandType.L_COMMAND


    # symbol

    # dest

    # comp

    # jump