from model.command_type import CommandType
from re import sub


# PURPOSE: Parses the given input stream
class Parser:

    # Initialize
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
            if self.current_command[0] == "@":
                return CommandType.A_COMMAND
            elif self.current_command[0] == "(":
                return CommandType.L_COMMAND
            else:
                return CommandType.C_COMMAND


    # TODO: rework later
    # PURPOSE: Returns the symbol or decimal Xxx of the current command @Xxx or (Xxx)
    # RETURNS: String
    def symbol(self):
        com_type = self.commandType()
        if com_type == CommandType.A_COMMAND or com_type == CommandType.L_COMMAND:
            return "TestSymbol"


    # PURPOSE: Returns the dest mnemonic in the current C-command
    # RETURNS: String
    def dest(self):
        if self.commandType() == CommandType.C_COMMAND:
            return self.current_command.split('=')[0]


    # PURPOSE: Returns the comp mnemonic in the current C-command
    # RETURNS: String
    def comp(self):
        if self.commandType() == CommandType.C_COMMAND:
            return str(self.current_command.split('=')[1].split(';')[0])


    # PURPOSE: Retuns the jump mnemonic in the current C-command
    # RETURNS: String
    def jump(self):
        if self.commandType() == CommandType.C_COMMAND:
            try:
                return self.current_command.split(';')[1]
            except IndexError:
                pass