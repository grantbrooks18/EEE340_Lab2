"""
When as a parse tree Listener on a valid Throbac parse tree, creates a
translation to C and stores this as a string attribute `c` on the root of
the tree, which is the `ScriptContext` node.

Author: Connor MacDonald; Grant Brooks
Author: Brooks and Macdonald
"""

from throbac.ThrobacListener import ThrobacListener
from throbac.ThrobacParser import ThrobacParser


DIGIT_MAP = {'NIL': '0', 'I': '1', 'II': '2', 'III': '3', 'IV': '4',
             'V': '5', 'VI': '6', 'VII': '7', 'VIII': '8', 'IX': '9'}


def c_block(node):
    """
    Given a parse tree node with a .c attribute, surrounds the text of the .c
    attribute with curly braces and indents each line by four spaces.
    """
    if node.c:
        lines = node.c.split('\n')
        indented_lines = [('    ' + line).rstrip() for line in lines]
        block = ('\n'.join(indented_lines))
        return f'{{\n{block}\n}}'
    else:
        return '{\n}'


class Throbac2CTranslator(ThrobacListener):

    # --- provided for you

    def exitNumber(self, ctx: ThrobacParser.NumberContext):
        throbac_number = ctx.getText()
        throbac_digits = throbac_number.strip('.').split('.')
        c_digits = [DIGIT_MAP[td] for td in throbac_digits]
        number = ''.join(c_digits)
        # str(int(...)) removes leading zeroes, since C doesn't permit them
        ctx.c = str(int(number))

    def exitString(self, ctx: ThrobacParser.StringContext):
        throbac = ctx.getText()
        c_with_pluses = f'"{throbac.strip("^")}"'
        ctx.c = c_with_pluses.replace('+', r'\n')  # note the raw string

    # --- TODO: yours to provide (not in this order - see `testcases.py`)

    def exitScript(self, ctx: ThrobacParser.ScriptContext):
        pass

    def exitFuncDef(self, ctx: ThrobacParser.FuncDefContext):
        pass

    def exitMain(self, ctx: ThrobacParser.MainContext):
        ctx.c = ctx.expr().c

    def exitBody(self, ctx: ThrobacParser.BodyContext):
        tempstring = ""

        for child in ctx.children:
            tempstring = tempstring + child.c + "\n"

        ctx.c = tempstring

        pass

    def exitVarDec(self, ctx: ThrobacParser.VarDecContext):
        testtext = ctx.children[0].c
        if "int" in testtext:
            ctx.c = testtext + ' = 0;'

        elif "bool" in testtext:
            ctx.c = testtext + ' = false;'

        elif "char*" in testtext:
            ctx.c = testtext + ' = NULL;'

    def exitNameDef(self, ctx: ThrobacParser.NameDefContext):
        testtext = ctx.getText();
        if "NUMERUS" in testtext:
            ctx.c = "int "

        elif "VERITAS" in testtext:
            ctx.c = "bool "

        elif "LOCUTIO" in testtext:
            ctx.c = "char* "

        testtext = testtext.split(":", 1)  # Isolate the ID
        ctx.c = ctx.c + testtext[0]

        pass

    def exitVarBlock(self, ctx: ThrobacParser.VarBlockContext):
        tempstring = ""

        for child in ctx.children:
            tempstring = tempstring + child.c + "\n"

        ctx.c = tempstring

    def exitBlock(self, ctx: ThrobacParser.BlockContext):
        string = []
        for statements in ctx.statement():
            string.append(statements.c)

        string = '\n'.join([str(statements) for statements in string])
        ctx.c = string

    def exitAssignment(self, ctx: ThrobacParser.AssignmentContext):
        testtext = ctx.getText()
        # print(testtext)
        testtext = testtext.split("^", 1)
        # print(testtext[0])
        ctx.c = testtext[0] + ' = ' + ctx.expr().c + ';'
        pass

    def exitWhile(self, ctx: ThrobacParser.WhileContext):
        ctx.c = 'while(' + ctx.expr().c + '){\n' + ctx.block().c + '\n}'

    def exitIf(self, ctx: ThrobacParser.IfContext):
        text = ctx.getText()
        ctx.c = 'if(' + ctx.expr().c + '){\n' + ctx.block(0).c + '\n}'
        if 'ALUID' in text:
            ctx.c = ctx.c + 'else{\n' + ctx.block(1).c + '\n}'

    def exitPrintNumber(self, ctx: ThrobacParser.PrintNumberContext):
        testtext = ctx.getText()
        if "NUMERUS" in testtext:
            testtext = testtext.split()
            ctx.c = 'printf("%i",' + ctx.expr().c + ");"

    def exitPrintString(self, ctx: ThrobacParser.PrintStringContext):
        var_name = ctx.expr().c
        ctx.c = 'printf("%s",'+var_name+');'

    def exitPrintBool(self, ctx: ThrobacParser.PrintBoolContext):
        expr = ctx.expr().c
        ctx.c = 'printf("%B",' + expr + ');'

    # Not easy
    # We need to be able to generate code that inspects the value of the inspection at runtime to evaluate and
    # Prints the right thing.

    def exitReturn(self, ctx: ThrobacParser.ReturnContext):
        text = ctx.getText()
        if text == 'REDEO':
            ctx.c = "return;"

        else:
            ctx.c = "return " + ctx.expr().c + ";"

    def exitFuncCallStmt(self, ctx: ThrobacParser.FuncCallStmtContext):
        ctx.c = ctx.children[0].c

    def exitParens(self, ctx: ThrobacParser.ParensContext):
        ctx.c = '(' + ctx.expr().c + ')'

    def exitNegation(self, ctx: ThrobacParser.NegationContext):
        throbac_negation = ctx.getText()

        if 'NI' in throbac_negation:
            ctx.c = '!' + ctx.expr().c #boolean negation

        elif 'NEGANS' in throbac_negation:
            value = 0 - int(ctx.expr().c) #arithmetic negation
            ctx.c = str(value)

    def exitCompare(self, ctx: ThrobacParser.CompareContext):
        throbac_compare = ctx.op.text

        compare_mapping = {
            'IDEM': '==',
            'NI.IDEM': '!=',
            'INFRA':  '<',
            'INFRA.IDEM': '<=',
            'SUPRA': '>',
            'SUPRA.IDEM': '>='
        }

        ctx.c = ctx.expr(0).c + compare_mapping[throbac_compare] + ctx.expr(1).c

    def exitConcatenation(self, ctx: ThrobacParser.ConcatenationContext):

        ctx.c = 'strcat(' + ctx.expr(0).c + ',' + ctx.expr(1).c + ');'

    def exitBool(self, ctx: ThrobacParser.BoolContext):
        throbac_bool = ctx.getText()
        if throbac_bool == 'VERUM':
            string = 'true'
        elif throbac_bool == 'FALSUM':
            string = 'false'

        ctx.c = string

    def exitVariable(self, ctx: ThrobacParser.VariableContext):
        throbac_var = ctx.getText()
        ctx.c = throbac_var

    def exitAddSub(self, ctx: ThrobacParser.AddSubContext):
        equation = ctx.getText();

        if "ADDO" in equation:
            ctx.c = ctx.expr(0).c + '+' + ctx.expr(1).c #+ ';' #should there be a comma at the end?

        elif "SUBTRAHO" in equation:
            ctx.c = ctx.expr(0).c + '-' + ctx.expr(1).c #+ ';' #should there be a comma at the end?

    def exitFuncCallExpr(self, ctx: ThrobacParser.FuncCallExprContext):
        ctx.c = ctx.children[0].c
        # ctx.c = ctx.expr(0).c
        # This second version doesn't work, but we're not sure why.

    def exitMulDiv(self, ctx: ThrobacParser.MulDivContext):
        equation = ctx.getText()

        if "CONGERO" in equation:
            ctx.c = ctx.expr(0).c + '*' + ctx.expr(1).c  # + ';' #should there be a comma at the end?

        elif "PARTIO" in equation:
            ctx.c = ctx.expr(0).c + '/' + ctx.expr(1).c  # + ';' #should there be a comma at the end?

    def exitFuncCall(self, ctx: ThrobacParser.FuncCallContext):
        func = ctx.getText()
        parameters = []
        num_para = 0 #number of parameters
        func = func.split('VOCO').pop() #get function name

        while ctx.expr(num_para): #get parameters
            parameters.append(ctx.expr(num_para).c)
            num_para = num_para+1

        ctx.c = func + '('
        for para in parameters: #make function call
            ctx.c = ctx.c + para
            num_para = num_para - 1
            if num_para:
                ctx.c = ctx.c + ', '
        ctx.c = ctx.c + ');'
