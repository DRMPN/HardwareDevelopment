import sys
from functools import wraps
from JackTokenizer import *


# Effects the actual compilation output. Gets its input from a JackTokenizer 
#   and emits its parsed structure into an output file/stream. The output 
#   is generated by a series of compilexxx() routines, one for every syntactic
#   element xxx of the Jack grammar. The contract between these routines is that each
#   compilexxx() routine should read the syntactic construct xxx from the input,
#   advance() the tokenizer exactly beyond xxx, and output the parsing of xxx. Thus,
#   compilexxx() may only be called if indeed xxx is the next syntactic element of the input.


# PURPOSE:  Generates marked-up output for a non-terminal element.
# <xxx>
#        Recursive code for the body of the xxx element.
# </xxx>
def wrap_non_terminal(func) -> None:

    @wraps(func)
    def non_terminal_wrapper(*args, **kwargs):
        
        non_terminal = re.split('_', func.__name__)[1] # get non-terminal name of an element

        args[0].write(args[0].compose_non_terminal(non_terminal))
        args[0].indent_level += 1

        func(*args, **kwargs)

        args[0].indent_level -= 1
        args[0].write(args[0].compose_non_terminal(f'/{non_terminal}'))

    return non_terminal_wrapper


class CompilationEngine():
    
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

        self.forward() # prepare first token to parse

    
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


    # TODO: maybe move inside ^^
    # PURPOSE:  Returns current token represented as a string.
    # RETURNS:  str
    def get_current_token(self, token_type: LexicalElement) -> str:
        if token_type == LexicalElement.KEYWORD: return self.JT.keyWord()
        elif token_type == LexicalElement.SYMBOL: return self.JT.symbol()
        elif token_type == LexicalElement.IDENTIFIER: return self.JT.identifier()
        elif token_type == LexicalElement.INT_CONST: return self.JT.intVal()
        elif token_type == LexicalElement.STRING_CONST: return self.JT.stringVal()

    
    # PURPOSE:  Writes current token element as an XML line in the output file 
    #           and advances the tokenizer.
    # CHANGES:  file, tokenizer
    def write_terminal(self) -> None:
        self.out_file.write(self.compose_terminal())
        self.forward()


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
    @wrap_non_terminal
    def compile_class(self) -> None:
        # class
        if self.eat('class'):
            self.write_terminal()
            # className
            if self.isIdentifier():
                self.write_terminal()
                # {
                if self.eat('{'):
                    self.write_terminal()
                    # classVarDec*
                    while self.eat('static') or self.eat('field'):
                        self.compile_classVarDec()
                    # subroutineDec*
                    while self.eat('constructor') or self.eat('function') or self.eat('method'):
                        self.compile_subroutineDec()
                    # }
                    if self.eat('}'):
                        self.write_terminal()


    # PURPOSE:  Compiles a static declaration or a field declaration.
    # static | field -> type -> varName -> (, -> varName )* -> ;
    @wrap_non_terminal
    def compile_classVarDec(self) -> None:
        # static | field # NOTE: previously checked
        self.write_terminal()
        # type
        if self.isKeywordOrIdentifier():
            self.write_terminal()
            # varName
            if self.isIdentifier():
                self.write_terminal()
                # (, -> varName )*
                while not(self.eat(';')):
                    self.write_terminal()
                self.write_terminal()
    

    # PURPOSE:  Compiles a complete method, function, or constructor.
    # constructor | function | method -> void | type -> subroutineName -> ( -> parameterList -> ) -> subroutineBody
    @wrap_non_terminal
    def compile_subroutineDec(self) -> None:
        # constructor | function | method # NOTE: previously checked
        self.write_terminal()
        # void | type
        if self.isKeywordOrIdentifier(): 
            self.write_terminal()
            # subroutineName
            if self.isIdentifier():
                self.write_terminal()
                # (
                if self.eat('('):
                    self.write_terminal()
                    # parameterList
                    self.compile_parameterList()
                    # )
                    if self.eat(')'):
                        self.write_terminal()
                        # subroutineBody
                        self.compile_subroutineBody()


    # PURPOSE:  Compiles a possibly empty parameter list, not including the enclosing ().
    # type -> varName -> (, -> varName)*
    @wrap_non_terminal
    def compile_parameterList(self) -> None:
        # type
        if self.isKeywordOrIdentifier():
            self.write_terminal()
            # varName
            self.write_terminal()
            # (, -> varName)*
            while not self.eat(')'):
                self.write_terminal()


    # PURPOSE:  Compiles a body of a subroutine.
    # { -> varDec* -> statements -> }
    @wrap_non_terminal
    def compile_subroutineBody(self) -> None:
        # {
        if self.eat('{'):
            self.write_terminal()
            # varDec*
            while self.eat('var'):
                self.compile_varDec()
            # statements
            self.compile_statements()
            # }
            if self.eat('}'):
                self.write_terminal()


    # PURPOSE:  Compiles a var declaration.
    # var -> type -> varName -> (, -> varName)* -> ;
    @wrap_non_terminal
    def compile_varDec(self) -> None:
        # var
        if self.eat('var'):
            self.write_terminal()
            # type
            if self.isKeywordOrIdentifier():
                self.write_terminal()
                # varName
                if self.isIdentifier():
                    self.write_terminal()
                    # (, -> varName)*
                    while not(self.eat(';')):
                        self.write_terminal()
                    # ;
                    if self.eat(';'):
                        self.write_terminal()
    
    
    # PURPOSE:  Compiles a sequence of statements, not including theenclosing {}.
    # statement*
    @wrap_non_terminal
    def compile_statements(self) -> None:
        # statement*
        while True:
            if self.eat('do'): 
                self.compile_doStatement()
            elif self.eat('if'): 
                self.compile_ifStatement()
            elif self.eat('let'): 
                self.compile_letStatement()
            elif self.eat('return'):
                self.compile_returnStatement()
            elif self.eat('while'): 
                self.compile_whileStatement()
            else:
                break #print("BREAK ON EXHAUST")
    

    # PURPOSE:  Compiles a do statement.
    # do -> subroutineCall -> ;
    @wrap_non_terminal
    def compile_doStatement(self) -> None: 
        # do # NOTE: previously checked
        self.write_terminal()
        # subroutineCall
        if self.isIdentifier():
            self.compile_subroutineCall()
            # ;
            if self.eat(';'):
                self.write_terminal()


    # PURPOSE: Compiles a subroutine call.
    # subroutineName -> ( -> expressionList -> )
    # or
    # className | varName -> . -> subroutineName -> ( -> expressionList-> )
    def compile_subroutineCall(self) -> None:
        # subroutineName | className | varName # NOTE: previously checked
        self.write_terminal()
        # .
        if self.eat('.'):
            self.write_terminal()
            # subroutineName
            if self.isIdentifier():
                self.write_terminal()
        # (
        if self.eat('('):
            self.write_terminal()
            # expressionList
            self.compile_expressionList()
            # )
            if self.eat(')'):
                self.write_terminal()


    # PURPOSE:  Compiles an if statement.
    # if -> ( -> expression -> ) -> { -> statements -> } -> ( else -> { -> statements -> } )?
    # TODO: remove code redundancy?
    @wrap_non_terminal
    def compile_ifStatement(self) -> None: 
        # if # NOTE: previously checked
        self.write_terminal()
        # (
        if self.eat('('):
            self.write_terminal()
            # expression
            self.compile_expression()
            # )
            if self.eat(')'):
                self.write_terminal()
                # {
                if self.eat('{'):
                    self.write_terminal()
                    # statements
                    self.compile_statements()
                    # }
                    if self.eat('}'):
                        self.write_terminal()
                    # else
                    if self.eat('else'):
                        self.write_terminal()
                        # {
                        if self.eat('{'):
                            self.write_terminal()
                            # statements
                            self.compile_statements()
                            # }
                            if self.eat('}'):
                                self.write_terminal()


    # PURPOSE:  Compiles a let statement.
    # let -> varName -> ([ -> expression -> ])? -> = -> expression -> ;
    @wrap_non_terminal
    def compile_letStatement(self) -> None: 
        # let # NOTE: previously checked
        self.write_terminal()
        # varName
        if self.isIdentifier(): # NOTE: changed from isKeywordOrIdentifier
            self.write_terminal()
            # ([ -> expression -> ])?
            if self.eat('['):
                self.write_terminal()
                # expression
                self.compile_expression()
                # ]
                if self.eat(']'):
                    self.write_terminal()
            # =
            if self.eat('='):
                self.write_terminal()
                # expression
                self.compile_expression()
                # ;
                if self.eat(';'):
                    self.write_terminal()

    
    # PURPOSE:  Compiles a return statement.
    # return -> expression? -> ;
    @wrap_non_terminal
    def compile_returnStatement(self) -> None: 
        # return # NOTE: previously checked
        self.write_terminal()
        # expresssion?
        if not self.eat(';'):
            self.compile_expression()
        # ;
        if self.eat(';'):
            self.write_terminal()


    # PURPOSE:  Compiles a while statement.
    # while -> ( -> expression -> ) -> { -> statements -> }
    @wrap_non_terminal
    def compile_whileStatement(self) -> None: 
        # while # NOTE: previously checked
        self.write_terminal()
        # (
        if self.eat('('):
            self.write_terminal()
            # expression
            self.compile_expression()
            # )
            if self.eat(')'):
                self.write_terminal()
                # {
                if self.eat('{'):
                    self.write_terminal()
                    # statements
                    self.compile_statements()
                    # }
                    if self.eat('}'):
                        self.write_terminal()


    # PURPOSE:  Compiles an expression.
    # term -> (op -> term)*
    @wrap_non_terminal
    def compile_expression(self) -> None:
        # term
        self.compile_term()
        # op*
        while self.isOp():
            self.write_terminal()
            # term
            self.compile_term()
    

    # PURPOSE: Compiles a term.
    # + integerConstant | + stringConstant | + keywordConstant | 
    # + varName | + varName [ expression ] | + varName . subroutineCall | 
    # + ( expression ) | + unaryOp term
    @wrap_non_terminal
    def compile_term(self) -> None:
        # stringConstant | integerConstant | keywordConstant
        if self.isStringConstant() or self.isIntegerConstant() or self.isKeyword():
            self.write_terminal()
        # varName
        elif self.isIdentifier():
            self.write_terminal()
            # . subroutineCall
            if self.eat('.'):
                self.write_terminal()
                # subroutineCall
                self.compile_subroutineCall()
            # [ expression ]
            if self.eat('['):
                self.write_terminal()
                # expression
                self.compile_expression()
                # ]
                if self.eat(']'):
                    self.write_terminal()
        # ( expression )
        elif self.eat('('):
            self.write_terminal()
            # expression
            self.compile_expression()
            # )
            if self.eat(')'):
                self.write_terminal()
        # unaryOp term
        elif self.isUnaryOp():
            self.write_terminal()
            # term
            self.compile_term()


    # PURPOSE:  Compiles a (possibly empty) comma-separated list of expressions.
    # ( expression -> (, -> expression)* )?
    @wrap_non_terminal
    def compile_expressionList(self) -> None:
        while not self.eat(')'):
            # ,
            if self.eat(','):
                self.write_terminal()
            # expressison
            self.compile_expression()