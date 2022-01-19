import sys
from JackTokenizer import *

# Effects the actual compilation output. Gets its input from a JackTokenizer 
#   and emits its parsed structure into an output file/stream. The output 
#   is generated by a series of compilexxx() routines, one for every syntactic
#   element xxx of the Jack grammar. The contract between these routines is that each
#   compilexxx() routine should read the syntactic construct xxx from the input,
#   advance() the tokenizer exactly beyond xxx, and output the parsing of xxx. Thus,
#   compilexxx() may only be called if indeed xxx is the next syntactic element of the input.

class CompilationEngine():
    

    # TODO:
    #   1. handle everything except expressions
    #   2. test it on the expressionless Square Dance
    #   3. extend the parser to handle expressions as well
    #   4. test it on the square dance and array test


    # PURPOSE:  Creates a new compilation engine with the given input and output.
    #           The next routine called must be compileClass().
    # ASSUMES:  Passed paths are absolute.
    def __init__(self, input_path, output_path) -> None:
        
        self.JT = JackTokenizer(input_path)
        self.indent_level = 0  # indentation level
        
        try: self.out_file = open(output_path, 'w')
        except OSError: sys.exit(f'Unable to create {output_path}')

        self.forward()

    
    # PURPOSE:  Writes a line into an output file.
    # CHANGES:  file
    def write(self, line) -> None:
        self.out_file.write(line)
        

    # PURPOSE:  Closes output file and frees the memory.
    # CHANGES:  file
    def dispose(self) -> None:
        self.out_file.close()


    # PURPOSE:  Advances tokenizer by one token.
    # CHANGES:  JackTokenizer
    def forward(self) -> None:
        if self.JT.hasMoreTokens(): self.JT.advance()


    # PURPOSE:  Returns an XML tag for a passed non-terminal element.
    # RETURNS:  str
    def compose_non_terminal(self, word) -> str:
        indent = self.indent_level * '  ' # 2 spaces
        return f'{indent}<{word}>\n'


    # PURPOSE:  Returns an XML line for a current terminal element.
    # RETURNS:  str
    def compose_terminal(self) -> str:
        indent = self.indent_level * '  ' # 2 spaces
        token_type = self.JT.tokenType()
        token = self.get_current_token(token_type)
        return f'{indent}<{token_type.value}> {token} </{token_type.value}>\n'

    
    # PURPOSE:  Returns current token represented as a string.
    # RETURNS:  str
    def get_current_token(self, token_type: LexicalElement) -> str:
        if token_type == LexicalElement.KEYWORD: return self.JT.keyWord()
        elif token_type == LexicalElement.SYMBOL: return self.JT.symbol()
        elif token_type == LexicalElement.IDENTIFIER: return self.JT.identifier()
        elif token_type == LexicalElement.INT_CONST: return self.JT.intVal()
        elif token_type == LexicalElement.STRING_CONST: return self.JT.stringVal()


    #   while ( expression ) { statements }
    #      eat while -> code to handle 'while'
    #      eat (
    #      compileexpression()
    #      eat )
    #      eat {
    #      compile statements
    #      eat }


    # PURPOSE:  Compiles a complete class.
    # ASSUMES:  Already has a token to start with.
    # class -> className -> { -> classVarDec* -> subroutineDec* -> }
    def compileClass(self) -> None:
        # class
        if self.eat('class'):
            self.write(self.compose_non_terminal('class'))
            self.indent_level += 1
            self.write(self.compose_terminal())
            # className
            self.forward()
            self.write(self.compose_terminal())
            # {
            self.forward()
            if self.eat('{'):
                self.write(self.compose_terminal())

                # TODO: test this block of code properly, but should work as expected
                # classVarDec*
                self.forward()
                while self.eat('static') or self.eat('field'):
                    self.compileClassVarDec()
                    self.forward()
                # subroutineDec*
                while self.eat('constructor') or self.eat('function') or self.eat('method'):
                    self.compileSubroutine()
                    self.forward()

                # }
                if self.eat('}'):
                    self.write(self.compose_terminal())
                    # end
                    self.indent_level -= 1
                    self.write(self.compose_non_terminal('/ class'))


    # eat(string) {
    # if currentToken != string
    #   error
    # else
    #   advance
    # }

    # PURPOSE:  TODO
    # RETURNS:  bool
    def eat(self, string) -> bool:
        return self.JT.current_token == string

    # TODO: idea for a new function
    # compileType
    # is int | char | boolean | className ?

    # TODO: idea for a new function
    # compileClassName
    # is identifier ?

    # TODO: idea for a new function
    # compileSubroutineName
    # is identifier ?

    # TODO: idea for a new function
    # compileVarName
    # is identifier ?


    # PURPOSE:  Compiles a static declaration or a field declaration.
    # static | field -> type -> varName -> (, -> varName )* -> ;
    def compileClassVarDec(self):
        # static | field
        # previously done
        self.write(self.compose_non_terminal('classVarDec'))
        self.indent_level += 1
        self.write(self.compose_terminal())
        # type
        self.forward()
        self.write(self.compose_terminal())
        # varName
        self.forward()
        self.write(self.compose_terminal())

        # more?
        # TODO: test this block of code properly, but should work as expected
        self.forward()
        self.write(self.compose_terminal())
        while not(self.eat(';')):
            self.forward()
            self.write(self.compose_terminal())

        # end
        self.indent_level -= 1
        self.write(self.compose_non_terminal('/classVarDec'))
    

    # PURPOSE:  Compiles a complete method, function, or constructor.
    # constructor | function | method -> void | type -> subroutineName -> ( -> parameterList -> ) -> subroutineBody
    def compileSubroutine(self):
        # constructor | function | method
        # previously done
        self.write(self.compose_non_terminal('subroutineDec'))
        self.indent_level += 1
        self.write(self.compose_terminal())
        
        # void | type
        self.forward()
        # TODO: type check
        if self.eat('void') or True: 
            self.write(self.compose_terminal())
            # subroutineName
            self.forward()
            self.write(self.compose_terminal())
            # (
            self.forward()
            if self.eat('('):
                self.write(self.compose_terminal())
                # parameterList
                self.forward()
                # strict 0 or 1
                # compileParameterList()
                 # TODO: ...

        # end
        self.indent_level -= 1
        self.write(self.compose_non_terminal('/subroutineDec'))


    # compileParameterList
    # compileVarDec
    # compileStatements
    # ??? compileStatement
    # compileDo
    # compileLet
    # compileWhile
    # compileReturn
    # compileIf
    # CompileExpression
    # CompileTerm
    # CompileExpressionList