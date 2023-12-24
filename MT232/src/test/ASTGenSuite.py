import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test301(self):
        input = """
        void main()
        {
            int a = 5, b = 3, c = 8;
            int max = (a > b? a : (a > c? a : c));
        }"""
        output = ""
        self.assertTrue(TestAST.test(input, output, 301))