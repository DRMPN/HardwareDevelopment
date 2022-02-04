"""VMWriter module.

Emits VM commands into a file, using the VM command syntax.
"""

import sys

class VMWriter():
    
    # PURPOSE: Creates a new file and prepares it for writing.
    def __init__(self, filepath: str) -> None:
        try:
            self.output_file = open(filepath, 'w')
        except OSError:
            sys.exit(f'Unable to open {filepath}')

    
    # PURPOSE: Writes a command to an output file.
    # NOTE: for internal use only
    def _write_command(self, command: str, *args: str):
        line = f'{command}'

        for arg in args:
            line += f' {arg}'

        line += '\n'

        self.output_file.write(line)

    
    # PURPOSE: Writes a VM push command.
    # TODO: maybe enum: const arg local static this that pointer temp
    def write_push(self, segment: str, index: str) -> None:
        self._write_command('push', segment, index)
        #self.output_file.write(f'push {segment} {index}\n')


    # PURPOSE: Writes a VM pop command.
    # TODO: maybe enum: arg local static this that pointer temp
    def write_pop(self, segment, index) -> None:
        self._write_command('pop', segment, index)

    
    # PURPOSE: Writes a VM arithmetic command.
    # TODO: maybe represent as enum: add sub neg eq gt lt and or not
    def write_arithmetic(self, command):
        if command == '+':
            self._write_command('add')

        # TODO: sub or not?

        elif command == '-':
            self._write_command('sub')
        elif command == '=':
            self._write_command('eq')
        elif command == '>':
            self._write_command('gt')
        elif command == '<':
            self._write_command('lt')
        elif command == '&':
            self._write_command('and')
        elif command == '|':
            self._write_command('or')
        elif command == '~':
            self._write_command('not')


    # PURPOSE: Writes a VM label command.
    def write_label(self, label):
        self._write_command('label', label)


    # PURPOSE: Writes a VM goto command.
    def write_goto(self, label):
        self._write_command('goto', label)


    # PURPOSE: Writes a VM if-goto command.
    def write_if(self, label):
        self._write_command('if-goto', label)


    # PURPOSE: Writes a VM call command.
    def write_call(self, name, nArgs):
        self._write_command('call', name, nArgs)


    # PURPOSE: Writes a VM function command.
    def write_function(self, name, nLocals):
        self._write_command('function', name, nLocals)

    
    # PURPOSE: Writes a VM return command.
    def write_return(self):
        self._write_command('return')


    # PURPOSE: Closes the output file.
    def close(self):
        self.output_file.close()