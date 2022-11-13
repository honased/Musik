from expr.expressions import LoopExpr, DeclarationExpr
import asyncio
class Program:
    def __init__(self, declarations, loops) -> None:
        self.declarations: list[DeclarationExpr] = declarations
        self.loops: list[LoopExpr] = loops

    async def run(self):
        store = {}
        for declaration in self.declarations:
            await declaration.eval(store)


        for loop in self.loops[0:-1]:
            asyncio.ensure_future(runEval(loop, store))

        await runEval(self.loops[-1], store)
        

async def runEval(loop: LoopExpr, store):
    while True:
        await loop.eval(store)
