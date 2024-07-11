import unittest
from automata.fa.nfa import NFA
from parameterized import parameterized
from src.Q02 import nfa01

class Test_nfa01 (unittest.TestCase):
    @parameterized.expand([
        ['00','01',True],
        ['01','001111', True],
        ['02','00001',True],
        ['03','1',True],
        ['04','111',True],
        ['05','1110',True],
        ['06','10000',True],
        ['07','010',False],
        ['08','00110',False],
        ['09','010111',False],
        ['10','000000011111011',False],
        ['11','',True]
    ])

    def test_base (self, name, str, expected_result):
        result = nfa01.accepts_input(str)
        self.assertEqual(result, expected_result)

    def test_instance (self):
        self.assertTrue(isinstance(nfa01,NFA))
        self.assertSetEqual(nfa01.input_symbols,{'0','1'})

if __name__ == '__main__':
    unittest.main(verbosity=2)