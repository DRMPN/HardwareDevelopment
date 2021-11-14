from enum import Enum


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
    C_LABEL = 'label'
    C_GOTO = 'goto'
    C_IF = 'if-goto'
    C_FUNCTION = 'function'
    C_RETURN = 'return'
    C_CALL = 'call'