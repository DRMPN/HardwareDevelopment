import unittest
from VMWriter import *


class TestVMWriter(unittest.TestCase):

    path = '/home/hex/HardwareDevelopment/nand2tetris/projects/11/JackCompiler/test/out_test.vm'

    VMW = VMWriter(path)

    # PURPOSE: Writes test commands into an output file.
    def test_1_write_commands(self) -> None:
        self.VMW.write_push('local', '0')
        self.VMW.write_pop('argument', '2')
        # TODO: self.VMW.write_arithmetic()
        self.VMW.write_label('end')
        self.VMW.write_goto('loop')
        self.VMW.write_if('end')
        self.VMW.write_call('mult', '2')
        self.VMW.write_function('mult', '2')
        self.VMW.write_return()
        self.VMW.close()


    # PURPOSE: Tests commands from output file.
    def test_2_out_file(self) -> None:
        with open(self.path, 'r') as file:
            self.assertEqual(file.readline(), 'push local 0\n')
            self.assertEqual(file.readline(), 'pop argument 2\n')
            # TODO: arithmetic
            self.assertEqual(file.readline(), 'label end\n')
            self.assertEqual(file.readline(), 'goto loop\n')
            self.assertEqual(file.readline(), 'if-goto end\n')
            self.assertEqual(file.readline(), 'call mult 2\n')
            self.assertEqual(file.readline(), 'function mult 2\n')
            self.assertEqual(file.readline(), 'return\n')


if __name__ == '__main__':
    unittest.main()