# Generated from musik.g4 by ANTLR 4.11.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,24,98,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,1,0,4,0,19,8,0,11,0,12,0,20,1,0,1,0,1,1,1,1,1,1,1,
        1,1,1,1,2,1,2,1,2,4,2,33,8,2,11,2,12,2,34,1,2,1,2,1,3,1,3,1,3,1,
        3,1,3,3,3,44,8,3,1,4,1,4,3,4,48,8,4,1,5,1,5,1,5,3,5,53,8,5,1,5,1,
        5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,5,5,70,8,5,
        10,5,12,5,73,9,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,3,6,88,8,6,1,7,1,7,1,7,1,7,1,7,1,7,3,7,96,8,7,1,7,0,1,10,8,0,
        2,4,6,8,10,12,14,0,0,107,0,18,1,0,0,0,2,24,1,0,0,0,4,29,1,0,0,0,
        6,43,1,0,0,0,8,47,1,0,0,0,10,52,1,0,0,0,12,87,1,0,0,0,14,95,1,0,
        0,0,16,19,3,2,1,0,17,19,3,4,2,0,18,16,1,0,0,0,18,17,1,0,0,0,19,20,
        1,0,0,0,20,18,1,0,0,0,20,21,1,0,0,0,21,22,1,0,0,0,22,23,5,0,0,1,
        23,1,1,0,0,0,24,25,5,1,0,0,25,26,5,18,0,0,26,27,5,2,0,0,27,28,3,
        8,4,0,28,3,1,0,0,0,29,30,5,3,0,0,30,32,5,4,0,0,31,33,3,6,3,0,32,
        31,1,0,0,0,33,34,1,0,0,0,34,32,1,0,0,0,34,35,1,0,0,0,35,36,1,0,0,
        0,36,37,5,5,0,0,37,5,1,0,0,0,38,39,5,18,0,0,39,40,5,2,0,0,40,44,
        3,8,4,0,41,44,3,14,7,0,42,44,3,8,4,0,43,38,1,0,0,0,43,41,1,0,0,0,
        43,42,1,0,0,0,44,7,1,0,0,0,45,48,3,10,5,0,46,48,3,12,6,0,47,45,1,
        0,0,0,47,46,1,0,0,0,48,9,1,0,0,0,49,50,6,5,-1,0,50,53,5,18,0,0,51,
        53,5,19,0,0,52,49,1,0,0,0,52,51,1,0,0,0,53,71,1,0,0,0,54,55,10,6,
        0,0,55,56,5,6,0,0,56,70,3,10,5,7,57,58,10,5,0,0,58,59,5,7,0,0,59,
        70,3,10,5,6,60,61,10,4,0,0,61,62,5,8,0,0,62,70,3,10,5,5,63,64,10,
        3,0,0,64,65,5,9,0,0,65,70,3,10,5,4,66,67,10,2,0,0,67,68,5,10,0,0,
        68,70,3,10,5,3,69,54,1,0,0,0,69,57,1,0,0,0,69,60,1,0,0,0,69,63,1,
        0,0,0,69,66,1,0,0,0,70,73,1,0,0,0,71,69,1,0,0,0,71,72,1,0,0,0,72,
        11,1,0,0,0,73,71,1,0,0,0,74,88,5,18,0,0,75,76,5,11,0,0,76,88,3,10,
        5,0,77,78,5,12,0,0,78,88,3,10,5,0,79,80,5,13,0,0,80,81,3,12,6,0,
        81,82,3,12,6,0,82,88,1,0,0,0,83,84,5,14,0,0,84,85,3,12,6,0,85,86,
        3,10,5,0,86,88,1,0,0,0,87,74,1,0,0,0,87,75,1,0,0,0,87,77,1,0,0,0,
        87,79,1,0,0,0,87,83,1,0,0,0,88,13,1,0,0,0,89,90,5,15,0,0,90,96,3,
        10,5,0,91,92,5,16,0,0,92,96,3,12,6,0,93,94,5,17,0,0,94,96,3,6,3,
        0,95,89,1,0,0,0,95,91,1,0,0,0,95,93,1,0,0,0,96,15,1,0,0,0,10,18,
        20,34,43,47,52,69,71,87,95
    ]

class musikParser ( Parser ):

    grammarFileName = "musik.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'let'", "'='", "'loop'", "'{'", "'}'", 
                     "'*'", "'/'", "'%'", "'+'", "'-'", "'sin_wave'", "'square_wave'", 
                     "'mix'", "'pitch_shift'", "'sleep'", "'play'", "'print'", 
                     "<INVALID>", "<INVALID>", "'int'", "'sound'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "ID", "NUM", "INT_TYPE", 
                      "SOUND_TYPE", "COMMENT", "WS", "NEW_LINE" ]

    RULE_prog = 0
    RULE_decl = 1
    RULE_loop = 2
    RULE_expr = 3
    RULE_val = 4
    RULE_num = 5
    RULE_sound = 6
    RULE_func = 7

    ruleNames =  [ "prog", "decl", "loop", "expr", "val", "num", "sound", 
                   "func" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    ID=18
    NUM=19
    INT_TYPE=20
    SOUND_TYPE=21
    COMMENT=22
    WS=23
    NEW_LINE=24

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(musikParser.EOF, 0)

        def decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(musikParser.DeclContext)
            else:
                return self.getTypedRuleContext(musikParser.DeclContext,i)


        def loop(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(musikParser.LoopContext)
            else:
                return self.getTypedRuleContext(musikParser.LoopContext,i)


        def getRuleIndex(self):
            return musikParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = musikParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 18
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1]:
                    self.state = 16
                    self.decl()
                    pass
                elif token in [3]:
                    self.state = 17
                    self.loop()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 20 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1 or _la==3):
                    break

            self.state = 22
            self.match(musikParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return musikParser.RULE_decl

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class DeclareTContext(DeclContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a musikParser.DeclContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(musikParser.ID, 0)
        def val(self):
            return self.getTypedRuleContext(musikParser.ValContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclareT" ):
                listener.enterDeclareT(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclareT" ):
                listener.exitDeclareT(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclareT" ):
                return visitor.visitDeclareT(self)
            else:
                return visitor.visitChildren(self)



    def decl(self):

        localctx = musikParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decl)
        try:
            localctx = musikParser.DeclareTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(musikParser.T__0)
            self.state = 25
            self.match(musikParser.ID)
            self.state = 26
            self.match(musikParser.T__1)
            self.state = 27
            self.val()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return musikParser.RULE_loop

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class LoopTContext(LoopContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a musikParser.LoopContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(musikParser.ExprContext)
            else:
                return self.getTypedRuleContext(musikParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoopT" ):
                listener.enterLoopT(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoopT" ):
                listener.exitLoopT(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoopT" ):
                return visitor.visitLoopT(self)
            else:
                return visitor.visitChildren(self)



    def loop(self):

        localctx = musikParser.LoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_loop)
        self._la = 0 # Token type
        try:
            localctx = musikParser.LoopTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.match(musikParser.T__2)
            self.state = 30
            self.match(musikParser.T__3)
            self.state = 32 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 31
                self.expr()
                self.state = 34 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((_la) & ~0x3f) == 0 and ((1 << _la) & 1046528) != 0):
                    break

            self.state = 36
            self.match(musikParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return musikParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class FuncTContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a musikParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def func(self):
            return self.getTypedRuleContext(musikParser.FuncContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncT" ):
                listener.enterFuncT(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncT" ):
                listener.exitFuncT(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncT" ):
                return visitor.visitFuncT(self)
            else:
                return visitor.visitChildren(self)


    class ValTContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a musikParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def val(self):
            return self.getTypedRuleContext(musikParser.ValContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValT" ):
                listener.enterValT(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValT" ):
                listener.exitValT(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValT" ):
                return visitor.visitValT(self)
            else:
                return visitor.visitChildren(self)


    class AssignTContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a musikParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(musikParser.ID, 0)
        def val(self):
            return self.getTypedRuleContext(musikParser.ValContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignT" ):
                listener.enterAssignT(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignT" ):
                listener.exitAssignT(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignT" ):
                return visitor.visitAssignT(self)
            else:
                return visitor.visitChildren(self)



    def expr(self):

        localctx = musikParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_expr)
        try:
            self.state = 43
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                localctx = musikParser.AssignTContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 38
                self.match(musikParser.ID)
                self.state = 39
                self.match(musikParser.T__1)
                self.state = 40
                self.val()
                pass

            elif la_ == 2:
                localctx = musikParser.FuncTContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 41
                self.func()
                pass

            elif la_ == 3:
                localctx = musikParser.ValTContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 42
                self.val()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return musikParser.RULE_val

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SoundTContext(ValContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a musikParser.ValContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def sound(self):
            return self.getTypedRuleContext(musikParser.SoundContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSoundT" ):
                listener.enterSoundT(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSoundT" ):
                listener.exitSoundT(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSoundT" ):
                return visitor.visitSoundT(self)
            else:
                return visitor.visitChildren(self)


    class NumTContext(ValContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a musikParser.ValContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def num(self):
            return self.getTypedRuleContext(musikParser.NumContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumT" ):
                listener.enterNumT(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumT" ):
                listener.exitNumT(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumT" ):
                return visitor.visitNumT(self)
            else:
                return visitor.visitChildren(self)



    def val(self):

        localctx = musikParser.ValContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_val)
        try:
            self.state = 47
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = musikParser.NumTContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 45
                self.num(0)
                pass

            elif la_ == 2:
                localctx = musikParser.SoundTContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 46
                self.sound()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return musikParser.RULE_num

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class IdNumTContext(NumContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a musikParser.NumContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(musikParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdNumT" ):
                listener.enterIdNumT(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdNumT" ):
                listener.exitIdNumT(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdNumT" ):
                return visitor.visitIdNumT(self)
            else:
                return visitor.visitChildren(self)


    class DivTContext(NumContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a musikParser.NumContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def num(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(musikParser.NumContext)
            else:
                return self.getTypedRuleContext(musikParser.NumContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDivT" ):
                listener.enterDivT(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDivT" ):
                listener.exitDivT(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDivT" ):
                return visitor.visitDivT(self)
            else:
                return visitor.visitChildren(self)


    class MinusTContext(NumContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a musikParser.NumContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def num(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(musikParser.NumContext)
            else:
                return self.getTypedRuleContext(musikParser.NumContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMinusT" ):
                listener.enterMinusT(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMinusT" ):
                listener.exitMinusT(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMinusT" ):
                return visitor.visitMinusT(self)
            else:
                return visitor.visitChildren(self)


    class ModTContext(NumContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a musikParser.NumContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def num(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(musikParser.NumContext)
            else:
                return self.getTypedRuleContext(musikParser.NumContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModT" ):
                listener.enterModT(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModT" ):
                listener.exitModT(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModT" ):
                return visitor.visitModT(self)
            else:
                return visitor.visitChildren(self)


    class MultTContext(NumContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a musikParser.NumContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def num(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(musikParser.NumContext)
            else:
                return self.getTypedRuleContext(musikParser.NumContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultT" ):
                listener.enterMultT(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultT" ):
                listener.exitMultT(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultT" ):
                return visitor.visitMultT(self)
            else:
                return visitor.visitChildren(self)


    class NumValTContext(NumContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a musikParser.NumContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(musikParser.NUM, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumValT" ):
                listener.enterNumValT(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumValT" ):
                listener.exitNumValT(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumValT" ):
                return visitor.visitNumValT(self)
            else:
                return visitor.visitChildren(self)


    class AddTContext(NumContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a musikParser.NumContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def num(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(musikParser.NumContext)
            else:
                return self.getTypedRuleContext(musikParser.NumContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddT" ):
                listener.enterAddT(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddT" ):
                listener.exitAddT(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddT" ):
                return visitor.visitAddT(self)
            else:
                return visitor.visitChildren(self)



    def num(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = musikParser.NumContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_num, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18]:
                localctx = musikParser.IdNumTContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 50
                self.match(musikParser.ID)
                pass
            elif token in [19]:
                localctx = musikParser.NumValTContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 51
                self.match(musikParser.NUM)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 71
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 69
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = musikParser.MultTContext(self, musikParser.NumContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_num)
                        self.state = 54
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 55
                        self.match(musikParser.T__5)
                        self.state = 56
                        self.num(7)
                        pass

                    elif la_ == 2:
                        localctx = musikParser.DivTContext(self, musikParser.NumContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_num)
                        self.state = 57
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 58
                        self.match(musikParser.T__6)
                        self.state = 59
                        self.num(6)
                        pass

                    elif la_ == 3:
                        localctx = musikParser.ModTContext(self, musikParser.NumContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_num)
                        self.state = 60
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 61
                        self.match(musikParser.T__7)
                        self.state = 62
                        self.num(5)
                        pass

                    elif la_ == 4:
                        localctx = musikParser.AddTContext(self, musikParser.NumContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_num)
                        self.state = 63
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 64
                        self.match(musikParser.T__8)
                        self.state = 65
                        self.num(4)
                        pass

                    elif la_ == 5:
                        localctx = musikParser.MinusTContext(self, musikParser.NumContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_num)
                        self.state = 66
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 67
                        self.match(musikParser.T__9)
                        self.state = 68
                        self.num(3)
                        pass

             
                self.state = 73
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class SoundContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return musikParser.RULE_sound

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PitchShiftTContext(SoundContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a musikParser.SoundContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def sound(self):
            return self.getTypedRuleContext(musikParser.SoundContext,0)

        def num(self):
            return self.getTypedRuleContext(musikParser.NumContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPitchShiftT" ):
                listener.enterPitchShiftT(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPitchShiftT" ):
                listener.exitPitchShiftT(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPitchShiftT" ):
                return visitor.visitPitchShiftT(self)
            else:
                return visitor.visitChildren(self)


    class IdSoundTContext(SoundContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a musikParser.SoundContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(musikParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdSoundT" ):
                listener.enterIdSoundT(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdSoundT" ):
                listener.exitIdSoundT(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdSoundT" ):
                return visitor.visitIdSoundT(self)
            else:
                return visitor.visitChildren(self)


    class MixTContext(SoundContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a musikParser.SoundContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def sound(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(musikParser.SoundContext)
            else:
                return self.getTypedRuleContext(musikParser.SoundContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMixT" ):
                listener.enterMixT(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMixT" ):
                listener.exitMixT(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMixT" ):
                return visitor.visitMixT(self)
            else:
                return visitor.visitChildren(self)


    class SinWaveTContext(SoundContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a musikParser.SoundContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def num(self):
            return self.getTypedRuleContext(musikParser.NumContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSinWaveT" ):
                listener.enterSinWaveT(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSinWaveT" ):
                listener.exitSinWaveT(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSinWaveT" ):
                return visitor.visitSinWaveT(self)
            else:
                return visitor.visitChildren(self)


    class SquareWaveTContext(SoundContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a musikParser.SoundContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def num(self):
            return self.getTypedRuleContext(musikParser.NumContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSquareWaveT" ):
                listener.enterSquareWaveT(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSquareWaveT" ):
                listener.exitSquareWaveT(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSquareWaveT" ):
                return visitor.visitSquareWaveT(self)
            else:
                return visitor.visitChildren(self)



    def sound(self):

        localctx = musikParser.SoundContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_sound)
        try:
            self.state = 87
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18]:
                localctx = musikParser.IdSoundTContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 74
                self.match(musikParser.ID)
                pass
            elif token in [11]:
                localctx = musikParser.SinWaveTContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 75
                self.match(musikParser.T__10)
                self.state = 76
                self.num(0)
                pass
            elif token in [12]:
                localctx = musikParser.SquareWaveTContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 77
                self.match(musikParser.T__11)
                self.state = 78
                self.num(0)
                pass
            elif token in [13]:
                localctx = musikParser.MixTContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 79
                self.match(musikParser.T__12)
                self.state = 80
                self.sound()
                self.state = 81
                self.sound()
                pass
            elif token in [14]:
                localctx = musikParser.PitchShiftTContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 83
                self.match(musikParser.T__13)
                self.state = 84
                self.sound()
                self.state = 85
                self.num(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return musikParser.RULE_func

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PlayTContext(FuncContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a musikParser.FuncContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def sound(self):
            return self.getTypedRuleContext(musikParser.SoundContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPlayT" ):
                listener.enterPlayT(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPlayT" ):
                listener.exitPlayT(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPlayT" ):
                return visitor.visitPlayT(self)
            else:
                return visitor.visitChildren(self)


    class PrintTContext(FuncContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a musikParser.FuncContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(musikParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintT" ):
                listener.enterPrintT(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintT" ):
                listener.exitPrintT(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintT" ):
                return visitor.visitPrintT(self)
            else:
                return visitor.visitChildren(self)


    class SleepTContext(FuncContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a musikParser.FuncContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def num(self):
            return self.getTypedRuleContext(musikParser.NumContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSleepT" ):
                listener.enterSleepT(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSleepT" ):
                listener.exitSleepT(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSleepT" ):
                return visitor.visitSleepT(self)
            else:
                return visitor.visitChildren(self)



    def func(self):

        localctx = musikParser.FuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_func)
        try:
            self.state = 95
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                localctx = musikParser.SleepTContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 89
                self.match(musikParser.T__14)
                self.state = 90
                self.num(0)
                pass
            elif token in [16]:
                localctx = musikParser.PlayTContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 91
                self.match(musikParser.T__15)
                self.state = 92
                self.sound()
                pass
            elif token in [17]:
                localctx = musikParser.PrintTContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 93
                self.match(musikParser.T__16)
                self.state = 94
                self.expr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[5] = self.num_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def num_sempred(self, localctx:NumContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         




