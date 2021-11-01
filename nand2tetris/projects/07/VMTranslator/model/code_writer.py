# CodeWriter module
# writes the assembly code that implements the parsed command


# Generates assembly code from the parsed VM command

# NOTE: Leaves comment for each command line that is being translated

# PURPOSE:  Opens the input file/stream and gets ready to parse it.
# constructor (file/stream)


# PURPOSE:  Writes to the output file the assembly code that implements
#           the given arithmetic command.
# writeArithmetic (command(string))


# PURPOSE:  Writes to the output file the assembly code that implements
#           the given command, where command is either C_PUSH or C_POP.
# writePushPop ( command( C_PUSH or C_POP, segment(string), index(int) ) )


# PURPOSE: Closes the output file.
# close