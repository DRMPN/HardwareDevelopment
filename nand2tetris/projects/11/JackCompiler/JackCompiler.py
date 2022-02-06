import os
import sys
from CompilationEngine import *


# TODO: REWRITE!

# The analyzer program operates on a given source, where source is either a file name
# of the form Xxx.jack or a directory name containing one or more such files. For
# each source Xxx.jack file, the analyzer goes through the following logic:
#   1. Create a JackTokenizer from the Xxx.jack input file.
#   2. Create an output file called Xxx.xml and prepare it for writing.
#   3. Use the CompilationEngine to compile the input JackTokenizer into the output
#      file.


def main():

    # Ensures correct program usage
    if len(sys.argv) != 2:
        sys.exit("USAGE: \t$ python3 JackCompiler.py file.jack\n\t$ python3 JackCompiler.py directory")


    list_of_fps = []
    abs_pathname = os.path.abspath(sys.argv[1])
    

    # adds file.jack into list to process
    if os.path.isdir(abs_pathname):
        for file in os.listdir(abs_pathname):
            if file.endswith(".jack"):
                list_of_fps.append(os.path.join(abs_pathname, file))
    else:
        list_of_fps.append(abs_pathname)


    for in_path in list_of_fps:
        out_path = in_path.split('.')[0] + 'Test.vm'
        CM = CompilationEngine(in_path, out_path)
        CM.compile_class()
        #CM.dispose() # Close output file
        
        print('DONE') # TODO: remove


if __name__ == "__main__":
    sys.exit(main())