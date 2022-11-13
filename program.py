from expr.expressions import LoopExpr, DeclarationExpr
import asyncio
class Program:
    def __init__(self, declarations, loops) -> None:
        self.declarations: list[DeclarationExpr] = declarations
        self.loops: list[LoopExpr] = loops

    async def run(self):
        store = {
            'c5': 523,
            'd5': 587,
            'e5': 659,
            'f5': 698,
            'g5': 784,
            'a5': 880,
            'b5': 988,
        }
        for declaration in self.declarations:
            await declaration.eval(store)


        for loop in self.loops[0:-1]:
            asyncio.ensure_future(runEval(loop, store))

        await runEval(self.loops[-1], store)
        

async def runEval(loop: LoopExpr, store):
    while True:
        await loop.eval(store)
