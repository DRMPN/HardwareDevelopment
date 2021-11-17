import os
from sys import exit
from time import time
from typing import IO, List
from functools import wraps


# PURPOSE:  Generates assembly code from the parsed VM command
# NOTE: Leaves comment for each command line that is being translated
class CodeWriter():

    # PURPOSE:  Opens the input file/stream and gets ready to write into it.
    def __init__(self, path_to_file: str) -> IO:
        
        self.file = None
        # Resolves a filename for an output file
        self.filename = os.path.basename(path_to_file).split('.')[0]
        
        # Replaces path/to/file.vm to path/to/file.asm
        path_to_file = path_to_file.replace('.vm', '.asm')
        
        try:
            self.file = open(f'{path_to_file}', 'w')
        except OSError:
            exit(f'ERROR: File {path_to_file} cannot be opened/created.')
            
        self.setFileName(self.filename)


    # PURPOSE:  Informes the code writer that the translation of a new VM
    #           file is started.
    def setFileName(self, filename: str) -> None:
        print(f'Translation has been started.\nOutput file: {filename}.asm')


    # PURPOSE:  Writes to the output file the assembly code that implements
    #           the given arithmetic command.
    def writeArithmetic(self, command: str) -> IO:
        # leave comment in file
        self.file.write(f'// {command}\n')

        # translate command
        com = translate_arithmetic(command)

        # write translated command in file
        self.file.write(f'{com}\n')
    

    # PURPOSE:  Writes to the output file the assembly code that implements
    #           the given command, where command is either C_PUSH or C_POP.
    def writePushPop(self, command: str, segment: str, index: int) -> IO:
        # leave comment in file
        self.file.write(f'// {command} {segment} {index} \n')

        # translate command
        if command =='push':
            com = translate_push(segment, index, self.filename)

        elif command == 'pop':
            com = translate_pop(segment, index, self.filename)

        # write translated command in file
        self.file.write(f'{com}\n')


    # PURPOSE: Closes the output file.
    def close(self) -> None:
        self.file.close()
        print('Done.')


    # PURPOSE:  Writes assembly code that effects the VM initialization.
    #           This code must be placed at the beginning of the output file.
    # TODO: later 
    # writeInit
    # SP = 256
    # call sys.init 


    # PURPOSE:  Writes assembly code that effects the label command
    def writeLabel(self, label: str) -> IO:
        # leave comment in file
        self.file.write(f'// label {label}\n')
        # translate label
        l = translate_label(label)
        # write to the file
        self.file.write(f'{l}\n')


    # PURPOSE:  Writes assembly code that effects the goto command.
    def writeGoto(self, label: str) -> IO:
        self.file.write(f'// goto {label}\n')
        goto = translate_goto(label)
        self.file.write(f'{goto}\n')


    # PURPOSE:  Writes assembly code that effects the if-goto command.
    def writeIf(self, label: str) -> IO:
        self.file.write(f'// goto {label}\n')
        if_goto = translate_if(label)
        self.file.write(f'{if_goto}\n')


    # PURPOSE:  Writes assembly code that effects the call command.
    # writeCall(functionName: str, numArgs: int)


    # PURPOSE:  Writes assembly code that effects the return command.
    # writeReturn()


    # PURPOSE:  Writes assembly code that effects the funciton command.
    # writeFunction(funcitonName: str, numLocals: int)


# PURPOSE:  Translates nine arithmetic commands
# RETURNS:  String

# TODO: maybe refactor it? huh O_o? but now it's more readable

def translate_arithmetic(command: str) -> str:

    if command in ['neg','not']:
        return translate_unary(command)

    if command in ['add','sub','and','or']:
        return translate_binary(command)

    if command in ['eq', 'gt','lt']:
        return translate_jump(command)   


# PURPOSE:  Joins a list of strings with a newline symbol
def add_newline(func) -> str:

    @wraps(func)
    def wrapper_add_newline(*args, **kwargs):
        return '\n'.join(func(*args, **kwargs))

    return wrapper_add_newline


# PURPOSE:  Generates Hack assembly code for 'and' 'sub' 'and' 'or' commands
# RETURNS:  List of strings
@add_newline
def translate_binary(command: str) -> List[str]:
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
    }.get(command)

    first_part.append(second_part)

    return first_part


# PURPOSE:  Generates Hack assembly code for 'neg' 'not' commands
# RETURNS:  List of strings
@add_newline
def translate_unary(command: str) -> List[str]:
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
    }.get(command)

    first_part.append(second_part)

    return first_part


# PURPOSE:  Generates hack assembly code for eq|gt|lt command
# RETURNS:  List of strings
@add_newline
def translate_jump(jump: str) -> List[str]:
    jump = jump.upper()
    # generate random variable based on hash of time
    name = jump + str(hash(time()))
    los = [ 
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

    return los


# PURPOSE:  Generates hack assembly code for a generic push command 
# RETURNS:  List of strings
@add_newline
def translate_push(arg1: str, arg2: str, filename: str) -> List[str]:

    bar = {
        'local':'LCL',
        'argument':'ARG',
        'this':'THIS',
        'that':'THAT'
    }.get(arg1)

    if bar is not None:
        # code that comes before common part

        first_part = [
        # take value
        f'@{arg2}',
        'D = A',
        # go to data
        f'@{bar}',
        'A = M + D',
        # take data
        'D = M'
        ]

    else:

        pointer = {'0':'THIS', '1':'THAT'}.get(arg2)

        # code that comes before common part
        first_part = {
            'temp': [
                # go to data
                f'@{5 + int(arg2)}', 
                # take data
                'D = M'
                ],
            'static': [f'@{filename}.{arg2}', 'D = M'],
            'pointer': [f'@{pointer}','D = M'],
            'constant': [f'@{arg2}','D = A']
        }.get(arg1)

    # common part of the code
    common_part = [
        # go to SP and push data
        '@SP',
        'A = M',
        'M = D',
        # increase SP
        '@SP',
        'M = M + 1'
    ]
    
    first_part.extend(common_part)

    return first_part


# PURPOSE:  Generates hack assembly code for a generic pop command 
# RETURNS:  List of strings
@add_newline
def translate_pop(arg1: str, arg2: str, filename: str) -> List[str]:
    # common part of the code
    common_part = [
        # move SP backwards
        '@SP',
        'M = M - 1',
        # go to data
        'A = M',
        # take data
        'D = M'
    ]

    foo = { 'local':'LCL',
            'argument':'ARG',
            'this':'THIS',
            'that':'THAT'
        }.get(arg1)

    if foo is not None:
        
        # code that comes before common part
        common_part[:0] = [   
            # get second argument
            f'@{arg2}',
            'D = A',
            # go to labeled memory segment
            f'@{foo}',
            # compute address of required memory segment
            'D = D + M',
            # save address of required memory segment
            '@R13',
            'M = D'
        ]

        # code that comes after common part
        common_part.extend(
            [   # pop data to requred memory segment
                '@R13',
                'A = M',
                'M = D' ])

    else:

        pointer = {'0':'THIS', '1':'THAT'}.get(arg2)

        # code that comes after common part
        bar = {
            'temp': [f'@{5 + int(arg2)}','M = D'],
            'static': [f'@{filename}.{arg2}', 'M = D'],
            'pointer': [f'@{pointer}', 'M = D']
        }.get(arg1)

        common_part.extend(bar)

    return common_part


# PURPOSE:  Generates hack assembly code for a label command
# RETURNS:  List of strings
@add_newline
def translate_label(label: str) -> List[str]:
    foo = [
        f'({label})'
    ]
    return foo


# PURPOSE:  Generates hack assembly code for a unconditional goto command
# RETURNS:  List of strings
@add_newline
def translate_goto(label: str) -> List[str]:
    foo = [
        f'@{label}',
        '0; JMP'
    ]
    return foo


# PURPOSE:  Generates hack assembly code for a conditional goto command
# RETURNS:  List of strings
@add_newline
def translate_if(label: str) -> List[str]:
    foo = [
        # move SP backward
        '@SP',
        'M = M - 1',
        # go to data
        'A = M',
        # take data
        'D = M',
        # if D != 0, jump
        f'@{label}',
        'D; JNE'
    ]
    return foo