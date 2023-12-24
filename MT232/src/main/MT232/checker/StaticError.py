from abc import ABC, ABCMeta


class StaticError(Exception):
    pass


class Kind(ABC):
    def __str__(self):
        return self.__class__.__name__


class Variable(Kind):
    pass


class Parameter(Kind):
    pass


class Function(Kind):
    pass


class Identifier(Kind):
    pass



class Constant(Kind):
    pass


class Redeclared(StaticError):
    def __init__(self, kind: Kind, identifier: str):
        self.kind = kind
        self.identifier = identifier

    def __str__(self):
        return f"Redeclared {str(self.kind)}: {self.identifier}"


class Undeclared(StaticError):
    def __init__(self, kind: Kind, name: str):
        self.kind = kind
        self.name = name

    def __str__(self):
        return f"Undeclared {str(self.kind)}: {self.name}"


class Invalid(StaticError):
    def __init__(self, kind: Kind, name: str):
        self.kind = kind
        self.name = name

    def __str__(self):
        return f"Invalid {str(self.kind)}: {self.name}"


class TypeMismatchInExpression(StaticError):
    def __init__(self, expr):
        self.expr = expr

    def __str__(self):
        return f"Type mismatch in Expression: {str(self.expr)}"


class TypeMismatchInStatement(StaticError):
    def __init__(self, stmt):
        self.stmt = stmt

    def __str__(self):
        return f"Type mismatch in Statement: {str(self.stmt)}"


class TypeMismatchInVarDecl(StaticError):
    def __init__(self, decl):
        self.decl = decl

    def __str__(self):
        return f"Type mismatch in Variable Declaration: {str(self.decl)}"


class MustInLoop(StaticError):
    def __init__(self, stmt):
        self.stmt = stmt

    def __str__(self):
        return f"Must in loop: {str(self.stmt)}"


class IllegalArrayLiteral(StaticError):
    def __init__(self, literal):
        self.literal = literal

    def __str__(self):
        return f"Illegal array literal: {str(self.literal)}"


class FunctionNotReturn(StaticError):
    def __init__(self, func: str):
        self.func = func
    
    def __str__(self):
        return f"Function Not Return: {self.func}"


class CannotAssignToConstant(StaticError):
    def __init__(self, assign):
        self.assign = assign
    
    def __str__(self):
        return f"Cannot Assign To Constant: {str(self.assign)}"


class TypeCannotBeInferred(StaticError):
    def __init__(self, stmt):
        self.stmt = stmt
    
    def __str__(self):
        return f"Type Cannot Be Inferred: {str(self.stmt)}"
    

class NoEntryPoint(StaticError):
    def __str__(self):
        return "No entry point"