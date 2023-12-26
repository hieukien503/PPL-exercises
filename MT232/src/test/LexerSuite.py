import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):
    def test101 (self):
        self.assertTrue(TestLexer.test("ABC", "ABC,<EOF>", 101))
    
    def test102 (self):
        self.assertTrue(TestLexer.test("aBC@", "aBC,Error Token @", 102))
    
    def test103 (self):
        self.assertTrue(TestLexer.test("a_BC1983", "a_BC1983,<EOF>", 103))
    
    def test104 (self):
        self.assertTrue(TestLexer.test("_abc$1983", "_abc,Error Token $", 104))
    
    def test105 (self):
        self.assertTrue(TestLexer.test("x,y", "x,Error Token ,", 105))
    
    def test106 (self):
        self.assertTrue(TestLexer.test("1_234_567", "1234567,<EOF>", 106))
    
    def test107 (self):
        self.assertTrue(TestLexer.test("234", "234,<EOF>", 107))
    
    def test108 (self):
        self.assertTrue(TestLexer.test("0234", "Error Token 0", 108))
    
    def test109 (self):
        self.assertTrue(TestLexer.test("1_296_080", "1296080,<EOF>", 109))
    
    def test110 (self):
        self.assertTrue(TestLexer.test("1_001_01", "100101,<EOF>", 110))
    
    def test111 (self):
        self.assertTrue(TestLexer.test("2.3", "2.3,<EOF>", 111))
    
    def test112 (self):
        self.assertTrue(TestLexer.test("16.108e3", "16.108e3,<EOF>", 112))
    
    def test113 (self):
        self.assertTrue(TestLexer.test(".239e-4", ".239e-4,<EOF>", 113))
    
    def test114 (self):
        self.assertTrue(TestLexer.test("2.e10", "2.e10,<EOF>", 114))
    
    def test115 (self):
        self.assertTrue(TestLexer.test("1_234E+20", "1234E+20,<EOF>", 115))
    
    def test116 (self):
        self.assertTrue(TestLexer.test("\"This is a string containing tab \t\"", "This is a string containing tab \t,<EOF>", 116))

    def test117 (self):
        self.assertTrue(TestLexer.test("""\"He asked me: \\\"Where is John?\\\"\"""", "He asked me: \\\"Where is John?\\\",<EOF>", 117))
    
    def test118 (self):
        self.assertTrue(TestLexer.test("""\"Hello\nMy name is John\"""", "Unclosed String: Hello\n", 118))
    
    def test119 (self):
        self.assertTrue(TestLexer.test("""\"Hello, My name is John""", "Unclosed String: Hello, My name is John", 119))
    
    def test120 (self):
        self.assertTrue(TestLexer.test("""\"Hello\v My name is John\"""", "Illegal Escape In String: Hello\v", 120))
    
    def test121 (self):
        self.assertTrue(TestLexer.test("// This is a comment", "<EOF>", 121))
    
    def test122 (self):
        self.assertTrue(TestLexer.test("""/*A\nMulti-line\nComment*/""", "<EOF>", 122))
    
    def test123 (self):
        self.assertTrue(TestLexer.test("""/*A Multi-line Comment""", "Unterminated Comment: /*", 123))
    
    def test124 (self):
        self.assertTrue(TestLexer.test("""// A comment /* Hi */""", "<EOF>", 124))
    
    def test125 (self):
        self.assertTrue(TestLexer.test("""/* // A line comment inside multi-line comment */""", "<EOF>", 125))