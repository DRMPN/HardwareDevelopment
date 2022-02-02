from enum import Enum, auto


class Kind(Enum):
    ARG = auto()    # scope: subroutine
    FIELD = auto()  # scope: class
    NONE = auto()
    STATIC = auto() # scope: class
    VAR = auto()    # scope: subroutine


# TODO: a bunch of code that requires testing and refactoring


# Provides a symbol table abstraction. The symbol table associates the identifier
# properties needed for compilation: type, kind, and running index. The symbol table for
# Jack programs has two nested scopes(class/subroutine).
class SymbolTable():

    # NOTE: Two separate hash tables: one for the class scope and another one for the sub-
    #       routine scope.
    
    # PURPOSE:  Creates a new empty symbol table.
    # +------+------+----------+
    # | name | type | kind | # |
    # |------+------+------+---|
    # |  ..  |  ..  |  ..  | . |
    # +------+------+------+---+
    def __init__(self) -> None:
        # list of dictionaries
        self.classTable = []
        self.subroutineTable = []
        self.runningIndex = 0
        self.previousKind = None

    
    # PURPOSE:  Starts a new subroutine scope (i.e., resets the subroutine's symbol table).
    def startSubroutine(self) -> None:
        self.subroutineTable = []
        self.runningIndex = 0
        self.previousKind = None


    # PURPOSE:  Defines a new identifier of a given name, type, and kind 
    #           and assigns it a running index. STATIC and FIELD identifiers 
    #           have a class scope, while ARG and VAR identifiers have a subroutine scope.
    # TODO: better solution?
    # TODO: write tests
    def Define(self, name: str, type: str, kind: Kind) -> None:
        # class
        if kind == Kind.FIELD or kind == Kind.STATIC:
            if kind == self.previousKind:
                self.runningIndex += 1
            else:
                self.runningIndex = 0
            self.classTable.extend({'name': name, 'type': type, 'kind': kind, '#': self.runningIndex})
        # subroutine
        elif kind == Kind.ARG or kind == Kind.VAR:
            if kind == self.previousKind:
                self.runningIndex += 1
            else:
                self.runningIndex = 0
            self.subroutineTable.extend({'name': name, 'type': type, 'kind': kind, '#': self.runningIndex})
        # in case Kind.NONE has been passed
        else: 
            pass
        

    # PURPOSE:  Returns the number of variables of the given kind 
    #           already defined in the current scope.
    # RETURNS:  int
    # TODO: write tests
    # NOTE: return 0 for NONE
    def VarCount(self, kind: Kind) -> int:
        num = 0
        # class
        if kind == Kind.FIELD or kind == Kind.STATIC:
            for row in self.classTable:
                if kind in row:
                    num += 1
        # subroutine
        elif kind == Kind.ARG or kind == Kind.VAR:
            for row in self.classTable:
                if kind in row:
                    num += 1
        return num

    
    # PURPOSE:  Returns the kind of the named identifier in the current scope.
    #           If the identifier is unknown in the current scope, returns NONE.
    # RETURNS:  Kind
    # TODO: write tests
    def KindOf(self, name: str) -> Kind:
        kind = None
        for row in self.subroutineTable:
            if name in row:
                kind = row.kind
        if kind is None:
            for row in self.classTable:
                if name in row:
                    kind = row.kind
        return kind


    # PURPOSE:  Returns the type of the named identifier in the current scope.
    # RETURNS:  string
    # TODO: write tests
    def TypeOf(self, name: str) -> str:
        type = None
        for row in self.subroutineTable:
            if name in row:
                type = row.type
        if type is None:
            for row in self.classTable:
                if name in row:
                    type = row.type
        return type

    
    # PURPOSE:  Returns the index assigned to the named identifier.
    # RETURNS:  int
    # TODO: write tests
    def IndexOf(self, name: str) -> int:
        index = None
        for row in self.subroutineTable:
            if name in row:
                index = row.index
        if index is None:
            for row in self.classTable:
                if name in row:
                    index = row.index
        return index