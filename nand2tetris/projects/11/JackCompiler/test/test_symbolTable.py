import unittest
from SymbolTable import *

# python3 -m unittest

class TestSymbolTable(unittest.TestCase):
    
    # PURPOSE: Creates new symbol table and fills it with test data.
    def setUp(self) -> None:
        self.ST = SymbolTable()
        self.test_class_define()
        self.test_subroutine_define()
        return super().setUp()


    # PURPOSE: Tests define function.
    # CHANGES: ST
    def test_class_define(self) -> None:
        self.ST.define('nAccounts', 'int', 'static')
        self.ST.define('bankCommission', 'int', 'static')
        self.ST.define('id', 'int', 'field')
        self.ST.define('owner', 'String', 'field')
        self.ST.define('balance', 'int', 'field')
    

    # PURPOSE: Tests define function.
    # CHANGES: ST
    def test_subroutine_define(self) -> None:
        self.ST.define('this', 'BankAccount', 'arg')
        self.ST.define('sum', 'int', 'arg')
        self.ST.define('i', 'int', 'var')
        self.ST.define('j', 'int', 'var')

    
    # PURPOSE: Tests var_count function.
    def test_var_count(self) -> None:
        self.assertEqual(self.ST.var_count('static'), 2)
        self.assertEqual(self.ST.var_count('field'), 3)

        self.assertEqual(self.ST.var_count('arg'), 2)
        self.assertEqual(self.ST.var_count('var'), 2)

    
    # PURPOSE: Tests kind_of function.
    def test_kind_of(self) -> None:
        self.assertEqual(self.ST.kind_of('nAccounts'), 'static')
        self.assertEqual(self.ST.kind_of('id'), 'field')

        self.assertEqual(self.ST.kind_of('this'), 'arg')
        self.assertEqual(self.ST.kind_of('i'), 'var')
        

    # PURPOSE: Tests type_of function.
    def test_type_of(self) -> None:
        self.assertEqual(self.ST.type_of('bankCommission'), 'int')
        self.assertEqual(self.ST.type_of('owner'), 'String')

        self.assertEqual(self.ST.type_of('this'), 'BankAccount')
        self.assertEqual(self.ST.type_of('i'), 'int')

    
    # PURPOSE: Tests index_of function.
    def test_index_of(self) -> None:
        self.assertEqual(self.ST.index_of('nAccounts'), 0)
        self.assertEqual(self.ST.index_of('bankCommission'), 1)
        self.assertEqual(self.ST.index_of('id'), 0)
        self.assertEqual(self.ST.index_of('owner'), 1)
        self.assertEqual(self.ST.index_of('balance'), 2)

        self.assertEqual(self.ST.index_of('this'), 0)
        self.assertEqual(self.ST.index_of('sum'), 1)
        self.assertEqual(self.ST.index_of('i'), 0)
        self.assertEqual(self.ST.index_of('j'), 1)

    
    # PURPOSE: Tests start_subroutine function.
    def test_start_subroutine(self) -> None:
        self.ST.start_subroutine()
        self.assertEqual(self.ST.subroutineTable, [])
        
        self.test_subroutine_define()
        self.test_index_of()


if __name__ == '__main__':
    unittest.main()