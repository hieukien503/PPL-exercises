import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test501(self):
        input = """
        void main()
        {
            printInteger(20);
        }"""
        output = "20"
        self.assertTrue(TestCodeGen.test(input, output, 501))