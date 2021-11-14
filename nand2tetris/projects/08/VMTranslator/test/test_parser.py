import unittest
from model.parser import Parser
from model.command_type import CommandType

class TestParserMethods(unittest.TestCase):

    # Some data to test parser
    data = [
        '// Test comment \t\n', 
        'push constant 1 \t \n', 
        'push constant 1 \t // comment goes here\n',
        'add \t// second comment\n',
        'pop local 2',
        'label LOOP_START',
        'goto END_PROGRAM',
        'if-goto COMPUTE_ELEMENT',
        'function Sys.init 0',
        'return',
        'call Class1.get 0'
    ]


    compare_data = [
        'push constant 1',
        'push constant 1',
        'add',
        'pop local 2',
        'label LOOP_START',
        'goto END_PROGRAM',
        'if-goto COMPUTE_ELEMENT',
        'function Sys.init 0',
        'return',
        'call Class1.get 0'
    ]
    

    # initialize parser with data
    parser = Parser(data)


    # PURPSOE:  Resets parser to initial state
    def reset_parser(self):
        self.parser.current_command = None
        self.parser.current_command_number = -1


    # PURPOSE:  Calls functions after each test
    def tearDown(self) -> None:
        self.reset_parser()


    # PURPOSE:  Tests preprocessed data
    def test_parser_preprocess(self):

        self.assertEqual(self.parser.data_size, len(self.compare_data))

        for i in range(self.parser.data_size):
            self.assertEqual(self.parser.data[i], self.compare_data[i])

    
    # PURPOSE:  Tests hasMoreCommands and advance funciton
    def test_hasMoreCommands(self):

        # initial position
        self.assertTrue(self.parser.hasMoreCommands())
        
        # advance once
        self.parser.advance()
        self.assertTrue(self.parser.hasMoreCommands())
        
        # try to advance past last command
        for i in range(15):
            self.parser.advance()
        # last command should stand still
        self.assertEqual(self.parser.current_command, self.compare_data[-1])

    
    # PURPOSE:  Tests commandType funciton
    def test_commandType(self):

        # initial position is null
        self.parser.advance()
        self.assertEqual(self.parser.commandType(), CommandType.C_PUSH)

        self.parser.advance()

        self.parser.advance()
        self.assertEqual(self.parser.commandType(), CommandType.C_ARITHMETIC)

        self.parser.advance()
        self.assertEqual(self.parser.commandType(), CommandType.C_POP)

        self.parser.advance()
        self.assertEqual(self.parser.commandType(), CommandType.C_LABEL)

        self.parser.advance()
        self.assertEqual(self.parser.commandType(), CommandType.C_GOTO)

        self.parser.advance()
        self.assertEqual(self.parser.commandType(), CommandType.C_IF)

        self.parser.advance()
        self.assertEqual(self.parser.commandType(), CommandType.C_FUNCTION)
        
        self.parser.advance()
        self.assertEqual(self.parser.commandType(), CommandType.C_RETURN)

        self.parser.advance()
        self.assertEqual(self.parser.commandType(), CommandType.C_CALL)


    # PURPOSE:  Tests arg1 function
    def test_arg1(self):
        # initial position is null
        self.parser.advance()
        self.assertEqual(self.parser.arg1(), 'constant')

        self.parser.advance()
        self.assertEqual(self.parser.arg1(), 'constant')

        self.parser.advance()
        self.assertEqual(self.parser.arg1(), 'add')

        self.parser.advance()
        self.assertEqual(self.parser.arg1(), 'local')

        self.parser.advance()
        self.assertEqual(self.parser.arg1(), 'LOOP_START')

        self.parser.advance()
        self.assertEqual(self.parser.arg1(), 'END_PROGRAM')

        self.parser.advance()
        self.assertEqual(self.parser.arg1(), 'COMPUTE_ELEMENT')

        self.parser.advance()
        self.assertEqual(self.parser.arg1(), 'Sys.init')

        self.parser.advance()
        self.assertEqual(self.parser.arg1(), None)

        self.parser.advance()
        self.assertEqual(self.parser.arg1(), 'Class1.get')

    
    # PURPOSE:  Tests arg2 function
    def test_arg2(self):
        # initial position is null
        self.parser.advance()
        self.assertEqual(self.parser.arg2(), '1')

        # push
        self.parser.advance()
        self.assertEqual(self.parser.arg2(), '1')

        self.parser.advance()
        self.assertEqual(self.parser.arg2(), None)

        # pop
        self.parser.advance()
        self.assertEqual(self.parser.arg2(), '2')

        # label
        self.parser.advance()

        # goto
        self.parser.advance()

        # if-goto
        self.parser.advance()

        # function
        self.parser.advance()
        self.assertEqual(self.parser.arg2(), '0')

        # return
        self.parser.advance()

        # function
        self.parser.advance()
        self.assertEqual(self.parser.arg2(), '0')        