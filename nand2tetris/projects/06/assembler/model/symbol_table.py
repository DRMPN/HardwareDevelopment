# PURPOSE: Keeps a correspondance between symbolic labels and numeric addresses
class SymbolTable():
    
    # Symbol table with predefined symbols
    predefined = {
        'SP' : 0,
        'LCL' : 1,
        'ARG' : 2,
        'THIS' : 3,
        'THAT' : 4,
        'R0' : 0,
        'R1' : 1,
        'R2' : 2,
        'R3' : 3,
        'R4' : 4,
        'R5' : 5,
        'R6' : 6,
        'R7' : 7,
        'R8' : 8,
        'R9' : 9,
        'R10' : 10,
        'R11' : 11,
        'R12' : 12,
        'R13' : 13,
        'R14' : 14,
        'R15' : 15,
        'SCREEN' : 16384,
        'KBD' : 24576 
    }

    # PURPOSE: Creates a symbol table with predefined symbols
    def __init__(self) -> None:

        self.table = self.predefined.copy()

    
    # PURPOSE: Adds the pair(symbol,address) to the table
    # CHANGES: self
    def addEntry(self, symbol: str, address: int) -> None:
        self.table[symbol] = address


    # PURPOSE: Does the symbol table contains the given symbol?
    # RETURNS: Boolean
    def contains(self, symbol: str) -> bool:
        return symbol in self.table


    # PURPOSE: Returns the address associated with the symbol
    # RETURNS: int
    def getAddress(self, symbol: str) -> int:
        return self.table[symbol]