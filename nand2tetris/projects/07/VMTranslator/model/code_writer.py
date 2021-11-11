# CodeWriter module
# writes the assembly code that implements the parsed command
import sys
from time import time
from typing import IO


# TODO:
#   0.  Find abstraction for Hack generator funcitons

#       Combine     push    constant + temp + pointer + static
#       Combine     pop     temp + pointer + static

#   1.  Rewrite Hack generator functions using decorator


# PURPOSE:  Generates assembly code from the parsed VM command
# NOTE: Leaves comment for each command line that is being translated
class CodeWriter():

    # PURPOSE:  Opens the input file/stream and gets ready to write into it.
    # constructor (file/stream)
    def __init__(self, path_to_file) -> IO:
        
        self.file = None
        self.filename = path_to_file.split('/')[-1]
        
        try:
            self.file = open(f'{path_to_file}.asm', 'w')
        except OSError:
            sys.exit(f'ERROR: File {path_to_file}.asm cannot be opened/created.')
            
        self.setFileName(path_to_file)


    # PURPOSE:  Informes the code writer that the translation of a new VM
    #           file is started.
    def setFileName(self, filename: str) -> None:
        print(f'Translation has been started.\n{filename}.vm --> {filename}.asm')


    # PURPOSE:  Writes to the output file the assembly code that implements
    #           the given arithmetic command.
    # writeArithmetic (command(string))
    def writeArithmetic(self, command: str) -> IO:
        self.file.write(f'// {command}\n')
        com = translate_arithmetic(command)
        self.file.write(f'{com}\n')
    

    # PURPOSE:  Writes to the output file the assembly code that implements
    #           the given command, where command is either C_PUSH or C_POP.
    # writePushPop ( command( C_PUSH or C_POP, segment(string), index(int) ) )
    def writePushPop(self, command, segment: str, index: int) -> IO:
        self.file.write(f'// {command} {segment} {index} \n')
        com = None
        if command =='push':
            com = translate_push(segment, index, self.filename)
        elif command == 'pop':
            com = translate_pop(segment, index, self.filename)
        self.file.write(f'{com}\n')


    # PURPOSE: Closes the output file.
    # close
    def close(self) -> None:
        self.file.close()
        print('Done.')


# PURPOSE:  Translates nine arithmetic commands
# RETURNS:  String
# NOTE: maybe refactor it? huh O_o? 
def translate_arithmetic(command: str) -> str:

    if command in ['neg','not']:
        return translate_unary(command)

    if command in ['add','sub','and','or']:
        return translate_binary(command)

    if command in ['eq', 'gt','lt']:
        return translate_jump(command)   


# PURPOSE:  Generates Hack assembly code for 'and' 'sub' 'and' 'or' commands
# RETURNS:  String

# TODO: custom decorator

def translate_binary(command: str) -> str:
    # Prepare two variables
    first_part = [
        # move SP to y
        '@SP',
        'M = M - 1',
        'A = M',
        # take y 
        'D = M',
        # go to x
        'A = A - 1'
    ]

    # Compute {command} and store it inside x
    second_part = {
        'add':'M = D + M',
        'sub':'M = M - D',
        'and':'M = D & M',
        'or':'M = D | M'
    }[command]

    first_part.append(second_part)

    return '\n'.join(first_part)


# PURPOSE:  Generates Hack assembly code for 'neg' 'not' commands
# RETURNS:  String

# TODO: custom decorator

def translate_unary(command: str) -> str:
    # Prepare single variable
    first_part = [
        # go to sp
        '@SP',
        # take sp address and go to y
        'A = M - 1'
    ]

    # Compute {command}
    second_part = {
        'neg':'M = -M',
        'not':'M = !M'
    }[command]

    first_part.append(second_part)

    return '\n'.join(first_part)


# PURPOSE:  Generates hack assembly code for eq|gt|lt command
# RETURNS:  String

# TODO: custom decorator

def translate_jump(jump: str) -> str:
    jump = jump.upper()
    name = jump + str(hash(time()))
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
        f'@TRUE{name}',
        # D is condition for jump
        f'D; J{jump}',
        # false route
        '@SP',
        'A = M',
        'M = 0',
        f'@END{name}',
        '0; JMP',
        # true route
        f'(TRUE{name})',
        '@SP',
        'A = M',
        'M = -1',
        # end 
        f'(END{name})',
        # increase SP
        '@SP',
        'M = M + 1'
    ]

    return '\n'.join(ls)

# PURPOSE:  Generates hack assembly code for a generic push command 
# RETURNS:  String

# TODO: Custom decorator

def translate_push(arg1: str, arg2: str, filename: str) -> str:

    pointer = {'0':'THIS', '1':'THAT'}.get(arg2)

    foo = {
        'temp': [
            # go to data
            f'@{5 + int(arg2)}', 
            # take data
            'D = M'
            ],
        'static': [f'@{filename}.{arg2}', 'D = M'],
        'pointer': [f'@{pointer}','D = M'],
        'constant': [f'@{arg2}','D = A']
    }

    bar = {
        'local':'LCL',
        'argument':'ARG',
        'this':'THIS',
        'that':'THAT'
    }.get(arg1)

    bar = [
        # take value
        f'@{arg2}',
        'D = A',
        # go to data
        f'@{bar}',
        'A = M + D',
        # take data
        'D = M'
        ]

    first_part = foo.get(arg1, bar)

    second_part = [
        # go to SP and push data
        '@SP',
        'A = M',
        'M = D',
        # increase SP
        '@SP',
        'M = M + 1'
    ]
    
    first_part.extend(second_part)

    return '\n'.join(first_part)


def tr_bar(arg1, arg2, filename):
    
    main_part = [
        # move SP backwards
        '@SP',
        'M = M - 1',
        # go to data
        'A = M',
        # take data
        'D = M'
    ]

    pointer = {'0':'THIS', '1':'THAT'}.get(arg2)

    foo = {
        'temp': [f'@{5 + int(arg2)}','M = D'],
        'static': [f'@{filename}.{arg2}', 'M = D'],
        'pointer': [f'@{pointer}', 'M = D']
    }

    bar = {
        'local':'LCL',
        'argument':'ARG',
        'this':'THIS',
        'that':'THAT'
    }.get(arg1)

    before = [
        # get second argument
        f'@{arg2}',
        'D = A',
        # go to labeled memory segment
        f'@{bar}',
        # compute address of required memory segment
        'D = D + M',
        # save address of required memory segment
        '@R13',
        'M = D'
    ]

    after = [
        # pop data to requred memory segment
        '@R13',
        'A = M',
        'M = D'
    ]

    barbar = before.extend(main_part)
    barbar = before.extend(after)    

    pass


# PURPOSE:  Generates hack assembly code for a generic pop command 
# RETURNS:  String

# TODO: rewrite

def translate_pop(arg1: str, arg2: str, filename: str):

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

    elif arg1 == 'pointer':

        addr = None

        if arg2 == '0':
            addr = 'THIS'
        else:
            addr = 'THAT'

        ls = [
            # move SP backwards
            '@SP',
            'M = M - 1',
            # go to data
            'A = M',
            # take data
            'D = M',
            # pop data to requred memory segment
            f'@{addr}',
            'M = D'
        ]
        
    elif arg1 == 'static':

        ls = [
            # move SP backwards
            '@SP',
            'M = M - 1',
            # go to data
            'A = M',
            # take data
            'D = M',
            # pop data to requred memory segment
            f'@{filename}.{arg2}',
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