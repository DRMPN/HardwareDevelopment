# CodeWriter module
# writes the assembly code that implements the parsed command
import sys
from typing import IO


# PURPOSE:  Generates assembly code from the parsed VM command
class CodeWriter():
    # NOTE: Leaves comment for each command line that is being translated

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
        self.file.write(f'{command}\n')
    

    # PURPOSE:  Writes to the output file the assembly code that implements
    #           the given command, where command is either C_PUSH or C_POP.
    # writePushPop ( command( C_PUSH or C_POP, segment(string), index(int) ) )

    # TODO: check out command argument

    def writePushPop(self, command, segment: str, index: int) -> IO:
        self.file.write(f'// {command} {segment} {index} \n')
        self.file.write(f'{command}\n')


    # PURPOSE: Closes the output file.
    # close
    def close(self) -> None:
        self.file.close()
        print('Done.')