import asyncio

class Expr:
    async def eval(self, store):
        pass

class DeclarationExpr(Expr):
    id = None
    expression = None
    def __init__(self, id, expression) -> None:
        self.id = id
        self.expression: Expr = expression

    async def eval(self, store):
        store[self.id] = await self.expression.eval(store)

class AssignExpr(Expr):
    def __init__(self, id, val) -> None:
        self.id = id
        self.val = val

    async def eval(self, store):
        store[self.id] = await self.val.eval(store)

class VariableExpr(Expr):
    id = None
    def __init__(self, id) -> None:
        self.id = id

    async def eval(self, store):
        return store[self.id]

class LoopExpr(Expr):
    def __init__(self, expressions: list[Expr]) -> None:
        self.expressions = expressions

    async def eval(self, store):
        for expr in self.expressions:
            await expr.eval(store)

class LeftRightExpr(Expr):
    left = None
    right = None
    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right

class AddExpr(LeftRightExpr):
    async def eval(self, store):
        return await self.left.eval(store) + await self.right.eval(store)

class MultExpr(LeftRightExpr):
    async def eval(self, store):
        return await self.left.eval(store) * await self.right.eval(store)

class DivExpr(LeftRightExpr):
    async def eval(self, store):
        return await self.left.eval(store) / await self.right.eval(store)

class ModExpr(LeftRightExpr):
    async def eval(self, store):
        return await self.left.eval(store) % await self.right.eval(store)

class NumValExpr(Expr):
    num = None
    def __init__(self, num) -> None:
        self.num = num

    async def eval(self, store):
        return self.num

class SinWaveExpr(Expr):
    interval = None
    def __init__(self, interval) -> None:
        self.interval = interval

class PlayExpr(Expr):
    sound = None
    time = None
    def __init__(self, sound, time) -> None:
        self.sound = sound
        self.time = time

class SleepExpr(Expr):
    def __init__(self, time: Expr) -> None:
        self.time: Expr = time

    async def eval(self, store):
        await asyncio.sleep(await self.time.eval(store) / 1000.0)

class PrintExpr(Expr):
    def __init__(self, expression) -> None:
        self.expression: Expr = expression

    async def eval(self, store):
        print(await self.expression.eval(store))
