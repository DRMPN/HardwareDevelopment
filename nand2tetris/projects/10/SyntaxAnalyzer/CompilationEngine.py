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
    

    # 1. TODO:
    # think about reducing code redundancy with:
    #       compose non terminal
    #       +- level_indent
    # NOTE:
    # use decorator
    #       function compile_something -> write <something> ... etc
    #       or regex compileSomething  -> write <something> ... etc


    # 2. TODO:
    # refactor: self.forward()
    #           self.write(self.compose_terminal())
    # into one function
    # NOTE: 
    # all compile functions should call self.forward() at the end 


    # 3. TODO:
    # maybe reforge isOp and isUnaryOp with ... == LexicalElement.SYMBOL ?


    # 4.TODO:
    # maybe eat(something) ->
    #       if something ->
    #           write -> forward
    #       else ->
    #           sys.exit("PARSE ERROR")


    # PURPOSE:  Creates a new compilation engine with the given input and output.
    #           The next routine called must be compileClass().
    # ASSUMES:  Passed paths are absolute.
    def __init__(self, input_path, output_path) -> None:
        
        self.JT = JackTokenizer(input_path)
        self.indent_level = 0  # indentation level
        
        try: self.out_file = open(output_path, 'w')
        except OSError: sys.exit(f'Unable to create {output_path}')

        # TODO: comment
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


    # PURPOSE:  Compares current token with a passed string.
    # RETURNS:  bool
    def eat(self, string) -> bool:
        return self.JT.current_token == string


    # PURPOSE:  Checks whether or not current token is keyword or identifier.
    #           Currently purpose is: int | char | boolean | className ?
    # RETURNS:  bool
    def isKeywordOrIdentifier(self) -> bool:
        token_type = self.JT.tokenType()
        return token_type == LexicalElement.KEYWORD or token_type == LexicalElement.IDENTIFIER


    # PURPOSE:  Checks whether or not current token is identifier or not.
    #           Current target is: className | subroutineName | varName
    # RETURNS:  bool
    def isIdentifier(self) -> bool:
        return self.JT.tokenType() == LexicalElement.IDENTIFIER

    # PURPOSE:  Checks whether or not current token is keyword or not.
    #           Current target is: true | false | null | this
    # RETURNS:  bool
    def isKeyword(self) -> bool:
        return self.JT.tokenType() == LexicalElement.KEYWORD


    # PURPOSE:  Checks whether or not current token is stringConstant or not.
    # RETURNS:  bool
    def isStringConstant(self) -> bool:
        return self.JT.tokenType() == LexicalElement.STRING_CONST

    
    # PURPOSE:  Checks whether or not current token is integerConstant or not.
    # RETURNS:  bool
    def isIntegerConstant(self) -> bool:
        return self.JT.tokenType() == LexicalElement.INT_CONST

    
    # PURPOSE:  Checks whether or not current token is op or not.
    # RETURNS:  bool
    def isOp(self) -> bool:
        op = ['+', '-', '*', '/', '&', '|', '<', '>', '=']
        return self.JT.current_token in op

    
    # PURPOSE:  Checks whether or not current token is unaryOp or not.
    # RETURNS:  bool
    def isUnaryOp(self) -> bool:
        unaryOp = ['-', '~']
        return self.JT.current_token in unaryOp
    

    # PURPOSE:  Compiles a complete class.
    # ASSUMES:  Already has a token to start with.
    # class -> className -> { -> classVarDec* -> subroutineDec* -> }
    # TODO: change to isKeyword?
    def compileClass(self) -> None:
        self.write(self.compose_non_terminal('class'))
        self.indent_level += 1

        # class
        if self.eat('class'):
            self.write(self.compose_terminal())
            # className
            self.forward()
            if self.isIdentifier():
                self.write(self.compose_terminal())
                # {
                self.forward()
                if self.eat('{'):
                    self.write(self.compose_terminal())
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
        self.write(self.compose_non_terminal('/class'))


    # PURPOSE:  Compiles a static declaration or a field declaration.
    # static | field -> type -> varName -> (, -> varName )* -> ;
    def compileClassVarDec(self) -> None:
        self.write(self.compose_non_terminal('classVarDec'))
        self.indent_level += 1
        
        # static | field
        # NOTE: previously checked
        self.write(self.compose_terminal())
        # type
        self.forward()
        if self.isKeywordOrIdentifier():
            self.write(self.compose_terminal())
            # varName
            self.forward()
            if self.isIdentifier():
                self.write(self.compose_terminal())
                # (, -> varName )*
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
    def compileSubroutine(self) -> None:
        self.write(self.compose_non_terminal('subroutineDec'))
        self.indent_level += 1
        
        # constructor | function | method
        # NOTE: previously checked
        self.write(self.compose_terminal())
        # void | type
        self.forward()
        if self.isKeywordOrIdentifier(): 
            self.write(self.compose_terminal())
            # subroutineName
            self.forward()
            if self.isIdentifier():
                self.write(self.compose_terminal())
                # (
                self.forward()
                if self.eat('('):
                    self.write(self.compose_terminal())  
                    # parameterList
                    self.forward()
                    self.compileParameterList()
                    # )
                    if self.eat(')'):
                        self.write(self.compose_terminal())
                        # subroutineBody
                        self.forward()
                        self.compileSubroutineBody()

        # end
        self.indent_level -= 1
        self.write(self.compose_non_terminal('/subroutineDec'))


    # PURPOSE:  Compiles a possibly empty parameter list, not including the enclosing ().
    # type -> varName -> (, -> varName)*
    def compileParameterList(self) -> None:
        self.write(self.compose_non_terminal('parameterList'))
        self.indent_level += 1

        # type
        if self.isKeywordOrIdentifier():
            self.write(self.compose_terminal())
            # varName
            self.forward()
            self.write(self.compose_terminal())
            # (, -> varName)*
            self.forward()
            while not self.eat(')'):
                self.write(self.compose_terminal())
                self.forward()

        # end
        self.indent_level -= 1
        self.write(self.compose_non_terminal('/parameterList'))


    # PURPOSE:  Compiles a body of a subroutine.
    # { -> varDec* -> statements -> }
    def compileSubroutineBody(self) -> None:
        self.write(self.compose_non_terminal('subroutineBody'))
        self.indent_level += 1

        # {
        if self.eat('{'):
            self.write(self.compose_terminal())
            # varDec*
            self.forward()
            while self.eat('var'):
                self.compileVarDec()
                self.forward()
            # statements
            self.compileStatements()
            # }
            self.write(self.compose_terminal())

        # end
        self.indent_level -= 1
        self.write(self.compose_non_terminal('/subroutineBody'))


    # PURPOSE:  Compiles a var declaration.
    # var -> type -> varName -> (, -> varName)* -> ;
    def compileVarDec(self) -> None:
        self.write(self.compose_non_terminal('varDec'))
        self.indent_level += 1

        # var
        self.write(self.compose_terminal())
        # type
        self.forward()
        if self.isKeywordOrIdentifier():
            self.write(self.compose_terminal())
            # varName
            self.forward()
            if self.isIdentifier():
                self.write(self.compose_terminal())
                # (, -> varName)*
                self.forward()
                self.write(self.compose_terminal())
                while not(self.eat(';')):
                    self.forward()
                    self.write(self.compose_terminal())

        # end
        self.indent_level -= 1
        self.write(self.compose_non_terminal('/varDec'))
    
    
    # PURPOSE:  Compiles a sequence of statements, not including theenclosing {}.
    # statement*
    # NOTE: reforge
    def compileStatements(self) -> None:
        self.write(self.compose_non_terminal('statements'))
        self.indent_level += 1

        while True:
            current_token = self.JT.current_token
            if current_token == 'do': 
                self.compileDo()
                self.forward()
            elif current_token == 'if': 
                self.compileIf()
            elif current_token == 'let': 
                self.compileLet()
                self.forward()
            elif current_token == 'return':
                self.compileReturn()
                self.forward()
            elif current_token == 'while': 
                self.compileWhile()
                self.forward()
            else:
                #print("BREAK ON EXHAUST")
                break

        # end
        self.indent_level -= 1
        self.write(self.compose_non_terminal('/statements'))
    

    # PURPOSE:  Compiles a do statement.
    # do -> subroutineCall -> ;
    def compileDo(self) -> None: 
        self.write(self.compose_non_terminal('doStatement'))
        self.indent_level += 1

        # do
        # NOTE: previously checked
        self.write(self.compose_terminal())
        # subroutineCall
        self.forward()
        # TODO: check?
        self.compileSubroutineCall()
        # ;
        self.forward()
        if self.eat(';'):
            self.write(self.compose_terminal())

        # end
        self.indent_level -= 1
        self.write(self.compose_non_terminal('/doStatement'))


    # PURPOSE: Compiles a subroutine call.
    # subroutineName -> ( -> expressionList -> )
    # or
    # className | varName -> . -> subroutineName -> ( -> expressionList-> )
    def compileSubroutineCall(self) -> None:
        # subroutineName | className | varName
        if self.isIdentifier():
            self.write(self.compose_terminal())
            # .
            self.forward()
            if self.eat('.'):
                self.write(self.compose_terminal())
                self.forward()
                # subroutineName
                if self.isIdentifier():
                    self.write(self.compose_terminal())
                    self.forward()
            # (
            if self.eat('('):
                self.write(self.compose_terminal())
                # expressionList
                self.forward()
                self.compileExpressionList()
                # )
                # NOTE: forward was in expressionList
                if self.eat(')'):
                    self.write(self.compose_terminal())


    # PURPOSE:  Compiles an if statement.
    # if -> ( -> expression -> ) -> { -> statements -> } -> ( else -> { -> statements -> } )?
    # FIXME: remove code redundancy
    def compileIf(self) -> None: 
        self.write(self.compose_non_terminal('ifStatement'))
        self.indent_level += 1

        # if
        # NOTE: previously checked
        self.write(self.compose_terminal())
        # (
        self.forward()
        if self.eat('('):
            self.write(self.compose_terminal())
            # expression
            self.forward()
            self.compileExpression()
            # )
            # NOTE: forward was in compileExpression
            if self.eat(')'):
                self.write(self.compose_terminal())
                # {
                self.forward()
                if self.eat('{'):
                    self.write(self.compose_terminal())
                    # statements
                    self.forward()
                    self.compileStatements()
                    # }
                    if self.eat('}'):
                        self.write(self.compose_terminal())
                    # else
                    self.forward()
                    if self.eat('else'):
                        self.write(self.compose_terminal())
                        # {
                        self.forward()
                        if self.eat('{'):
                            self.write(self.compose_terminal())
                            # statements
                            self.forward()
                            self.compileStatements()
                            # }
                            if self.eat('}'):
                                self.write(self.compose_terminal())
                                self.forward()
        # end
        self.indent_level -= 1
        self.write(self.compose_non_terminal('/ifStatement'))


    # PURPOSE:  Compiles a let statement.
    # let -> varName -> ([ -> expression -> ])? -> = -> expression -> ;
    def compileLet(self) -> None: 
        self.write(self.compose_non_terminal('letStatement'))
        self.indent_level += 1

        # let
        # NOTE: previously checked
        self.write(self.compose_terminal())
        # varName
        self.forward()
        if self.isIdentifier(): # NOTE: changed from isKeywordOrIdentifier
            self.write(self.compose_terminal())
            # ([ -> expression -> ])?
            self.forward()
            if self.eat('['):
                self.write(self.compose_terminal())
                # expression
                self.forward()
                self.compileExpression()
                # ]
                # NOTE: forward was in compileExpression
                if self.eat(']'):
                    self.write(self.compose_terminal())
                    self.forward()
            # =
            if self.eat('='):
                self.write(self.compose_terminal())
                # expression
                self.forward()
                self.compileExpression()
                # ;
                if self.eat(';'):
                    self.write(self.compose_terminal())

        # end
        self.indent_level -= 1
        self.write(self.compose_non_terminal('/letStatement'))


    # PURPOSE:  Compiles a while statement.
    # while -> ( -> expression -> ) -> { -> statements -> }
    def compileWhile(self) -> None: 
        self.write(self.compose_non_terminal('whileStatement'))
        self.indent_level += 1

        # while
        # NOTE: previously checked
        self.write(self.compose_terminal())
        # (
        self.forward()
        if self.eat('('):
            self.write(self.compose_terminal())
            # expression
            self.forward()
            self.compileExpression()
            # )
            # NOTE: forward was in compileExpression
            if self.eat(')'):
                self.write(self.compose_terminal())
                # {
                self.forward()
                if self.eat('{'):
                    self.write(self.compose_terminal())
                    # statements
                    self.forward()
                    self.compileStatements()
                    # }
                    if self.eat('}'):
                        self.write(self.compose_terminal())

        # end
        self.indent_level -= 1
        self.write(self.compose_non_terminal('/whileStatement'))


    # PURPOSE:  Compiles a return statement.
    # return -> expression? -> ;
    def compileReturn(self) -> None: 
        self.write(self.compose_non_terminal('returnStatement'))
        self.indent_level += 1

        # return
        # NOTE: previously checked
        self.write(self.compose_terminal())
        # expresssion?
        self.forward()
        if not self.eat(';'):
            self.compileExpression()
        # ;
        # NOTE: forward was in compileExpression
        if self.eat(';'):
            self.write(self.compose_terminal())

        # end
        self.indent_level -= 1
        self.write(self.compose_non_terminal('/returnStatement'))


    # PURPOSE:  Compiles an expression.
    # term -> (op -> term)*
    def compileExpression(self) -> None:
        self.write(self.compose_non_terminal('expression'))
        self.indent_level += 1
        
        # term
        self.compileTerm()
        # op*
        while self.isOp():
            self.write(self.compose_terminal())
            # term
            self.forward()
            self.compileTerm()

        # end
        self.indent_level -= 1
        self.write(self.compose_non_terminal('/expression'))
    

    # PURPOSE: Compiles a term.
    # + integerConstant | + stringConstant | + keywordConstant | 
    # + varName | + varName [ expression ] | + varName . subroutineCall | 
    # + ( expression ) | + unaryOp term
    # TODO: remove code redundancy
    def compileTerm(self) -> None:
        self.write(self.compose_non_terminal('term'))
        self.indent_level += 1

        # varName
        if self.isIdentifier():
            self.write(self.compose_terminal())
            self.forward()
            # . subroutineCall
            if self.eat('.'):
                self.write(self.compose_terminal())
                # subroutineCall
                self.forward()
                self.compileSubroutineCall()
                self.forward()
            # [ expression ]
            if self.eat('['):
                self.write(self.compose_terminal())
                # expression
                self.forward()
                self.compileExpression()
                # ]
                # NOTE: forward was in compileExpression
                if self.eat(']'):
                    self.write(self.compose_terminal())
                    self.forward()

        # ( expression )
        elif self.eat('('):
            self.write(self.compose_terminal())
            # expression
            self.forward()
            self.compileExpression()
            # )
            # NOTE: forward was in compileExpression
            if self.eat(')'):
                self.write(self.compose_terminal())
                self.forward()
        
        # unaryOp term
        elif self.isUnaryOp():
            self.write(self.compose_terminal())
            # term
            self.forward()
            self.compileTerm()
            # NOTE: forward?

        # stringConstant
        elif self.isStringConstant():
            self.write(self.compose_terminal())
            self.forward()

        # integerConstant
        elif self.isIntegerConstant():
            self.write(self.compose_terminal())
            self.forward()

        # keywordConstant
        elif self.isKeyword():
            self.write(self.compose_terminal())
            self.forward()

        self.indent_level -= 1
        self.write(self.compose_non_terminal('/term'))


    # PURPOSE:  Compiles a (possibly empty) comma-separated list of expressions.
    # ( expression -> (, -> expression)* )?
    def compileExpressionList(self) -> None:
        self.write(self.compose_non_terminal('expressionList'))
        self.indent_level += 1

        while not self.eat(')'):
            # ,
            if self.eat(','):
                self.write(self.compose_terminal())
                self.forward()
            # expressison
            self.compileExpression()
            # NOTE: forward was in compileExpression

        # end
        self.indent_level -= 1
        self.write(self.compose_non_terminal('/expressionList'))   