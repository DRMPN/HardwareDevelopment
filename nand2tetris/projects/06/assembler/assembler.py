import os
import sys
from typing import IO
from model.code import Code
from model.parser import Parser
from model.command_type import CommandType
from model.symbol_table import SymbolTable


# TODO: add decorators, or at least give it a try

# TODO: reforge

# TODO: add predefined symbols

# TODO: comment
def main() -> IO:

    # Ensures correct usage of the program
    if len(sys.argv) != 2:
        sys.exit("Usage: python(3) file.asm")


    # Reads data from an input file 
    try:
        input_file = open(sys.argv[1], 'r')
    except OSError:
        sys.exit("File '" + sys.argv[1] + "' cannot be found/opened")


    # Initializes parser with data
    parser = Parser(input_file.readlines())


    # Initialize symbol table
    symbol_table = SymbolTable()


    # Closes input file
    input_file.close()

    
    # Creates file to write data
    try:
        output_file = open(os.path.splitext(sys.argv[1])[0]+'.hack', 'w')
    except:
        sys.exit("Output file " + sys.argv[1] + " cannot be created")


    ### First pass
    # Builds symbol table
    ROM = 0
    for i in range(parser.data_size):
        parser.advance()
        if parser.commandType() == CommandType.L_COMMAND:
            symbol_table.addEntry(parser.symbol(), ROM)
        else:
            ROM += 1
            

    # Reset parser
    parser.current_command = None
    parser.current_command_number = -1
    

    ### Second pass
    # Parses input data and writes it to an output file
    # TODO: checks for a command type two times
    ram_var = 16
    for i in range(parser.data_size):
        parser.advance()

        # C command
        if parser.commandType() == CommandType.C_COMMAND:
            output_file.write(assemble_C(parser))
        
        # A command
        elif parser.commandType() == CommandType.A_COMMAND: 
            
            symbol = parser.symbol()

            # TODO: WTF TRY TO REFACTROR THIS
            # is number
            try:
                int(symbol)
                output_file.write(assemble_A(symbol))
                
            # is symbol and not a number 
            except ValueError:   
                
                # symbol is found
                if symbol_table.contains(symbol):
                    # get address of that symbol and assemble it
                    output_file.write(assemble_A(symbol_table.getAddress(symbol)))
                
                # symbol is not found
                else:
                    # add pair to the symbol table
                    symbol_table.addEntry(symbol, ram_var)
                    output_file.write(assemble_A(ram_var))
                    ram_var += 1
            
                
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