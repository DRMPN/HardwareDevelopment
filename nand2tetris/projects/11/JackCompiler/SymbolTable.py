"""Symbol Table module.

Provides a symbol table abstraction. The symbol table associates the 
identifier properties needed for compilation: type, kind, and running index. 
The symbol table for Jack programs has two nested scopes(class/subroutine).

+------+------+----------+
| name | type | kind | # |
|------+------+------+---|
|  ..  |  ..  |  ..  | . |
+------+------+------+---+
"""


class SymbolTable():

    # NOTE: Two separate hash tables: one for the class scope and
    #       another one for the sub-routine scope.

    # TODO: think about enum?
    # TODO: change symbol table arg to argument? var to local?
    
    # PURPOSE: Creates a new empty symbol table.
    def __init__(self) -> None:
        self.runningIndex = 0
        self.previousKind = None
        # list of dictionaries
        self.classTable = []
        self.subroutineTable = []

    
    # PURPOSE: Starts a new subroutine scope 
    #          (i.e., resets the subroutine's symbol table).
    def start_subroutine(self) -> None:
        self.runningIndex = 0
        self.previousKind = None
        self.subroutineTable = []


    # PURPOSE: Defines a new identifier of a given name, type, and kind 
    #          and assigns it a running index. STATIC and FIELD identifiers 
    #          have a class scope, while ARG and VAR identifiers have a 
    #          subroutine scope.
    def define(self, name: str, type_: str, kind: str) -> None:
        if kind == self.previousKind:
            self.runningIndex += 1
        else:
            self.runningIndex = 0

        element = {'name': name, 
                   'type': type_, 
                   'kind': kind, 
                   '#': self.runningIndex
        }

        if kind =='field' or kind == 'static':
            self.classTable.append(element.copy())
        elif kind == 'arg' or kind == 'var':
            self.subroutineTable.append(element.copy())

        self.previousKind = kind
        

    # PURPOSE: Returns the number of variables of the given kind 
    #          already defined in the current scope.
    # RETURNS: int
    def var_count(self, kind: str) -> int:
        count = 0

        if kind == 'field' or kind == 'static':
            table = self.classTable
        elif kind == 'arg' or kind == 'var':
            table = self.subroutineTable

        for row in table:
            if row['kind'] == kind:
                count += 1

        return count

    
    # PURPOSE: Returns the kind of the named identifier in the current scope.
    #          If the identifier is unknown in the current scope, returns NONE.
    # RETURNS: str
    def kind_of(self, name: str) -> str:
        kind = None

        for row in self.subroutineTable:
            if row['name'] == name:
                kind = row['kind']

        if kind is None:
            for row in self.classTable:
                if row['name'] == name:
                    kind = row['kind']

        return kind


    # PURPOSE: Returns the type of the named identifier in the current scope.
    # RETURNS: str
    def type_of(self, name: str) -> str:
        type = None

        for row in self.subroutineTable:
            if row['name'] == name:
                type = row['type']

        if type is None:
            for row in self.classTable:
                if row['name'] == name:
                    type = row['type']

        return type

    
    # PURPOSE: Returns the index assigned to the named identifier.
    # RETURNS: int
    def index_of(self, name: str) -> int:
        index = None

        for row in self.subroutineTable:
            if row['name'] == name:
                index = row['#']

        if index is None:
            for row in self.classTable:
                if row['name'] == name:
                    index = row['#']

        return index