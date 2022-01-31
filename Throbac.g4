/*
Author: Greg Phillips

Version: 2021-01-24
*/

grammar Throbac;

script: funcDef* main EOF;

funcDef: ('APUD'  nameDef (',' nameDef)*)?
         'DEFINITIO' ID ('PRAEBET' TYPE)?
         '>' body '<';

main: body;

body : varBlock block;

varDec: nameDef 'MUTABILIS';

nameDef: ID ':' TYPE;

varBlock: varDec* ;

block : statement* ;

statement :  ID expr 'VALORUM'       # assignment
    | expr 'DUM' '>' block '<'       # while
    | expr 'SI' '>' block '<'
          ('ALUID' '>' block '<')?   # if
    | expr 'NUMERUS.IMPRIMO'         # printNumber
    | expr 'LOCUTIO.IMPRIMO'         # printString
    | expr 'VERITAS.IMPRIMO'         # printBool
    | (expr)? 'REDEO'                # return
    | funcCall                       # funcCallStmt
    ;

expr: '(' expr ')'                       # parens
    | op=('NI'|'NEGANS') expr            # negation
    | expr op=('CONGERO'|'PARTIO') expr  # mulDiv
    | expr op=('ADDO'|'SUBTRAHO') expr   # addSub
    | expr 'IUNGO' expr                  # concatenation
    | expr op=('IDEM'|'NI.IDEM'|
           'INFRA'|'INFRA.IDEM'|
           'SUPRA'|'SUPRA.IDEM') expr    # compare
    | funcCall                           # funcCallExpr
    | ID                                 # variable
    | STRING                             # string
    | NUMBER                             # number
    | BOOL                               # bool
    ;

funcCall : ('APUD' expr (',' expr)*)? 'VOCO' ID ;

NUMBER : '.' DIGIT ('.' DIGIT)* '.' ;
fragment DIGIT : 'NIL' | 'I' | 'II' | 'III' | 'IV' |
                 'V' | 'VI' | 'VII' | 'VIII' | 'IX';

STRING : '^' [A-Z.+]* '^';

BOOL: 'VERUM' | 'FALSUM';

TYPE: 'NUMERUS' | 'VERITAS' | 'LOCUTIO';

ID : [a-z]+ ;

WS : [ \t\r\n]+ -> skip ;

COMMENT : '//' ~[\r\n]* -> channel(1) ;
