import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):
    def test101 (self):
        self.assertTrue(TestLexer.test("ABC", "ABC,<EOF>", 101))