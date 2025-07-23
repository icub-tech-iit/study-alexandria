grammar SysMLv2;

// Lexer rules
IMPORT     : 'import';
PART       : 'part';
PACKAGE    : 'package';
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
COMMA      : ',';
INTEGER    : 'Integer';
STRING     : 'String';
REAL       : 'Real';
BOOLEAN    : 'Boolean';
FALSE      : 'false';
TRUE       : 'true';
ARRAY      : 'Array';
SPECIALIZE : ':>';
OVERRIDE   : ':>>';
DIMENSIONS : 'dimensions';
ELEMENTS   : 'elements';
ID         : [a-zA-Z_][a-zA-Z0-9_]*;
qualifiedID 
           : ID ('.' ID)* ;
NUMBER     : DIGIT+ ('.' DIGIT+)? ;
fragment DIGIT 
           : [0-9]+ ;
STR        : '"' (~["\r\n])* '"' ;
WS         : [ \t\r\n]+ -> skip;

// Parser rules
model       : importStmt* (partStmt | attributeStmt | packageStmt)* EOF ;
packageStmt : PACKAGE ID LBRACE (attributeStmt | partStmt)+ RBRACE ;
importStmt  : IMPORT ID '::*' SEMICOLON ;
partStmt    : PART (DEF)? ID ((COLON ID) | (SPECIALIZE | COLON) ID)? (LBRACE (partBody | overrideBody)+ RBRACE | SEMICOLON) ;
partBody    : (attributeStmt | partStmt)+ ;
overrideBody: OVERRIDE qualifiedID EQUALS defaultValue SEMICOLON ;
attributeStmt
            : ATTRIBUTE (DEF)? ID (LBRACE attributeStmt RBRACE)? COLON attributeType (DEFAULT defaultValue)? SEMICOLON? ;
attributeType
            : INTEGER | STRING | REAL | BOOLEAN | arrayType | ID ;
defaultValue
            : NUMBER | ('-' | '+')? NUMBER | STR | vector | bool;
bool        : TRUE | FALSE;
vector      : LPAREN defaultValue (COMMA defaultValue)* COMMA? RPAREN;
arrayType   : ARRAY LBRACE arrayBody RBRACE ;
arrayBody   : OVERRIDE DIMENSIONS DEFAULT NUMBER SEMICOLON OVERRIDE ELEMENTS COLON attributeType (LBRACK DIMENSIONS RBRACK)? DEFAULT defaultValue SEMICOLON ;