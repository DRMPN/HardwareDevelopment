from re import sub
from typing import List
from model.command_type import CommandType


# PURPOSE: Parses the given input stream
class Parser:

    # Initialize
    def __init__(self, data: List[str]):
        
        self.data = self.preprocess(data)
        self.data_size = len(self.data)
        
        self.current_command = None
        self.current_command_number = -1
    

    # PURPOSE: Removes whitespaces and comments from a single line
    # ASSUMES: line is a string encoded with ASCII
    # RETURNS: String
    def preprocess_line(self, line: str) -> str:
        # remove all whitespaces then split on comment symbol
        return sub("\s","", line).split('//')[0]


    # PURPOSE: Removes whitespaces and comments from an input data
    # RETURNS: List of Strings
    # CHANGES: self
    def preprocess(self, data: List[str]) -> List[str]:
        preprocessed_data = []
        for line in data:
            preprocessed_line = self.preprocess_line(line)
            # exclude strings with a length of 0 
            if preprocessed_line != '' :
                preprocessed_data.append(preprocessed_line)
        return preprocessed_data


    # PURPOSE: Are there more commands in the input?
    # RETURNS: Boolean
    def hasMoreCommands(self) -> bool:
        return self.current_command_number < self.data_size - 1


    # PURPOSE: Reads the next command from the input and makes it the current command
    # CHANGES: self
    def advance(self) -> None:
        if self.hasMoreCommands():
            self.current_command_number += 1
            self.current_command = self.data[self.current_command_number]
    

    # PURPOSE: Returns the type of the current command
    # RETURNS: CommandType
    def commandType(self) -> CommandType:
        if self.current_command is not None:
            if self.current_command[0] == "@":
                return CommandType.A_COMMAND
            elif self.current_command[0] == "(":
                return CommandType.L_COMMAND
            else:
                return CommandType.C_COMMAND


    # TODO: rework later
    # PURPOSE: Returns the symbol or decimal Xxx of the current command @Xxx or (Xxx)
    # RETURNS: String
    def symbol(self) -> str:
        com_type = self.commandType()
        if com_type == CommandType.A_COMMAND:
            return self.current_command.split('@')[1]
        if com_type == CommandType.L_COMMAND:
            return "TestSymbol"


    # PURPOSE: Returns the dest mnemonic in the current C-command
    # RETURNS: String
    def dest(self) -> str:
        if self.commandType() == CommandType.C_COMMAND:
            return self.current_command.split('=')[0]


    # PURPOSE: Returns the comp mnemonic in the current C-command
    # RETURNS: String
    def comp(self) -> str:
        if self.commandType() == CommandType.C_COMMAND:
            return str(self.current_command.split('=')[1].split(';')[0])


    # PURPOSE: Retuns the jump mnemonic in the current C-command
    # RETURNS: String
    def jump(self) -> str:
        if self.commandType() == CommandType.C_COMMAND:
            try:
                return self.current_command.split(';')[1]
            except IndexError:
                pass