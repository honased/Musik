# Generated from musik.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .musikParser import musikParser
else:
    from musikParser import musikParser

# This class defines a complete listener for a parse tree produced by musikParser.
class musikListener(ParseTreeListener):

    # Enter a parse tree produced by musikParser#prog.
    def enterProg(self, ctx:musikParser.ProgContext):
        pass

    # Exit a parse tree produced by musikParser#prog.
    def exitProg(self, ctx:musikParser.ProgContext):
        pass


    # Enter a parse tree produced by musikParser#DeclareT.
    def enterDeclareT(self, ctx:musikParser.DeclareTContext):
        pass

    # Exit a parse tree produced by musikParser#DeclareT.
    def exitDeclareT(self, ctx:musikParser.DeclareTContext):
        pass


    # Enter a parse tree produced by musikParser#LoopT.
    def enterLoopT(self, ctx:musikParser.LoopTContext):
        pass

    # Exit a parse tree produced by musikParser#LoopT.
    def exitLoopT(self, ctx:musikParser.LoopTContext):
        pass


    # Enter a parse tree produced by musikParser#IfT.
    def enterIfT(self, ctx:musikParser.IfTContext):
        pass

    # Exit a parse tree produced by musikParser#IfT.
    def exitIfT(self, ctx:musikParser.IfTContext):
        pass


    # Enter a parse tree produced by musikParser#AssignT.
    def enterAssignT(self, ctx:musikParser.AssignTContext):
        pass

    # Exit a parse tree produced by musikParser#AssignT.
    def exitAssignT(self, ctx:musikParser.AssignTContext):
        pass


    # Enter a parse tree produced by musikParser#FuncT.
    def enterFuncT(self, ctx:musikParser.FuncTContext):
        pass

    # Exit a parse tree produced by musikParser#FuncT.
    def exitFuncT(self, ctx:musikParser.FuncTContext):
        pass


    # Enter a parse tree produced by musikParser#ValT.
    def enterValT(self, ctx:musikParser.ValTContext):
        pass

    # Exit a parse tree produced by musikParser#ValT.
    def exitValT(self, ctx:musikParser.ValTContext):
        pass


    # Enter a parse tree produced by musikParser#NumT.
    def enterNumT(self, ctx:musikParser.NumTContext):
        pass

    # Exit a parse tree produced by musikParser#NumT.
    def exitNumT(self, ctx:musikParser.NumTContext):
        pass


    # Enter a parse tree produced by musikParser#SoundT.
    def enterSoundT(self, ctx:musikParser.SoundTContext):
        pass

    # Exit a parse tree produced by musikParser#SoundT.
    def exitSoundT(self, ctx:musikParser.SoundTContext):
        pass


    # Enter a parse tree produced by musikParser#IdNumT.
    def enterIdNumT(self, ctx:musikParser.IdNumTContext):
        pass

    # Exit a parse tree produced by musikParser#IdNumT.
    def exitIdNumT(self, ctx:musikParser.IdNumTContext):
        pass


    # Enter a parse tree produced by musikParser#DivT.
    def enterDivT(self, ctx:musikParser.DivTContext):
        pass

    # Exit a parse tree produced by musikParser#DivT.
    def exitDivT(self, ctx:musikParser.DivTContext):
        pass


    # Enter a parse tree produced by musikParser#MinusT.
    def enterMinusT(self, ctx:musikParser.MinusTContext):
        pass

    # Exit a parse tree produced by musikParser#MinusT.
    def exitMinusT(self, ctx:musikParser.MinusTContext):
        pass


    # Enter a parse tree produced by musikParser#ModT.
    def enterModT(self, ctx:musikParser.ModTContext):
        pass

    # Exit a parse tree produced by musikParser#ModT.
    def exitModT(self, ctx:musikParser.ModTContext):
        pass


    # Enter a parse tree produced by musikParser#MultT.
    def enterMultT(self, ctx:musikParser.MultTContext):
        pass

    # Exit a parse tree produced by musikParser#MultT.
    def exitMultT(self, ctx:musikParser.MultTContext):
        pass


    # Enter a parse tree produced by musikParser#NumValT.
    def enterNumValT(self, ctx:musikParser.NumValTContext):
        pass

    # Exit a parse tree produced by musikParser#NumValT.
    def exitNumValT(self, ctx:musikParser.NumValTContext):
        pass


    # Enter a parse tree produced by musikParser#AddT.
    def enterAddT(self, ctx:musikParser.AddTContext):
        pass

    # Exit a parse tree produced by musikParser#AddT.
    def exitAddT(self, ctx:musikParser.AddTContext):
        pass


    # Enter a parse tree produced by musikParser#IdSoundT.
    def enterIdSoundT(self, ctx:musikParser.IdSoundTContext):
        pass

    # Exit a parse tree produced by musikParser#IdSoundT.
    def exitIdSoundT(self, ctx:musikParser.IdSoundTContext):
        pass


    # Enter a parse tree produced by musikParser#SinWaveT.
    def enterSinWaveT(self, ctx:musikParser.SinWaveTContext):
        pass

    # Exit a parse tree produced by musikParser#SinWaveT.
    def exitSinWaveT(self, ctx:musikParser.SinWaveTContext):
        pass


    # Enter a parse tree produced by musikParser#SquareWaveT.
    def enterSquareWaveT(self, ctx:musikParser.SquareWaveTContext):
        pass

    # Exit a parse tree produced by musikParser#SquareWaveT.
    def exitSquareWaveT(self, ctx:musikParser.SquareWaveTContext):
        pass


    # Enter a parse tree produced by musikParser#NoiseWaveT.
    def enterNoiseWaveT(self, ctx:musikParser.NoiseWaveTContext):
        pass

    # Exit a parse tree produced by musikParser#NoiseWaveT.
    def exitNoiseWaveT(self, ctx:musikParser.NoiseWaveTContext):
        pass


    # Enter a parse tree produced by musikParser#MixT.
    def enterMixT(self, ctx:musikParser.MixTContext):
        pass

    # Exit a parse tree produced by musikParser#MixT.
    def exitMixT(self, ctx:musikParser.MixTContext):
        pass


    # Enter a parse tree produced by musikParser#PitchShiftT.
    def enterPitchShiftT(self, ctx:musikParser.PitchShiftTContext):
        pass

    # Exit a parse tree produced by musikParser#PitchShiftT.
    def exitPitchShiftT(self, ctx:musikParser.PitchShiftTContext):
        pass


    # Enter a parse tree produced by musikParser#SleepT.
    def enterSleepT(self, ctx:musikParser.SleepTContext):
        pass

    # Exit a parse tree produced by musikParser#SleepT.
    def exitSleepT(self, ctx:musikParser.SleepTContext):
        pass


    # Enter a parse tree produced by musikParser#PlayT.
    def enterPlayT(self, ctx:musikParser.PlayTContext):
        pass

    # Exit a parse tree produced by musikParser#PlayT.
    def exitPlayT(self, ctx:musikParser.PlayTContext):
        pass


    # Enter a parse tree produced by musikParser#PrintT.
    def enterPrintT(self, ctx:musikParser.PrintTContext):
        pass

    # Exit a parse tree produced by musikParser#PrintT.
    def exitPrintT(self, ctx:musikParser.PrintTContext):
        pass



del musikParser