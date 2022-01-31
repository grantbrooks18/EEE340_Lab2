"""
Translates the Throbac programs in the THROBAC_DIR to equivalent C programs,
assuming there's a correct implementation of a `Throbac2CTranslator` in the
`throbac2c` module. Generated files will be placed in `PYTHON_DIR`.

Author: Greg Phillips

Version: 2022-01-23
"""

import os.path
import sys
import traceback

import generic_parser
from antlr4 import ParseTreeWalker
from throbac.ThrobacLexer import ThrobacLexer
from throbac.ThrobacParser import ThrobacParser
from throbac2c import Throbac2CTranslator

THROBAC_DIR = 'throbac_source'
C_DIR = 'generated_c'

if __name__ == '__main__':
    if not os.path.exists(C_DIR):
        os.makedirs(C_DIR)
    else:
        for old_c in os.listdir(C_DIR):
            if old_c.endswith('.c'):
                os.remove(os.path.join(C_DIR, old_c))

    for throbac_name in os.listdir(THROBAC_DIR):
        if throbac_name.endswith('.throbac'):
            throbac_path = os.path.join(THROBAC_DIR, throbac_name)
            try:
                parse_tree = generic_parser.parse(throbac_path, 'script',
                                                  ThrobacLexer, ThrobacParser,
                                                  from_file=True)
                walker = ParseTreeWalker()
                translator = Throbac2CTranslator()

                # -----------------------------------------------------------
                # translation happens here; the generated C is stored as
                # parse_tree.c
                walker.walk(translator, parse_tree)
                # -----------------------------------------------------------

                c_name = '.'.join(throbac_name.split('.')[:-1]) + '.c'
                c_path = os.path.join(C_DIR, c_name)
                with open(c_path, 'w') as python_file:
                    python_file.write(parse_tree.c)

            except generic_parser.SyntaxErrors as e:
                print(f'\nSyntax errors in {throbac_path}\n\n{str(e)}',
                      file=sys.stderr)

            except Exception as e:
                print(f'\nError processing {throbac_path}\n\n{traceback.format_exc()}',
                      file=sys.stderr)
