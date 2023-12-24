import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test201(self):
        input = """int a, b, c;
        int main()
        {
            c += ((a > b)? 0 : 1);
            printInteger(c);
        }
        """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 201))