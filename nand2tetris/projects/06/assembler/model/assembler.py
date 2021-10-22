from parser import Parser


# TODO: https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertLogs
# TODO: implement os check args


# TODO: try - catch
# open file
file = open('test/test.txt', 'r')
# read it data
data = file.readlines()
# close file
file.close()


# initialize parser
test_parser = Parser(data)

test_parser.advance()
    

test_parser.debug() #, end=''