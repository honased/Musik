from dist.musikVisitor import musikVisitor as MusikVisitor
from dist.musikParser import musikParser as MusikParser
from expr.antlrToExpr import AntlrToExpr
from expr.expressions import DeclarationExpr
from program import Program

class AntlrToProgram(MusikVisitor):
    # Visit a parse tree produced by MusikParser#prog.
    def visitProg(self, ctx:MusikParser.ProgContext):
        visitor = AntlrToExpr()
        declarations = []
        loops = []
        for i in range(ctx.getChildCount()):
            if (i != ctx.getChildCount() - 1):
                expr = visitor.visit(ctx.getChild(i))
                if (isinstance(expr, DeclarationExpr)):
                    declarations.append(expr)
                else:
                    loops.append(expr)

        return Program(declarations, loops)

        