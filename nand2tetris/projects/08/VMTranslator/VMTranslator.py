# VM-to-Hack translator
# xxx.vm programs -> xxx.asm programs


import os
import sys
from typing import List
from model.parser import Parser
from model.code_writer import CodeWriter
from model.command_type import CommandType


# BUG FIXME HACK NOTE TODO


# Main logic:
#   constructs a Parser to handle input file
#   constructs a CodeWritter to handle output file
#   marches through the input file, parsing each line and generatic code 


def main():

    # Ensures correct program usage
    if len(sys.argv) != 2:
        sys.exit("USAGE: \t$ python3 VMTranslator.py directory\n\t$ python3 VMTranslator.py file.vm")


    # Initializes data
    data = []


    # Get absolute path to a passed argument file/folder
    abs_path_to_arg = os.path.abspath(sys.argv[1])


    # If passed argument is a folder, then for every .vm file inside read it's data
    if os.path.isdir(abs_path_to_arg):
        
        found = False

        for file in os.listdir(abs_path_to_arg):
            if file.endswith('.vm'):
                found = True

                path_to_file = os.path.join(abs_path_to_arg, file)

                read_file(data, path_to_file)

        if not found:
            sys.exit(f"ERROR: Passed directory '{abs_path_to_arg}' contains not a single .vm file.")

    # If passed argument is a file, just read it's data
    else:
        read_file(data, abs_path_to_arg)
    

    # Creates and initializes parser object with data
    parser = Parser(data)


    # Creates and initializes CodeWriter object
    code_writer = CodeWriter(abs_path_to_arg)


    # Main loop:

    # TODO: rewrite

    
    for i in range(parser.data_size):

        parser.advance()

        command_type = parser.commandType()

        # TODO: reforge
        '''
        for _, m in CommandType.__members__.items():
            if command in m.value:
                return m
        '''

        if command_type == CommandType.C_ARITHMETIC:
            code_writer.writeArithmetic(parser.arg1())
        elif command_type in [CommandType.C_PUSH, CommandType.C_POP]:
            code_writer.writePushPop(command_type.value, parser.arg1(), parser.arg2())
        elif command_type == CommandType.C_LABEL:
            code_writer.writeLabel(parser.arg1())
        elif command_type == CommandType.C_GOTO:
            code_writer.writeGoto(parser.arg1())
        elif command_type == CommandType.C_IF:
            code_writer.writeIf(parser.arg1())
        elif command_type == CommandType.C_FUNCTION:
            code_writer.writeFunction(parser.arg1(), parser.arg2())
        elif command_type == CommandType.C_CALL:
            pass
        else:
            code_writer.writeReturn()
    
    # Closes code_writer
    code_writer.close()


    # Program exits with no error code:
    sys.exit(0)


# PURPOSE:  Opens file by given path, reads it's data and concatenates it with passed data
# RETURNS:  None  
# CHANGES:  data
def read_file(data: List[str], path_to_file: str) -> None:
        try:
            file = open(path_to_file, 'r')
            data += file.readlines()
            file.close()     
        except OSError:
            sys.exit(f"ERROR: File '{path_to_file}' cannot be found/opened.")


if __name__ == "__main__":
    main()