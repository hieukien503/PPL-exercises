# Generated from main/MT232/parser/MT232.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\7")
        buf.write("\34\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3")
        buf.write("\2\7\2\20\n\2\f\2\16\2\23\13\2\3\3\3\3\3\4\3\4\3\5\3\5")
        buf.write("\3\6\3\6\2\2\7\3\3\5\4\7\5\t\6\13\7\3\2\4\5\2C\\aac|\6")
        buf.write("\2\62;C\\aac|\2\34\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2")
        buf.write("\2\t\3\2\2\2\2\13\3\2\2\2\3\r\3\2\2\2\5\24\3\2\2\2\7\26")
        buf.write("\3\2\2\2\t\30\3\2\2\2\13\32\3\2\2\2\r\21\t\2\2\2\16\20")
        buf.write("\t\3\2\2\17\16\3\2\2\2\20\23\3\2\2\2\21\17\3\2\2\2\21")
        buf.write("\22\3\2\2\2\22\4\3\2\2\2\23\21\3\2\2\2\24\25\13\2\2\2")
        buf.write("\25\6\3\2\2\2\26\27\13\2\2\2\27\b\3\2\2\2\30\31\13\2\2")
        buf.write("\2\31\n\3\2\2\2\32\33\13\2\2\2\33\f\3\2\2\2\4\2\21\2")
        return buf.getvalue()


class MT232Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ID = 1
    ERROR_CHAR = 2
    UNCLOSED_STRING = 3
    ILLEGAL_ESCAPE = 4
    UNTERMINATED_COMMENT = 5

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "ID", "ERROR_CHAR", "UNCLOSED_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    ruleNames = [ "ID", "ERROR_CHAR", "UNCLOSED_STRING", "ILLEGAL_ESCAPE", 
                  "UNTERMINATED_COMMENT" ]

    grammarFileName = "MT232.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


