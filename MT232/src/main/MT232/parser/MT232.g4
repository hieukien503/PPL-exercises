grammar MT232;

@lexer::header {
from lexererr import *
}

options {
    language = Python3;
}

program: . EOF;

WS: [ \r\n\t]+ -> skip; // Skip whitespace characters

ERROR_CHAR: .;
UNCLOSED_STRING: .;
ILLEGAL_ESCAPE: .;
UNTERMINATED_COMMENT: .;