import os
import sys
from JackTokenizer import JackTokenizer, LexicalElement


# The analyzer program operates on a given source, where source is either a file name
# of the form Xxx.jack or a directory name containing one or more such files. For
# each source Xxx.jack file, the analyzer goes through the following logic:
#   1. Create a JackTokenizer from the Xxx.jack input file.
#   2. Create an output file called Xxx.xml and prepare it for writing.
#   3. Use the CompilationEngine to compile the input JackTokenizer into the output
#      file.


def main():

    list_of_fps = []
    abs_pathname = os.path.abspath(sys.argv[1])
    
    # add file.jack
    if os.path.isdir(abs_pathname):
        for file in os.listdir(abs_pathname):
            if file.endswith(".jack"):
                list_of_fps.append(os.path.join(abs_pathname, file))
    else:
        list_of_fps.append(abs_pathname)
    
    # tokenize each file by fp
    for fp in list_of_fps:
        JT = JackTokenizer(fp)
        try:
            tokens_fp = fp.split('.')[0] + 'Tokens.xml' # TODO: change to T.xml
            tokenizeInput(JT, tokens_fp)
        except OSError:
            sys.exit(f"Unable to create {fp}")


# PURPOSE:  Emits tokens in output file
# CHANGES:  output file
def tokenizeInput(JT, path) -> None:
    with open(path, 'w') as out_f:
        out_f.write('<tokens>\n')
        while JT.hasMoreTokens():
            JT.advance()
            token_type = JT.tokenType()
            if token_type == LexicalElement.KEYWORD: out_f.write(f'<keyword> {JT.keyWord()} </keyword>\n')
            elif token_type == LexicalElement.SYMBOL: out_f.write(f'<symbol> {JT.symbol()} </symbol>\n')
            elif token_type == LexicalElement.IDENTIFIER: out_f.write(f'<identifier> {JT.identifier()} </identifier>\n')
            elif token_type == LexicalElement.INT_CONST: out_f.write(f'<integerConstant> {JT.intVal()} </integerConstant>\n')
            elif token_type == LexicalElement.STRING_CONST: out_f.write(f'<stringConstant> {JT.stringVal()} </stringConstant>\n')
        out_f.write('</tokens>\n')


if __name__ == "__main__":
    sys.exit(main())