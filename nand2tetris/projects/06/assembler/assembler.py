import os
import sys
from typing import IO
from model.code import Code
from model.parser import Parser
from model.command_type import CommandType


# TODO: add decorators, or at least give it a try

# TODO: comment
def main() -> IO:

    # Ensures correct usage of the program
    if len(sys.argv) != 2:
        sys.exit("Usage: python(3) file.asm")


    # Reads data from an input file 
    try:
        input_file = open(sys.argv[1], 'r')
    except FileNotFoundError:
        sys.exit("File " + sys.argv[1] + " cannot be found")


    # Initializes parser with data
    parser = Parser(input_file.readlines())


    # Closes input file
    input_file.close()

    
    # Creates file to write data
    try:
        output_file = open(os.path.splitext(sys.argv[1])[0]+'.hack', 'w')
    except:
        sys.exit("Output file " + sys.argv[1] + " cannot be created")


    # Parses input data and writes it to an output file
    # TODO: checks for a command type two times
    for i in range(parser.data_size):
        parser.advance()
        if parser.commandType() == CommandType.A_COMMAND:
            output_file.write(assemble_A(parser.symbol()))
        elif parser.commandType() == CommandType.C_COMMAND:
            output_file.write(assemble_C(parser))
        
        # TODO: L command
        
        else:
            pass        
    
    
    # Closes output file
    output_file.close()


# PURPOSE: Converts decimal number represented as a string to a binary number as string
# ASSUMES: Input is a string
# RETURNS: String
def int_to_bin(dec_str: str) -> str:
    return bin(int(dec_str))[2:]


# PURPOSE: Assembles A command
# RETUENS: String
def assemble_A(a_command: str) -> str:
    com = int_to_bin(a_command)
    return (16 - len(com)) * '0' + com + '\n'


# PURPOSE: Assembles C command
# ASSUMES: It does not take double memory space for parser xD
# RETURNS: String
def assemble_C(parser: Parser) -> str:

    c = parser.comp()
    d = parser.dest()
    j = parser.jump()

    co = Code.comp(c)
    de = Code.dest(d)
    ju = Code.jump(j)

    return '111' + co + de + ju + '\n'


if __name__ == '__main__':
    main()