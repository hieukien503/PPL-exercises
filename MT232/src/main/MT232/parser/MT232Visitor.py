# Generated from main/MT232/parser/MT232.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MT232Parser import MT232Parser
else:
    from MT232Parser import MT232Parser

# This class defines a complete generic visitor for a parse tree produced by MT232Parser.

class MT232Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by MT232Parser#program.
    def visitProgram(self, ctx:MT232Parser.ProgramContext):
        return self.visitChildren(ctx)



del MT232Parser