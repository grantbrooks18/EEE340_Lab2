# Generated from /Users/phillips/Sync/EEE340 2022/code/Lab 2 start/Throbac.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ThrobacParser import ThrobacParser
else:
    from ThrobacParser import ThrobacParser

# This class defines a complete listener for a parse tree produced by ThrobacParser.
class ThrobacListener(ParseTreeListener):

    # Enter a parse tree produced by ThrobacParser#script.
    def enterScript(self, ctx:ThrobacParser.ScriptContext):
        pass

    # Exit a parse tree produced by ThrobacParser#script.
    def exitScript(self, ctx:ThrobacParser.ScriptContext):
        pass


    # Enter a parse tree produced by ThrobacParser#funcDef.
    def enterFuncDef(self, ctx:ThrobacParser.FuncDefContext):
        pass

    # Exit a parse tree produced by ThrobacParser#funcDef.
    def exitFuncDef(self, ctx:ThrobacParser.FuncDefContext):
        pass


    # Enter a parse tree produced by ThrobacParser#main.
    def enterMain(self, ctx:ThrobacParser.MainContext):
        pass

    # Exit a parse tree produced by ThrobacParser#main.
    def exitMain(self, ctx:ThrobacParser.MainContext):
        pass


    # Enter a parse tree produced by ThrobacParser#body.
    def enterBody(self, ctx:ThrobacParser.BodyContext):
        pass

    # Exit a parse tree produced by ThrobacParser#body.
    def exitBody(self, ctx:ThrobacParser.BodyContext):
        pass


    # Enter a parse tree produced by ThrobacParser#varDec.
    def enterVarDec(self, ctx:ThrobacParser.VarDecContext):
        pass

    # Exit a parse tree produced by ThrobacParser#varDec.
    def exitVarDec(self, ctx:ThrobacParser.VarDecContext):
        pass


    # Enter a parse tree produced by ThrobacParser#nameDef.
    def enterNameDef(self, ctx:ThrobacParser.NameDefContext):
        pass

    # Exit a parse tree produced by ThrobacParser#nameDef.
    def exitNameDef(self, ctx:ThrobacParser.NameDefContext):
        pass


    # Enter a parse tree produced by ThrobacParser#varBlock.
    def enterVarBlock(self, ctx:ThrobacParser.VarBlockContext):
        pass

    # Exit a parse tree produced by ThrobacParser#varBlock.
    def exitVarBlock(self, ctx:ThrobacParser.VarBlockContext):
        pass


    # Enter a parse tree produced by ThrobacParser#block.
    def enterBlock(self, ctx:ThrobacParser.BlockContext):
        pass

    # Exit a parse tree produced by ThrobacParser#block.
    def exitBlock(self, ctx:ThrobacParser.BlockContext):
        pass


    # Enter a parse tree produced by ThrobacParser#assignment.
    def enterAssignment(self, ctx:ThrobacParser.AssignmentContext):
        pass

    # Exit a parse tree produced by ThrobacParser#assignment.
    def exitAssignment(self, ctx:ThrobacParser.AssignmentContext):
        pass


    # Enter a parse tree produced by ThrobacParser#while.
    def enterWhile(self, ctx:ThrobacParser.WhileContext):
        pass

    # Exit a parse tree produced by ThrobacParser#while.
    def exitWhile(self, ctx:ThrobacParser.WhileContext):
        pass


    # Enter a parse tree produced by ThrobacParser#if.
    def enterIf(self, ctx:ThrobacParser.IfContext):
        pass

    # Exit a parse tree produced by ThrobacParser#if.
    def exitIf(self, ctx:ThrobacParser.IfContext):
        pass


    # Enter a parse tree produced by ThrobacParser#printNumber.
    def enterPrintNumber(self, ctx:ThrobacParser.PrintNumberContext):
        pass

    # Exit a parse tree produced by ThrobacParser#printNumber.
    def exitPrintNumber(self, ctx:ThrobacParser.PrintNumberContext):
        pass


    # Enter a parse tree produced by ThrobacParser#printString.
    def enterPrintString(self, ctx:ThrobacParser.PrintStringContext):
        pass

    # Exit a parse tree produced by ThrobacParser#printString.
    def exitPrintString(self, ctx:ThrobacParser.PrintStringContext):
        pass


    # Enter a parse tree produced by ThrobacParser#printBool.
    def enterPrintBool(self, ctx:ThrobacParser.PrintBoolContext):
        pass

    # Exit a parse tree produced by ThrobacParser#printBool.
    def exitPrintBool(self, ctx:ThrobacParser.PrintBoolContext):
        pass


    # Enter a parse tree produced by ThrobacParser#return.
    def enterReturn(self, ctx:ThrobacParser.ReturnContext):
        pass

    # Exit a parse tree produced by ThrobacParser#return.
    def exitReturn(self, ctx:ThrobacParser.ReturnContext):
        pass


    # Enter a parse tree produced by ThrobacParser#funcCallStmt.
    def enterFuncCallStmt(self, ctx:ThrobacParser.FuncCallStmtContext):
        pass

    # Exit a parse tree produced by ThrobacParser#funcCallStmt.
    def exitFuncCallStmt(self, ctx:ThrobacParser.FuncCallStmtContext):
        pass


    # Enter a parse tree produced by ThrobacParser#number.
    def enterNumber(self, ctx:ThrobacParser.NumberContext):
        pass

    # Exit a parse tree produced by ThrobacParser#number.
    def exitNumber(self, ctx:ThrobacParser.NumberContext):
        pass


    # Enter a parse tree produced by ThrobacParser#parens.
    def enterParens(self, ctx:ThrobacParser.ParensContext):
        pass

    # Exit a parse tree produced by ThrobacParser#parens.
    def exitParens(self, ctx:ThrobacParser.ParensContext):
        pass


    # Enter a parse tree produced by ThrobacParser#negation.
    def enterNegation(self, ctx:ThrobacParser.NegationContext):
        pass

    # Exit a parse tree produced by ThrobacParser#negation.
    def exitNegation(self, ctx:ThrobacParser.NegationContext):
        pass


    # Enter a parse tree produced by ThrobacParser#compare.
    def enterCompare(self, ctx:ThrobacParser.CompareContext):
        pass

    # Exit a parse tree produced by ThrobacParser#compare.
    def exitCompare(self, ctx:ThrobacParser.CompareContext):
        pass


    # Enter a parse tree produced by ThrobacParser#concatenation.
    def enterConcatenation(self, ctx:ThrobacParser.ConcatenationContext):
        pass

    # Exit a parse tree produced by ThrobacParser#concatenation.
    def exitConcatenation(self, ctx:ThrobacParser.ConcatenationContext):
        pass


    # Enter a parse tree produced by ThrobacParser#string.
    def enterString(self, ctx:ThrobacParser.StringContext):
        pass

    # Exit a parse tree produced by ThrobacParser#string.
    def exitString(self, ctx:ThrobacParser.StringContext):
        pass


    # Enter a parse tree produced by ThrobacParser#bool.
    def enterBool(self, ctx:ThrobacParser.BoolContext):
        pass

    # Exit a parse tree produced by ThrobacParser#bool.
    def exitBool(self, ctx:ThrobacParser.BoolContext):
        pass


    # Enter a parse tree produced by ThrobacParser#variable.
    def enterVariable(self, ctx:ThrobacParser.VariableContext):
        pass

    # Exit a parse tree produced by ThrobacParser#variable.
    def exitVariable(self, ctx:ThrobacParser.VariableContext):
        pass


    # Enter a parse tree produced by ThrobacParser#addSub.
    def enterAddSub(self, ctx:ThrobacParser.AddSubContext):
        pass

    # Exit a parse tree produced by ThrobacParser#addSub.
    def exitAddSub(self, ctx:ThrobacParser.AddSubContext):
        pass


    # Enter a parse tree produced by ThrobacParser#funcCallExpr.
    def enterFuncCallExpr(self, ctx:ThrobacParser.FuncCallExprContext):
        pass

    # Exit a parse tree produced by ThrobacParser#funcCallExpr.
    def exitFuncCallExpr(self, ctx:ThrobacParser.FuncCallExprContext):
        pass


    # Enter a parse tree produced by ThrobacParser#mulDiv.
    def enterMulDiv(self, ctx:ThrobacParser.MulDivContext):
        pass

    # Exit a parse tree produced by ThrobacParser#mulDiv.
    def exitMulDiv(self, ctx:ThrobacParser.MulDivContext):
        pass


    # Enter a parse tree produced by ThrobacParser#funcCall.
    def enterFuncCall(self, ctx:ThrobacParser.FuncCallContext):
        pass

    # Exit a parse tree produced by ThrobacParser#funcCall.
    def exitFuncCall(self, ctx:ThrobacParser.FuncCallContext):
        pass



del ThrobacParser