# Generated from musik.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .musikParser import musikParser
else:
    from musikParser import musikParser

# This class defines a complete generic visitor for a parse tree produced by musikParser.

class musikVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by musikParser#prog.
    def visitProg(self, ctx:musikParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by musikParser#DeclareT.
    def visitDeclareT(self, ctx:musikParser.DeclareTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by musikParser#LoopT.
    def visitLoopT(self, ctx:musikParser.LoopTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by musikParser#IfT.
    def visitIfT(self, ctx:musikParser.IfTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by musikParser#AssignT.
    def visitAssignT(self, ctx:musikParser.AssignTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by musikParser#FuncT.
    def visitFuncT(self, ctx:musikParser.FuncTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by musikParser#ValT.
    def visitValT(self, ctx:musikParser.ValTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by musikParser#NumT.
    def visitNumT(self, ctx:musikParser.NumTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by musikParser#SoundT.
    def visitSoundT(self, ctx:musikParser.SoundTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by musikParser#IdNumT.
    def visitIdNumT(self, ctx:musikParser.IdNumTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by musikParser#DivT.
    def visitDivT(self, ctx:musikParser.DivTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by musikParser#MinusT.
    def visitMinusT(self, ctx:musikParser.MinusTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by musikParser#ModT.
    def visitModT(self, ctx:musikParser.ModTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by musikParser#MultT.
    def visitMultT(self, ctx:musikParser.MultTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by musikParser#NumValT.
    def visitNumValT(self, ctx:musikParser.NumValTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by musikParser#AddT.
    def visitAddT(self, ctx:musikParser.AddTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by musikParser#IdSoundT.
    def visitIdSoundT(self, ctx:musikParser.IdSoundTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by musikParser#SinWaveT.
    def visitSinWaveT(self, ctx:musikParser.SinWaveTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by musikParser#SquareWaveT.
    def visitSquareWaveT(self, ctx:musikParser.SquareWaveTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by musikParser#NoiseWaveT.
    def visitNoiseWaveT(self, ctx:musikParser.NoiseWaveTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by musikParser#SawWaveT.
    def visitSawWaveT(self, ctx:musikParser.SawWaveTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by musikParser#TriangleWaveT.
    def visitTriangleWaveT(self, ctx:musikParser.TriangleWaveTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by musikParser#MixT.
    def visitMixT(self, ctx:musikParser.MixTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by musikParser#PitchShiftT.
    def visitPitchShiftT(self, ctx:musikParser.PitchShiftTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by musikParser#PitchShiftSemiT.
    def visitPitchShiftSemiT(self, ctx:musikParser.PitchShiftSemiTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by musikParser#SleepT.
    def visitSleepT(self, ctx:musikParser.SleepTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by musikParser#PlayT.
    def visitPlayT(self, ctx:musikParser.PlayTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by musikParser#PrintT.
    def visitPrintT(self, ctx:musikParser.PrintTContext):
        return self.visitChildren(ctx)



del musikParser