# CodeWriter module
# writes the assembly code that implements the parsed command
import sys
from typing import IO


# PURPOSE:  Generates assembly code from the parsed VM command
# NOTE: Leaves comment for each command line that is being translated
class CodeWriter():

    # PURPOSE:  Opens the input file/stream and gets ready to write into it.
    # constructor (file/stream)
    def __init__(self, filename) -> IO:
        
        self.file = None
        
        try:
            self.file = open(f'{filename}.asm', 'w')
        except OSError:
            sys.exit(f'ERROR: File {filename} cannot be opened/created.')
            
        self.setFileName(filename)


    # PURPOSE:  Informes the code writer that the translation of a new VM
    #           file is started.
    def setFileName(self, filename: str) -> None:
        print(f'Translation has been started.\n{filename}.vm --> {filename}.asm')


    # PURPOSE:  Writes to the output file the assembly code that implements
    #           the given arithmetic command.
    # writeArithmetic (command(string))

    # TODO: check out command argument

    def writeArithmetic(self, command: str) -> IO:
        self.file.write(f'// {command}\n')
        c = translate_arithmetic(command)
        self.file.write(f'{c}\n')
    

    # PURPOSE:  Writes to the output file the assembly code that implements
    #           the given command, where command is either C_PUSH or C_POP.
    # writePushPop ( command( C_PUSH or C_POP, segment(string), index(int) ) )

    # TODO: check out command argument

    def writePushPop(self, command, segment: str, index: int) -> IO:
        self.file.write(f'// {command} {segment} {index} \n')
        c = translate_push(segment, index)
        self.file.write(f'{command}\n')


    # PURPOSE: Closes the output file.
    # close
    def close(self) -> None:
        self.file.close()
        print('Done.')

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


# PURPOSE:  Generates hack assembly code for add command
# RETURNS:  String
def translate_eq() -> str:
    ls = [ 
        # go to sp
        '@SP',
        # take sp address and go to y
        'A = M - 1',
        # negate y 
        'M = -M',
    ]
    '''
    @SP            // SP--
          M=M-1

           go to y and take it
          @SP
          A=M
          D=M

          @SP            // SP--
          M=M-1

           go to x and negate x - y
          @SP
          A=M
          D=M-D          // D is condition for jump

           
          @TRUE
          D;$condition
           false route
          @SP
          A=M
          M=$FalseValue
           end
          @END
          0;JMP

           true route
          (TRUE)
          @SP
          A=M
          M=$TrueValue

          (END)
          @SP            // SP++
          M=M+1
    '''

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