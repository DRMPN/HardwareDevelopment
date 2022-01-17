import sys
import unittest
from JackTokenizer import JackTokenizer

# python3 -m unittest

class TestJackTokenizerMethods(unittest.TestCase):
    
    test_path = "test/test_data.jack"
    verify_path = "test/verify_data.jack"
    verify_data = []

    try:
        with open(verify_path, 'r') as f:
            for line in f:
                verify_data += line
    except OSError:
        sys.exit(f"Unable to open {verify_path}")

    JT = JackTokenizer(test_path)


    def test_preprocessed_data(self):
        self.assertEqual(self.verify_data, self.JT.data)