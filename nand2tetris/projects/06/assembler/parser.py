from re import sub
from enum import Enum, auto


class CommandType(Enum):
    A_COMMAND = auto()
    C_COMMAND = auto()
    L_COMMAND = auto()


class Parser:


    # PURPOSE: Opens the input file/steram and gets ready to parse it
    # TODO: maybe create a dictionary for current command?
    def __init__(self, data):
        self.current_command = None
        self.current_command_type = None
        self.current_command_number = 0
        self.data = data
    
    # PURPOSE: Removes whitespaces and comments from a single line
    # ASSUMES: line is a string encoded with ASCII
    # RETURNS: String
    def preprocess(self, line):
        # remove all whitespaces then split on comment symbol
        rm_ws = sub("\s","", line)
        rm_comments = rm_ws.split('//')[0]
        return rm_comments


    # PURPOSE: Are there more commands in the input?
    # RETURNS: Boolean
    def hasMoreCommands(self):
        return len(self.data) != 0


    # PURPOSE: Reads the next command from the input and makes it the current command
    # TODO: add logic to parse it
    def advance(self):
        if self.hasMoreCommands():
            self.current_command = self.data[self.current_command_number]
            self.current_command_number += 1
    

    # PURPOSE: Returns the type of the current command
    # RETURNS: CommandType
    def commandType(self):
        # TODO: throw an error/exception "No current command" or "Current command is empty"
        # TODO: self.current_command_type
        pass


    def debug(self):
        for i in self.data:
            print(self.preprocess(i))

    # commandType

    # symbol

    # dest

    # comp

    # jump