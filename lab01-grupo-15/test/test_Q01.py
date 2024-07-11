import unittest
from automata.fa.dfa import DFA
from parameterized import parameterized
from src.Q01 import dfa01

class Test_dfa01 (unittest.TestCase):
    @parameterized.expand([
        ['00','ab',True],
        ['01','ababab', True],
        ['02','abababab',True],
        ['03','aab',False],
        ['04','abb',False],
        ['05','aba',False],
        ['06','a',False],
        ['07','b',False],
        ['08','ababaabab',False],
        ['09','ababbabab',False],
        ['10','',False]
    ])

    def test_base (self, name, str, expected_result):
        result = dfa01.accepts_input(str)
        self.assertEqual(result, expected_result)

    def test_instance (self):
        self.assertTrue(isinstance(dfa01,DFA))
        self.assertSetEqual(dfa01.input_symbols,{'a','b'})

if __name__ == '__main__':
    unittest.main(verbosity=2)