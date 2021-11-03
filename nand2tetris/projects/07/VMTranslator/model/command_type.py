from enum import Enum, auto


# Arithmetic and Logical commands:
a_and_l_commands = ['add', 
                    'sub',
                    'neg',
                    'eq',
                    'gt',
                    'lt',
                    'and',
                    'or',
                    'not']


# PURPOSE:  Implements all possible commands for a VMTranslator
class CommandType(Enum):
    C_ARITHMETIC = a_and_l_commands
    C_PUSH = 'push'
    C_POP = 'pop'
    C_LABEL = auto()
    C_GOTO = auto()
    C_IF = auto()
    C_FUNCTION = auto()
    C_RETURN = auto()
    C_CALL = auto()