from antlr4 import TerminalNode, ParserRuleContext
from dist.musikVisitor import musikVisitor as MusikVisitor
from dist.musikParser import musikParser as MusikParser
from expr.expressions import *


class AntlrToExpr(MusikVisitor):
    # Visit a parse tree produced by MusikParser#DeclareNumT.
    def visitDeclareT(self, ctx:MusikParser.DeclareTContext):
        id = ctx.ID().getText()
        valExpr = self.visit(ctx.val())
        # error handling
        return DeclarationExpr(id, valExpr)

    def visitAssignT(self, ctx: MusikParser.AssignTContext):
        return (AssignExpr(
            ctx.ID().getText(),
            self.visit(ctx.val())))

    # Visit a parse tree produced by MusikParser#LoopT.
    def visitLoopT(self, ctx:MusikParser.LoopTContext):
        expressions = []
        for node in ctx.expr():
            if not isinstance(node, TerminalNode):
                expressions.append(self.visit(node))
        return LoopExpr(expressions)

    # Visit a parse tree produced by musikParser#IfT.
    def visitIfT(self, ctx:MusikParser.IfTContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MusikParser#IdT.
    def visitIdNumT(self, ctx:MusikParser.IdNumTContext):
        return VariableExpr(ctx.ID().getText())

    # Visit a parse tree produced by MusikParser#IdT.
    def visitIdSoundT(self, ctx:MusikParser.IdSoundTContext):
        return VariableExpr(ctx.ID().getText())

    # Visit a parse tree produced by MusikParser#DivT.
    def visitDivT(self, ctx:MusikParser.DivTContext):
        num = ctx.num()
        return DivExpr(
            self.visit(num[0]),
            self.visit(num[1]))

    # Visit a parse tree produced by MusikParser#MinusT.
    def visitMinusT(self, ctx:MusikParser.MinusTContext):
        num = ctx.num()
        return MinusExpr(
            self.visit(num[0]),
            self.visit(num[1]))

    # Visit a parse tree produced by MusikParser#ModT.
    def visitModT(self, ctx:MusikParser.ModTContext):
        num = ctx.num()
        return ModExpr(
            self.visit(num[0]),
            self.visit(num[1]))

    # Visit a parse tree produced by MusikParser#MultT.
    def visitMultT(self, ctx:MusikParser.MultTContext):
        num = ctx.num()
        return MultExpr(
            self.visit(num[0]),
            self.visit(num[1]))

    # Visit a parse tree produced by MusikParser#AddT.
    def visitAddT(self, ctx:MusikParser.AddTContext):
        num = ctx.num()
        return AddExpr(
            self.visit(num[0]),
            self.visit(num[1]))
            
    # Visit a parse tree produced by MusikParser#NumValT.
    def visitNumValT(self, ctx:MusikParser.NumValTContext):
        num = int(ctx.NUM().getText())
        return NumValExpr(num)


    # Visit a parse tree produced by MusikParser#SinWaveT.
    def visitSinWaveT(self, ctx:MusikParser.SinWaveTContext):
        num = ctx.num()
        return SinWaveExpr(self.visit(num))

    # Visit a parse tree produced by MusikParser#SquareWaveT.
    def visitSquareWaveT(self, ctx:MusikParser.SquareWaveTContext):
        num = ctx.num()
        return SquareWaveExpr(self.visit(num))

    # Visit a parse tree produced by MusikParser#NoiseWaveT.
    def visitNoiseWaveT(self, ctx:MusikParser.NoiseWaveTContext):
        num = ctx.num()
        return NoiseWaveExpr(self.visit(num))

    # Visit a parse tree produced by MusikParser#SawWaveT.
    def visitSawWaveT(self, ctx:MusikParser.SawWaveTContext):
        num = ctx.num()
        return SawWaveExpr(self.visit(num))

    # Visit a parse tree produced by MusikParser#TriangleWaveT.
    def visitTriangleWaveT(self, ctx:MusikParser.TriangleWaveTContext):
        num = ctx.num()
        return TriangleWaveExpr(self.visit(num))

    # Visit a parse tree produced by MusikParser#MixT.
    def visitMixT(self, ctx:MusikParser.MixTContext):
        return MixExpr(self.visit(ctx.sound()[0]), self.visit(ctx.sound()[1]))

    # Visit a parse tree produced by MusikParser#PitchShiftT.
    def visitPitchShiftT(self, ctx:MusikParser.PitchShiftTContext):
        return PitchShiftExpr(self.visit(ctx.sound()), self.visit(ctx.num()))

    # Visit a parse tree produced by MusikParser#PitchShiftSemiT.
    def visitPitchShiftSemiT(self, ctx:MusikParser.PitchShiftSemiTContext):
        return PitchShiftSemiExpr(self.visit(ctx.sound()), self.visit(ctx.num()))

    # Visit a parse tree produced by MusikParser#SleepT.
    def visitSleepT(self, ctx:MusikParser.SleepTContext):
        return SleepExpr(self.visit(ctx.num()))

    # Visit a parse tree produced by MusikParser#PlayT.
    def visitPlayT(self, ctx:MusikParser.PlayTContext):
        return PlayExpr(self.visit(ctx.sound()), self.visit(ctx.num()))
        
    def visitPrintT(self, ctx:MusikParser.PrintTContext):
        return PrintExpr(self.visit(ctx.expr()))
