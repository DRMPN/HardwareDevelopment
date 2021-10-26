import unittest
from model.symbol_table import SymbolTable


class TestSymbolTableMethods(unittest.TestCase):

    # Initialize empty symbol table
    sym_tab = SymbolTable()
    data = [('i',0), ('foo', 1), ('bar', 2)]


    # Push data inside symbol table
    for (sym,add) in data:
        sym_tab.addEntry(sym,add)


    # PURPOSE: Tests contains and addEntry functions
    def test_contains(self):
        for (sym, add) in self.data:
            self.assertTrue(self.sym_tab.contains(sym))
            self.assertFalse(self.sym_tab.contains(add))


    # PURPOSE: Tests getAddress function
    def test_getAddress(self):
        for (sym, add) in self.data:
            self.assertEqual(self.sym_tab.getAddress(sym), add)