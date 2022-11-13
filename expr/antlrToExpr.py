from antlr4 import TerminalNode, ParserRuleContext
from dist.musikVisitor import musikVisitor as MusikVisitor
from dist.musikParser import musikParser as MusikParser
from expr.expressions import *


class AntlrToExpr(MusikVisitor):
    # Visit a parse tree produced by MusikParser#DeclareNumT.
    def visitDeclareT(self, ctx:MusikParser.DeclareTContext):
        id = ctx.ID().getText()
        num = ctx.num()
        numExpr = self.visit(ctx.num())
        # error handling
        return DeclarationExpr(id, numExpr)

    # Visit a parse tree produced by MusikParser#LoopT.
    def visitLoopT(self, ctx:MusikParser.LoopTContext):
        expressions = []
        for i in range(ctx.getChildCount()):
            node = ctx.getChild(i)
            if not isinstance(node, TerminalNode):
                expressions.append(self.visit(ctx.getChild(i)))
        return LoopExpr(expressions)

    # Visit a parse tree produced by MusikParser#FuncT.
    def visitFuncT(self, ctx:MusikParser.FuncTContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MusikParser#SoundT.
    def visitSoundT(self, ctx:MusikParser.SoundTContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MusikParser#NumberT.
    def visitNumberT(self, ctx:MusikParser.NumberTContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MusikParser#AssignT.
    def visitAssignT(self, ctx:MusikParser.AssignTContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MusikParser#IdT.
    def visitIdT(self, ctx:MusikParser.IdTContext):
        return VariableExpr(ctx.ID().getText())

    # Visit a parse tree produced by MusikParser#DivT.
    def visitDivT(self, ctx:MusikParser.DivTContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MusikParser#MinusT.
    def visitMinusT(self, ctx:MusikParser.MinusTContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MusikParser#ModT.
    def visitModT(self, ctx:MusikParser.ModTContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MusikParser#MultT.
    def visitMultT(self, ctx:MusikParser.MultTContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MusikParser#NumValT.
    def visitNumValT(self, ctx:MusikParser.NumValTContext):
        num = int(ctx.NUM().getText())
        return NumValExpr(num)

    # Visit a parse tree produced by MusikParser#AddT.
    def visitAddT(self, ctx:MusikParser.AddTContext):
        num = ctx.num()
        return AddExpr(
            self.visit(num[0]),
            self.visit(num[1]))

    # Visit a parse tree produced by MusikParser#SinWaveT.
    def visitSinWaveT(self, ctx:MusikParser.SinWaveTContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MusikParser#SquareWaveT.
    def visitSquareWaveT(self, ctx:MusikParser.SquareWaveTContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MusikParser#MixT.
    def visitMixT(self, ctx:MusikParser.MixTContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MusikParser#PitchShiftT.
    def visitPitchShiftT(self, ctx:MusikParser.PitchShiftTContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MusikParser#SleepT.
    def visitSleepT(self, ctx:MusikParser.SleepTContext):
        return SleepExpr(self.visit(ctx.num()))

    # Visit a parse tree produced by MusikParser#PlayT.
    def visitPlayT(self, ctx:MusikParser.PlayTContext):
        return self.visitChildren(ctx)

    def visitPrintT(self, ctx:MusikParser.PrintTContext):
        return PrintExpr(self.visit(ctx.expr()))
