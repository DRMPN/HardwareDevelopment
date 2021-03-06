# VM-to-Hack translator
# xxx.vm programs -> xxx.asm programs


import os
import sys
from model.parser import Parser
from model.code_writer import CodeWriter
from model.command_type import CommandType


# BUG FIXME HACK NOTE TODO


# Main logic:
#   constructs a Parser to handle input file
#   constructs a CodeWritter to handle output file
#   marches through the input file, parsing each line and generatic code 
def main():

    # Insures correct program usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python3 VMTranslator.py filename.vm")

    
    # Opens given file and reads it's data
    try:
        file = open(sys.argv[1], 'r')
        data = file.readlines()
        file.close()
    except OSError:
        sys.exit(f'ERROR: File {sys.argv[1]} cannot be found/opened.')
    

    # Creates and initializes parser object
    parser = Parser(data)


    # Creates and initializes CodeWriter object
    code_writer = CodeWriter(os.path.splitext(sys.argv[1])[0])


    # Main loop:
    for i in range(parser.data_size):

        parser.advance()

        command_type = parser.commandType()

        if command_type == CommandType.C_ARITHMETIC:
            code_writer.writeArithmetic(parser.arg1())
        else:
            code_writer.writePushPop(command_type.value, parser.arg1(), parser.arg2())

    
    # Closes code_writer
    code_writer.close()


    # Program exits with no error code:
    sys.exit(0)


if __name__ == "__main__":
    main()