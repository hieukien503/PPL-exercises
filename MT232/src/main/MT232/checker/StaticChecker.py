from Visitor import Visitor
from AST import *
from Utils import Utils
from StaticError import *

class StaticChecker (Visitor, Utils):
    """
        Do not modify the check method
    """
    def __init__(self, ast):
        self.ast = ast
        self.global_env = [[]]
    
    def check(self):
        self.visit(self.ast, self.global_env)
