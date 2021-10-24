import unittest
from model.code import Code

class TestCodeMethods(unittest.TestCase):


    test_dest_data = [
        None,
        'M',
        'D',
        'MD',
        'A',
        'AM',
        'AD',
        'AMD'
    ]
    comp_dest_data = [
        '000',
        '001',
        '010',
        '011',
        '100',
        '101',
        '110',
        '111'
    ]


    test_comp_data = [
        '0',
        '1',
        '-1',
        'D',
        'A',
        '!D',
        '!A',
        '-D',
        '-A',
        'D+1',
        'A+1',
        'D-1',
        'A-1',
        'D+A',
        'D-A',
        'A-D',
        'D&A',
        'D|A',
        'M',
        '!M',
        '-M',
        'M+1',
        'M-1',
        'D+M',
        'D-M',
        'M-D',
        'D&M',
        'D|M'
    ]
    comp_comp_data = [
        '0101010',
        '0111111',
        '0111010',
        '0001100',
        '0110000',
        '0001101',
        '0110001',
        '0001111',
        '0110011',
        '0011111',
        '0110111',
        '0001110',
        '0110010',
        '0000010',
        '0010011',
        '0000111',
        '0000000',
        '0010101',
        '1110000',
        '1110001',
        '1110011',
        '1110111',
        '1110010',
        '1000010',
        '1010011',
        '1000111',
        '1000000',
        '1010101'
    ]


    test_jump_data = [
        None,
        'JGT',
        'JEQ',
        'JGE',
        'JLT',
        'JNE',
        'JLE',
        'JMP'
    ]
    comp_jump_data = [
        '000',
        '001',
        '010',
        '011',
        '100',
        '101',
        '110',
        '111'
    ]


    # PURPOSE: Tests dest funciton
    def test_dest(self):
        for i in range(len(self.test_dest_data)):
            self.assertEqual(Code.dest(self, self.test_dest_data[i]), self.comp_dest_data[i])


    # PURPOSE: Tests comp funciton
    def test_comp(self):
        for i in range(len(self.test_comp_data)):
            self.assertEqual(Code.comp(self, self.test_comp_data[i]), self.comp_comp_data[i])
    

    # PURPOSE: Tests comp funciton
    def test_jump(self):
        for i in range(len(self.test_jump_data)):
            self.assertEqual(Code.jump(self, self.test_jump_data[i]), self.comp_jump_data[i])