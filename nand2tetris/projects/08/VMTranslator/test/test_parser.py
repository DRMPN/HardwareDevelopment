import unittest
from model.parser import Parser
from model.command_type import CommandType

class TestParserMethods(unittest.TestCase):

    data = ['// Test comment \t\n', 
            'push constant 1 \t \n', 
            'push constant 1 \t // comment goes here\n',
            'add \t// second comment\n']

    compare_data = ['push constant 1',
                    'push constant 1',
                    'add']
    
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
        for i in range(10):
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


    # PURPOSE:  Tests arg1 function
    def test_arg1(self):
        # initial position is null
        self.parser.advance()
        self.assertEqual(self.parser.arg1(), 'constant')

        self.parser.advance()
        self.assertEqual(self.parser.arg1(), 'constant')

        self.parser.advance()
        self.assertEqual(self.parser.arg1(), 'add')

    
    # PURPOSE:  Tests arg2 function
    def test_arg1(self):
        # initial position is null
        self.parser.advance()
        self.assertEqual(self.parser.arg2(), '1')

        self.parser.advance()
        self.assertEqual(self.parser.arg2(), '1')

        self.parser.advance()
        self.assertEqual(self.parser.arg2(), None)