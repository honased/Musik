from expr.expressions import Expr, DeclarationExpr

class ExprProcessor:
    def __init__(self, expressions) -> None:
        self.expressions = expressions

    def runEvaluation(self):
        store = {}
        for expr in self.expressions:
            if (isinstance(expr, DeclarationExpr)):
                val = eval(expr.expression)
                store[expr.id] = val
                
