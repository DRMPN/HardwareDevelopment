from enum import Enum, auto


# PURPOSE: Represents possible machine language commands
class CommandType(Enum):
    A_COMMAND = auto()
    C_COMMAND = auto()
    L_COMMAND = auto()