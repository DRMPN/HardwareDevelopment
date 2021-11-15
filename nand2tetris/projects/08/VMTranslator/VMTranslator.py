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

# TODO: decide what was passed as argument, a directory or a single file 

def main():

    # Ensures correct program usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python3 VMTranslator.py directory/filename.vm")

    
    # Opens given directory/file and reads it's data

    data = []

    if os.path.isdir(sys.argv[1]):
        
        found = None

        for file in os.listdir(sys.argv[1]):
            if file.endswith('.vm'):
                
                found = True
                
                '''    
                    print(f'Inside: {sys.argv[1]}')
                    print(f'\tFound: {file}')
                '''
                test = (os.path.join(sys.argv[1], file))
                
                foo(data, test)

        if not found:
            sys.exit(f"ERROR: Passed directory '{sys.argv[1]}' contains not a single .vm file.")
        
    else:
        foo(data, sys.argv[1])
    

    print(data)


    # Creates and initializes parser object
    #parser = Parser(data)


    # Creates and initializes CodeWriter object
    # TODO: pass filename not a path to file print(os.path.splitext(sys.argv[1])[0].split('/')[-1])
    #code_writer = CodeWriter(os.path.splitext(sys.argv[1])[0])


    # Main loop:

    # TODO: rewrite

    """
    for i in range(parser.data_size):

        parser.advance()

        command_type = parser.commandType()

        '''
        for _, m in CommandType.__members__.items():
            if command in m.value:
                return m
        '''

        if command_type == CommandType.C_ARITHMETIC:
            code_writer.writeArithmetic(parser.arg1())
        else:
            code_writer.writePushPop(command_type.value, parser.arg1(), parser.arg2())
    """

    
    # Closes code_writer
    #code_writer.close()


    # Program exits with no error code:
    sys.exit(0)


# TODO: comment
def foo(data, path_to_file):
        try:
            file = open(path_to_file, 'r')
            data += file.readlines()
            file.close()     
        except OSError as io:
            print(io)
            sys.exit(f"ERROR: File '{path_to_file}' cannot be found/opened.")


if __name__ == "__main__":
    main()