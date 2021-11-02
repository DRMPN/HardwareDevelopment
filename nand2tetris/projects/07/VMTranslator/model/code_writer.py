# CodeWriter module
# writes the assembly code that implements the parsed command
from typing import IO


# PURPOSE:  Generates assembly code from the parsed VM command
class codeWriter():
    # NOTE: Leaves comment for each command line that is being translated

    # PURPOSE:  Opens the input file/stream and gets ready to write into it.
    # constructor (file/stream)
    def __init__(self) -> None:
        pass


    # PURPOSE:  Informes the code writer that the translation of a new VM
    #           file is started.
    def setFileName(self, filename: str) -> None:
        pass


    # PURPOSE:  Writes to the output file the assembly code that implements
    #           the given arithmetic command.
    # writeArithmetic (command(string))
    def writeArithmetic(self, command: str) -> IO:
        pass
    

    # PURPOSE:  Writes to the output file the assembly code that implements
    #           the given command, where command is either C_PUSH or C_POP.
    # writePushPop ( command( C_PUSH or C_POP, segment(string), index(int) ) )
    def writePushPop(self, command, segment: str, index: int) -> IO:
        pass


    # PURPOSE: Closes the output file.
    # close
    def close(self) -> None:
        pass