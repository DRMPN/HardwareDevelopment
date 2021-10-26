# PURPOSE: Keeps a correspondance between symbolic labels and numeric addresses
class SymbolTable():
    
    # PURPOSE: Creates a new empty symbol table
    def __init__(self) -> None:

        self.table = {}

    
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