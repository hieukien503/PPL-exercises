import unittest
from TestUtils import TestChecker

class CheckerSuite(unittest.TestCase):
    def test401(self):
        input = """
        int f(int a = 0, int b, int c)
        {
            return a + b + c;
        }
        void main()
        {
        
        }"""
        output = ""
        self.assertTrue(TestChecker.test(input, output, 401))