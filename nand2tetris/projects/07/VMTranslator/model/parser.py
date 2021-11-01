# parser module
# parses each VM command into its lexical elements


# Handles the parsing of a single .vm file
# Reads a VM command, parses the command line into its lexical
# components, and provides convenient access to these components
# Ignores all white space and comments


# PURPOSE:  Opens the input file/stream and gets ready to parse it
# Constructor

# PURPOSE:  Are there more commands in the input?
# RETURNS:  boolean
# hasMoreCommands

# PURPOSE:  Reads the next command from the input and makes it current command.
#           Should be called only if hasMoreCommands is true. Initially there
#           is no current command.
# advance (file/stream)


# PURPOSE:  Returns a constant representing the type of the current command.
#           C_ARITHMETIC is returned for all the arithmetic/logical commands.
# RETURNS:  class_name (C_ARITHMETIC, C_PUSH, C_POP, C_LABEL, C_GOTO, C_IF, 
#           C_FUNCTION, C_RETURN, C_CALL).
# commandType


# PURPOSE:  Returns the first argument of the current command. In the case of
#           C_ARITHMETIC, the command itself (add, sub, etc.) is returned.
#           Should not be called if the current command is C_RETURN.
# RETURNS:  String
# arg1


# PURPOSE:  Returns the second argument of the current command. Should be called
#           only if the current command is C_PUSH, C_POP, C_FUNCTION, or C_CALL.
# RETURNS: String
# arg2