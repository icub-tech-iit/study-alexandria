grammar SysMLv2;

// Lexer rules
IMPORT     : 'import';
PART       : 'part';
ATTRIBUTE  : 'attribute';
DEFAULT    : 'default';
DEF        : 'def';
COLON      : ':';
SEMICOLON  : ';';
LBRACE     : '{';
RBRACE     : '}';
LBRACK     : '[';
RBRACK     : ']';
LPAREN     : '(';
RPAREN     : ')';
EQUALS     : '=';
INTEGER    : 'Integer';
STRING     : 'String';
REAL       : 'Real';
BOOLEAN    : 'Boolean';
ARRAY      : 'Array';
SPECIALIZE : ':>>';
DIMENSIONS : 'dimensions';
ELEMENTS   : 'elements';
ID         : [a-zA-Z_][a-zA-Z0-9_]*;
SPECIALIZATION
           : [a-zA-Z_][a-zA-Z0-9_]*;
NUMBER     : DIGIT+ ('.' DIGIT+)? ;
fragment DIGIT 
           : [0-9]+ ;
STR        : '"' (~["\r\n])* '"' ;
WS         : [ \t\r\n]+ -> skip;

// Parser rules
model       : importStmt* partStmt* EOF ;
importStmt  : IMPORT ID '::*' SEMICOLON ;
partStmt    : PART (DEF)? ID (COLON SPECIALIZATION)? LBRACE partBody RBRACE ;
partBody    : (attributeStmt | partStmt)+ ;
attributeStmt
            : ATTRIBUTE (DEF)? ID COLON attributeType (DEFAULT defaultValue)? SEMICOLON? ;
attributeType
            : INTEGER | STRING | REAL | BOOLEAN | arrayType ;
defaultValue
            : NUMBER | '-'? NUMBER | STR | vector;
vector      : '(' defaultValue (',' defaultValue)* ')';
arrayType   : ARRAY LBRACE arrayBody RBRACE ;
arrayBody   : SPECIALIZE DIMENSIONS DEFAULT NUMBER SEMICOLON SPECIALIZE ELEMENTS COLON attributeType (LBRACK DIMENSIONS RBRACK)? DEFAULT defaultValue SEMICOLON ;