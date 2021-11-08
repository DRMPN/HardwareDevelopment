# CodeWriter module
# writes the assembly code that implements the parsed command
import sys
from random import randrange
from typing import IO


# TODO:
#   0.  Find abstraction for Hack generator funcitons
#   1.  Rewrite Hack generator functions using decorator


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
    def writeArithmetic(self, command: str) -> IO:
        self.file.write(f'// {command}\n')
        c = translate_arithmetic(command)
        self.file.write(f'{c}\n')
    

    # PURPOSE:  Writes to the output file the assembly code that implements
    #           the given command, where command is either C_PUSH or C_POP.
    # writePushPop ( command( C_PUSH or C_POP, segment(string), index(int) ) )
    def writePushPop(self, command, segment: str, index: int) -> IO:
        self.file.write(f'// {command} {segment} {index} \n')
        c = None
        if command =='push':
            c = translate_push(segment, index)
        elif command == 'pop':
            c = translate_pop(segment, index)
        self.file.write(f'{c}\n')


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
    if command in ['eq', 'gt','lt']:
        return translate_jump(command)
    if command == 'and':
        return translate_and()
    if command == 'or':
        return translate_or()
    if command == 'not':
        return translate_not()


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


# PURPOSE:  Generates hack assembly code for sub command
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


# PURPOSE:  Generates hack assembly code for neg command
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


# PURPOSE:  Generates hack assembly code for eq|gt|lt command
# RETURNS:  String

# TODO: scan for a better solution for random variables

def translate_jump(jump) -> str:
    jump = jump.upper()
    n = randrange(100)
    ls = [ 
        # go to sp
        '@SP',
        # move SP to y
        'M = M - 1',
        'A = M',
        # take value of  y 
        'D = M',
        # move SP to x
        '@SP',
        'M = M - 1',
        'A = M',
        # at x calculate x - y
        'D = M - D',
        # compose 'unique' label
        f'@TRUE{jump}{n}',
        # D is condition for jump
        f'D; J{jump}',
        # false route
        '@SP',
        'A = M',
        'M = 0',
        f'@END{jump}{n}',
        '0; JMP',
        # true route
        f'(TRUE{jump}{n})',
        '@SP',
        'A = M',
        'M = -1',
        # end 
        f'(END{jump}{n})',
        # increase SP
        '@SP',
        'M = M + 1'
    ]

    s = '\n'.join(ls)

    return s


# PURPOSE:  Generates hack assembly code for and command
# RETURNS:  String
def translate_and():
    
    ls = [
        # move SP to y
        '@SP',
        'M = M - 1',
        'A = M',
        # take y
        'D = M',
        # go to x
        'A = A - 1',
        # compute (x and y) then store it in x
        'M = D & M',
    ]
    
    s = '\n'.join(ls)
    
    return s


# PURPOSE:  Generates hack assembly code for or command
# RETURNS:  String
def translate_or():
        
    ls = [
        # move SP to y
        '@SP',
        'M = M - 1',
        'A = M',
        # take y
        'D = M',
        # go to x
        'A = A - 1',
        # compute (x and y) then store it in x
        'M = D | M',
    ]
    
    s = '\n'.join(ls)
    
    return s


# PURPOSE:  Generates hack assembly code for not command
# RETURNS:  String
def translate_not():
    ls = [ 
        # go to sp
        '@SP',
        # take sp address and go to y
        'A = M - 1',
        # invert y 
        'M = !M',
    ]

    s = '\n'.join(ls)

    return s


# PURPOSE:  NOTE: only works with push constant N
# RETURNS:  String

# BUG:  there might be a bug somewhere

def translate_push(arg1, arg2) -> str:
    
    if arg1 == 'constant':
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
    elif arg1 == 'temp':

        try:
            n = 5 + int(arg2)
        except:
            sys.exit(f'Translation error, cannot resolve {arg2} symbol.')

        ls = [
            # go to constant
            f'@{n}',
            # take constant
            'D = M',
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
    else:

        m_seg = {
            'local':'LCL',
            'argument':'ARG',
            'this':'THIS',
            'that':'THAT'
        }
        
        ls = [
            # save second argument
            f'@{arg2}',
            'D = A',
            # go to labeled memory segment
            f'@{m_seg[arg1]}',
            # go to computed address of required memory segment
            'A = M + D',
            # take data
            'D = M',
            # go to SP and push data
            '@SP',
            'A = M',
            'M = D',
            # increase SP
            '@SP',
            'M = M + 1'
        ]

    s = '\n'.join(ls)

    return s


# PURPOSE:  Generates hack assembly code for pop command 
def translate_pop(arg1, arg2):

    if arg1 == 'temp':
        
        n = 5 + int(arg2)

        ls = [
            # move SP backwards
            '@SP',
            'M = M - 1',
            # go to data
            'A = M',
            # take data
            'D = M',
            # pop data to requred memory segment
            f'@{n}',
            'M = D'
        ]

    else:

        m_seg = {
                'local':'LCL',
                'argument':'ARG',
                'this':'THIS',
                'that':'THAT'
            }

        ls = [
            # get second argument
            f'@{arg2}',
            'D = A',
            # go to labeled memory segment
            f'@{m_seg[arg1]}',
            # compute address of required memory segment
            'D = D + M',
            # save address of required memory segment
            '@R13',
            'M = D',
            # move SP backwards
            '@SP',
            'M = M - 1',
            # go to data
            'A = M',
            # take data
            'D = M',
            # pop data to requred memory segment
            '@R13',
            'A = M',
            'M = D'
        ]
    
    s = '\n'.join(ls)
    return s