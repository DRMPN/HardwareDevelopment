# main module
# VM-to-Hack translator
# xxx.vm programs -> xxx.asm programs
# drives the process
import os
import sys
from model.parser import Parser
from model.code_writer import CodeWriter
from model.command_type import CommandType


# BUG FIXME HACK NOTE TODO


# Main logic:
# constructs a Parser to handle input file
# constructs a CodeWritter to handle output file
# marches through the input file, parsing each line and generatic code 


# TODO:
# 0. Implement preprocess
# 1. Implement the nine stack arithmetic and logical commands
# 2. Implement the push constant x command


# TODO:
# Rewrite functions using decorator


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

        # TODO: write logic to parse current command

        # NOTE: placeholer
        if command_type == CommandType.C_ARITHMETIC:
            c = translate_arithmetic(parser.arg1())
            code_writer.writeArithmetic(c)
        else:
            c = translate_push(parser.arg1(), parser.arg2())
            code_writer.writePushPop(c, parser.arg1(), parser.arg2())

    
    # Closes code_writer
    code_writer.close()


    # Program exits with no error code:
    sys.exit(0)


# PURPOSE:  Translates nine arithmetic commands
# RETURNS:  String
def translate_arithmetic(command: str) -> str:
    if command == 'add':
        return translate_add()
    if command == 'sub':
        return translate_sub()
    if command == 'neg':
        return translate_neg()


# PURPOSE:  Generates hack assembly code for add command
# RETURNS:  String
def translate_add() -> str:
    ls = [ 
        # go to sp
        '@SP',
        # take sp address and go to y
        'A = M - 1',
        # take y 
        'D = M',
        # go to x
        'A = A - 1',
        # calculate x + y then store to x
        'M = D + M',
        # move SP backward
        '@SP',
        'M = M - 1'
    ]

    s = '\n'.join(ls)

    return s


# PURPOSE:  Generates hack assembly code for add command
# RETURNS:  String
def translate_sub() -> str:
    ls = [ 
        # go to sp
        '@SP',
        # take sp address and go to y
        'A = M - 1',
        # take y 
        'D = M',
        # go to x
        'A = A - 1',
        # calculate x + y then store to x
        'M = M - D',
        # move SP backward
        '@SP',
        'M = M - 1'
    ]

    s = '\n'.join(ls)

    return s


# PURPOSE:  Generates hack assembly code for add command
# RETURNS:  String
def translate_neg() -> str:
    ls = [ 
        # go to sp
        '@SP',
        # take sp address and go to y
        'A = M - 1',
        # negate y 
        'M = -M',
    ]

    s = '\n'.join(ls)

    return s


# PURPOSE:  NOTE: only works with push constant N
# RETURNS:  string
def translate_push(arg1, arg2) -> str:
    ls = [
        # go to constant
        f'@{arg2}',
        # take constant
        'D = A',
        # go to sp
        '@SP',
        # push constant
        'A = M',
        'M = D',
        # go to sp
        '@SP',
        # increase sp
        'M = M + 1'
    ]

    s = '\n'.join(ls)

    return s


if __name__ == "__main__":
    main()