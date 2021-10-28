import unittest
from model.parser import Parser
from model.command_type import CommandType


# PURPOSE: Tests parser module
class TestParserMethods(unittest.TestCase):

    # Initialize parser with given test data
    data = ['@100 \t \n', 'D = M + 1; JGT // Comment line', '(LOOP)', '// Comment line', 'A = A + 1\t\n', 'D ; JGT']
    parser = Parser(data)


    # PURPOSE: Returns parser to initial state
    # CHANGES: self
    def reset_parser(self):
        self.parser.current_command = None
        self.parser.current_command_number = -1

    
    # PURPOSE: Method called immediately after the test method has been called and the result recorded
    # CHANGES: self
    def tearDown(self):
        self.reset_parser()


    # PURPOSE: Tests preprocess_line function
    def test_parser_preprocess_line(self):
        compare_data = ['@100', 'D=M+1;JGT', '(LOOP)', '','A=A+1', 'D;JGT']
        for i in range(len(self.data)):
            test_line = self.data[i]
            compare_line = compare_data[i]
            self.assertEqual(self.parser.preprocess_line(test_line), compare_line)


    # PURPOSE: Tests preprocess function
    def test_preprocess(self):
        test_data = self.data
        compare_data = ['@100', 'D=M+1;JGT', '(LOOP)','A=A+1', "D;JGT"]
        self.assertEqual(self.parser.preprocess(test_data), compare_data)


    # PURPOSE: Tests hasMoreCommands function
    # CHANGES: self
    def test_hasMoreCommands(self):
        self.parser.data_size = 10

        self.parser.current_command_number = 1
        self.assertTrue(self.parser.hasMoreCommands())

        self.parser.current_command_number = 10
        self.assertFalse(self.parser.hasMoreCommands())

        self.parser.current_command_number = 33
        self.assertFalse(self.parser.hasMoreCommands())
        
        # empty data
        p = Parser([])
        self.assertFalse(p.hasMoreCommands())

   
    # PURPOSE: Tests advance function
    # CHANGES: self
    def test_advance(self):
        # initial state
        self.assertIsNone(self.parser.current_command)
        self.assertEqual(self.parser.current_command_number, -1)
        # next command
        self.parser.advance()
        self.assertEqual(self.parser.current_command, '@100')
        self.assertEqual(self.parser.current_command_number, 0)

        self.parser.advance()
        self.assertEqual(self.parser.current_command, 'D=M+1;JGT')
        self.assertEqual(self.parser.current_command_number, 1)
        
        self.parser.advance()
        self.assertEqual(self.parser.current_command, '(LOOP)')
        self.assertEqual(self.parser.current_command_number, 2)
        
        self.parser.advance()
        self.assertEqual(self.parser.current_command, 'A=A+1')
        self.assertEqual(self.parser.current_command_number, 3)

        self.parser.advance()
        self.assertEqual(self.parser.current_command, 'D;JGT')
        self.assertEqual(self.parser.current_command_number, 4)

        # try to advance past current data
        self.parser.advance()
        self.assertEqual(self.parser.current_command, 'D;JGT')
        self.assertEqual(self.parser.current_command_number, 4)

        # test on empty data
        p = Parser([])
        p.advance()
        self.assertIsNone(p.current_command)
        self.assertEqual(p.current_command_number, -1)


    # PURPOSE: Tests commandType funciton
    # CHANGES: self
    def test_commandType(self):
        # A-command test
        self.parser.advance()
        self.assertEqual(self.parser.commandType(), CommandType.A_COMMAND)
        # C-command test
        self.parser.advance()
        self.assertEqual(self.parser.commandType(), CommandType.C_COMMAND)
        # L-command test
        self.parser.advance()
        self.assertEqual(self.parser.commandType(), CommandType.L_COMMAND)


    # PURPOSE: Tests symbol function
    # CHANGES: self
    def test_symbol(self):
        # A-command test
        self.parser.advance()
        self.assertEqual(self.parser.symbol(), "100")
        # C-command test
        self.parser.advance()
        self.assertIsNone(self.parser.symbol())
        # L-command test
        self.parser.advance()
        self.assertEqual(self.parser.symbol(), "LOOP")


    # PURPOSE: Tests dest function
    # CHANGES: self
    def test_dest(self):
        # A-command test
        self.parser.advance()
        self.assertIsNone(self.parser.jump())
        # C-command test
        self.parser.advance()
        self.assertEqual(self.parser.dest(), 'D')
        # L-command test
        self.parser.advance()
        self.assertIsNone(self.parser.jump())
        # C-command test
        self.parser.advance()
        self.assertEqual(self.parser.dest(), 'A')

   
    # PURPOSE: Tests comp function
    # CHANGES: self
    def test_comp(self):
        # A-command test
        self.parser.advance()
        self.assertIsNone(self.parser.jump())
        # C-command test
        self.parser.advance()
        self.assertEqual(self.parser.comp(), 'M+1')
        # L-command test
        self.parser.advance()
        self.assertIsNone(self.parser.jump())
        # C-command test
        self.parser.advance()
        self.assertEqual(self.parser.comp(), 'A+1')
        # C-command test
        self.parser.advance()
        self.assertEqual(self.parser.comp(), 'D')


    # PURPOSE: Tests jump function
    # CHANGES: self
    def test_jump(self):
        # A-command test
        self.parser.advance()
        self.assertIsNone(self.parser.jump())
        # C-command test
        self.parser.advance()
        self.assertEqual(self.parser.jump(), 'JGT')
        # L-command test
        self.parser.advance()
        self.assertIsNone(self.parser.jump())
        # C-command test
        self.parser.advance()
        self.assertIsNone(self.parser.jump())


if __name__ == '__main__':
    unittest.main()