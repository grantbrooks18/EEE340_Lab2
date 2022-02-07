"""
Test cases for the Throbac to C transpiler

Author: Brooks and Macdonald
"""

import unittest

import generic_parser
from antlr4 import ParseTreeWalker
from throbac.ThrobacLexer import ThrobacLexer
from throbac.ThrobacParser import ThrobacParser
from throbac2c import Throbac2CTranslator


def as_c(source, start_rule):
    """
    Translates the given Throbac source string to C, using start_rule for parsing.
    """
    parse_tree = generic_parser.parse(source, start_rule, ThrobacLexer, ThrobacParser)
    walker = ParseTreeWalker()
    translator = Throbac2CTranslator()
    walker.walk(translator, parse_tree)
    if hasattr(parse_tree, 'c'):
        return parse_tree.c
    else:
        return 'No generated C found'


"""
 `TEST_CASES` is a list of triples, where the first element is the expected
 C equivalent, the second is the Throbac source, and the third is the parser
 rule to be used to parse the Throbac. These are intended to be processed by
 the `test_all_cases` method in the `TranslationTest` class below.
 
For complex tests you may wish to write separate test cases, rather than using
the `TEST_CASES` approach.

The comments in `TEST_CASES` suggest a reasonable order in which to proceed with
implementation of your `Throbac2CTranslator`.
 """

TEST_CASES = [
    # numbers
    ('0', '.NIL.', 'expr'),
    ('7', '.NIL.NIL.VII.', 'expr'),  # trim leading zeroes
    ('1234567890', '.I.II.III.IV.V.VI.VII.VIII.IX.NIL.', 'expr'),
    # strings
    ('"HELLO.WORLD"', '^HELLO.WORLD^', 'expr'),
    ('""', '^^', 'expr'),
    (r'"YO\nYOYO\n\n"', '^YO+YOYO++^', 'expr'),  # Note the use of raw string to permit \n
    # alternative would have been '"YO\\nYOYO\\n\\n"'
    # booleans
    ('true', 'VERUM', 'expr'),
    ('false', 'FALSUM', 'expr'),

    # variables
    ('count', 'count', 'expr'),
    ('message', 'message', 'expr'),

    # parentheses
    ('(55)', '( .V.V. )', 'expr'),
    ('(45)', '( .IV.V. )', 'expr'),

    # compare
    ('7 > 55', ".NIL.NIL.VII. SUPRA .V.V.", 'expr'),  # TOD0 spacing handling?

    # concatenation
    ('strcat("ABC","EFG");', "^ABC^ IUNGO ^EFG^", 'expr'),
    ('strcat("SENATUS","POPULUM");', "^SENATUS^ IUNGO ^POPULUM^", 'expr'),

    # add and subtract
    ('1 + 2', '.I. ADDO .II.', 'expr'),  # should there be a comma at the end?
    ('(55) - (45)', '( .V.V. ) SUBTRAHO (.IV.V. )', 'expr'),

    # multiply and divide
    ('1 * 2', '.I. CONGERO .II.', 'expr'),
    ('(55) / (45)', '( .V.V. ) PARTIO (.IV.V. )', 'expr'),

    # negation
    ('!true', 'NI VERUM', 'expr'),
    ('!1 < 2', ' NI .I. INFRA .II.', 'expr'),
    ('!!false', ' NI NI FALSUM', 'expr'),
    ('-55', 'NEGANS .V.V.', 'expr'),
    ('55', 'NEGANS NEGANS .V.V.', 'expr'),

    # function call
    ("frobincate(2, false);", 'APUD .II., FALSUM VOCO frobincate', 'funcCall'),

    # function call expression
    ("frobincate(5 + 7, 6 * 2);", 'APUD .V. ADDO .VII., .VI. CONGERO .II. VOCO frobincate', 'expr'),
    # function call statement
    ("frobincate(5 + 7, 6 * 2);", 'APUD .V. ADDO .VII., .VI. CONGERO .II. VOCO frobincate', 'statement'),
    # assignment
    ('apple = "ORANGE";', "apple ^ORANGE^ VALORUM", 'statement'),
    # return
    ('return;', 'REDEO', 'statement'),
    ('return apple;', 'apple REDEO', 'statement'),
    # print int
    ('printf("%d", 1234567890);', ".I.II.III.IV.V.VI.VII.VIII.IX.NIL. NUMERUS.IMPRIMO", "statement"),
    ('printf("%d", num);', "num NUMERUS.IMPRIMO", "statement"),
    # print string
    ('printf("%s", string);', "string LOCUTIO.IMPRIMO", "statement"),
    (r'printf("%s", "\n");', "^+^ LOCUTIO.IMPRIMO", "statement"),
    (r'printf("%s", "\nGET.READY\n");', '^+GET.READY+^ LOCUTIO.IMPRIMO', "statement"),
    # print bool
    ('printf("%B",bool);', "bool VERITAS.IMPRIMO", "statement"),
    ('printf("%B",(1 < 2));', "(.I. INFRA .II.) VERITAS.IMPRIMO", "statement"),
    ('printf("%B",true);', "VERUM VERITAS.IMPRIMO", "statement"),
    # block
    ('printf("%s", string);\nprintf("%B",bool);', "string LOCUTIO.IMPRIMO bool VERITAS.IMPRIMO", "block"),
    ('return;\nvar = "ROMAN";', "REDEO var ^ROMAN^ VALORUM", "block"),
    # while
    ('while(true){\nprintf("%s", string);\n}', 'VERUM DUM > string LOCUTIO.IMPRIMO <', 'statement'),
    ('while(1 < 2){\nwhile(true){\nprintf("%s", string);\n}\n}',
     '.I. INFRA .II. DUM > VERUM DUM >string LOCUTIO.IMPRIMO< <', 'statement'),
    # if
    ('if (var < 2) {\n\tfrobincate(var);\n}', 'var INFRA .II. SI > APUD var VOCO frobincate <', 'statement'),
    ('if (boolean != true) {\n\treturn false;\n} else {\n\treturn true;\n}',
     'boolean NI.IDEM VERUM SI > FALSUM REDEO< ALUID > VERUM REDEO <', 'statement'),
    # nameDef
    ('int apple', 'apple : NUMERUS', 'nameDef'),
    ('bool pear', 'pear : VERITAS ', 'nameDef'),
    ('char* peach', 'peach : LOCUTIO  ', 'nameDef'),
    # varDec
    ('int apple = 0;', 'apple : NUMERUS MUTABILIS', 'varDec'),
    ('bool pear = false;', 'pear : VERITAS MUTABILIS', 'varDec'),
    ('char* peach = NULL;', 'peach : LOCUTIO  MUTABILIS', 'varDec'),
    # varBlock
    ('int apple = 0;\nbool pear = false;\nchar* peach = NULL;\n',
     'apple : NUMERUS MUTABILIS pear : VERITAS MUTABILIS peach : LOCUTIO  MUTABILIS,'
     , 'varBlock'),
    # body
    ('int apple = 0;\nbool pear = false;\nchar* peach = NULL;\n\n'  # VarBlock
     'printf("%s", string);\nprintf("%B",bool);\n',  # block
     'apple : NUMERUS MUTABILIS pear : VERITAS MUTABILIS peach : LOCUTIO  MUTABILIS'
     "string LOCUTIO.IMPRIMO bool VERITAS.IMPRIMO",
     'body'),

    # main
    ('int apple = 0;\nbool pear = false;\nchar* peach = NULL;\n\n'  # VarBlock
     'printf("%s", string);\nprintf("%B",bool);\n',  # block
     'apple : NUMERUS MUTABILIS pear : VERITAS MUTABILIS peach : LOCUTIO  MUTABILIS'
     "string LOCUTIO.IMPRIMO bool VERITAS.IMPRIMO",
     'body'),
    # funcdef
    ('int displayanddecrement(int count) {\n'
     'printf("%d", count);\n'
     'count = count - 1;\n'
     'if (count == 3) {\n\t'
     r'printf("%s", "\nGET.READY\n");'
     '\n} else {\n\t'
     r'printf("%s",' + ' ' + r'"\n");'
                             '\n}\n'
                             'return count;\n'
                             '}',
     'APUD count : NUMERUS DEFINITIO displayanddecrement PRAEBET NUMERUS >\n'
     'count NUMERUS.IMPRIMO\n'
     'count count SUBTRAHO .I. VALORUM\n'
     'count IDEM .III. SI >\n'
     '^+GET.READY+^ LOCUTIO.IMPRIMO\n'
     '< ALUID >\n'
     '^+^ LOCUTIO.IMPRIMO\n'
     '<\n'
     'count REDEO\n'
     '<\n'
     , "funcDef")
    # script

]


class TranslationTest(unittest.TestCase):

    def test_all_cases(self):
        self.maxDiff = None
        for c, throbac, rule in TEST_CASES:
            with self.subTest(c=c,
                              throbac=throbac,
                              rule=rule):
                self.assertEqual(c, as_c(throbac, rule))
