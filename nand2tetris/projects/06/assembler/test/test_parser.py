from model.parser import CommandType, Parser
import unittest


class TestParserMethods(unittest.TestCase):

    '''
    test_data = None
    path_to_test_file = 'test/test.txt'

    compare_data = None
    path_to_compare_file = 'test/compare.txt'


    # Init test objects
    def setUp(self):

        # open test file and read its context
        file = open(self.path_to_test_file, 'r')
        self.test_data = file.readlines()
        file.close()
        
        # open compare file and read its context
        file = open(self.path_to_compare_file, 'r')
        self.compare_data = file.readlines()
        file.close()

        self.parser = Parser(self.test_data)


    # Test parser's instance variables
    def test_init_parser(self):

        self.assertEqual(self.parser.current_command, None)
        self.assertEqual(self.parser.current_command_type, None)
        self.assertEqual(self.parser.current_command_number, 0)
        self.assertEqual(self.parser.data, self.test_data)
    '''


    # Initialize empty parser
    data = ['Des troy\nRock\t ', '// Comment Line', 'Some Thing // Comment line']
    parser = Parser(data)
    

    # PURPOSE: Tests preprocess_line function
    # TODO: add tests with actual code
    def test_parser_preprocess_line(self):
        compare_data = ['DestroyRock', '', 'SomeThing']
        for i in range(len(self.data)):
            test_line = self.data[i]
            compare_line = compare_data[i]
            self.assertEqual(self.parser.preprocess_line(test_line), compare_line)


    # PURPOSE: Tests preprocess function
    # TODO: add test with actual code
    def test_preprocess(self):
        test_data = self.data
        compare_data = ['DestroyRock','SomeThing']
        self.assertEqual(self.parser.preprocess(test_data), compare_data)

    
    # PURPOSE: Tests hasMoreCommands function
    def test_hasMoreCommands(self):
        self.parser.data_size = 10

        self.parser.current_command_number = 1
        self.assertEqual(self.parser.hasMoreCommands(), True)

        self.parser.current_command_number = 10
        self.assertEqual(self.parser.hasMoreCommands(), False)

        self.parser.current_command_number = 33
        self.assertEqual(self.parser.hasMoreCommands(), False)
        # empty data
        p = Parser([])
        self.assertEqual(p.hasMoreCommands(), False)

    
    # PURPOSE: Tests advance function
    def test_advance(self):
        # initial position
        self.assertEqual(self.parser.current_command, None)
        self.assertEqual(self.parser.current_command_number, -1)

        self.parser.advance()
        self.assertEqual(self.parser.current_command, 'DestroyRock')
        self.assertEqual(self.parser.current_command_number, 0)

        self.parser.advance()
        self.assertEqual(self.parser.current_command, 'SomeThing')
        self.assertEqual(self.parser.current_command_number, 1)
        # try to advance past current data
        self.parser.advance()
        self.assertEqual(self.parser.current_command, 'SomeThing')
        self.assertEqual(self.parser.current_command_number, 1)
        # empty data
        p = Parser([])
        p.advance()
        self.assertEqual(p.current_command, None)
        self.assertEqual(p.current_command_number, -1)


    # PURPOSE: Tests commandType
    def test_commandType(self):
        p = Parser([])

        a_command = "000000000000001"
        p.current_command = a_command
        self.assertEqual(p.commandType(), CommandType.A_COMMAND)

        c_command = "1110111111001000"
        p.current_command = c_command
        self.assertEqual(p.commandType(), CommandType.C_COMMAND)
        
        l_command = "(LOOP)"
        p.current_command = l_command
        self.assertEqual(p.commandType(), CommandType.L_COMMAND)


if __name__ == '__main__':
    unittest.main()