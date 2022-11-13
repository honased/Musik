import asyncio
import audio.musik

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

class IfExpr(Expr):
    def __init__(self) -> None:
        super().__init__()

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

class MinusExpr(LeftRightExpr):
    async def eval(self, store):
        val = await self.left.eval(store) - await self.right.eval(store)
        return val

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

    async def eval(self, store):
        return audio.musik.sine_wave_sound(await self.interval.eval(store))

class SquareWaveExpr(Expr):
    interval = None
    def __init__(self, interval) -> None:
        self.interval = interval

    async def eval(self, store):
        return audio.musik.square_wave_sound(await self.interval.eval(store))

class NoiseWaveExpr(Expr):
    interval = None
    def __init__(self, interval) -> None:
        self.interval = interval

    async def eval(self, store):
        return audio.musik.noise_wave_sound(await self.interval.eval(store))

class SawWaveExpr(Expr):
    interval = None
    def __init__(self, interval) -> None:
        self.interval = interval

    async def eval(self, store):
        return audio.musik.saw_wave_sound(await self.interval.eval(store))

class TriangleWaveExpr(Expr):
    interval = None
    def __init__(self, interval) -> None:
        self.interval = interval

    async def eval(self, store):
        return audio.musik.triangle_wave_sound(await self.interval.eval(store))

class PlayExpr(Expr):
    sound = None
    time = None
    def __init__(self, sound, time) -> None:
        self.sound = sound
        self.time = time

    async def eval(self, store):
        snd = await self.sound.eval(store)
        tm = await self.time.eval(store)
        audio.musik.MusicManager.play_sound(snd, tm)

class PitchShiftExpr(Expr):
    sound = None
    pitch = None
    def __init__(self, sound, pitch) -> None:
        self.sound = sound
        self.pitch = pitch

    async def eval(self, store):
        snd = await self.sound.eval(store)
        pitch = await self.pitch.eval(store)
        return audio.musik.pitch_shift(snd, pitch)

class PitchShiftSemiExpr(Expr):
    sound = None
    pitch = None
    def __init__(self, sound, pitch) -> None:
        self.sound = sound
        self.pitch = pitch

    async def eval(self, store):
        snd = await self.sound.eval(store)
        pitch = await self.pitch.eval(store)
        return audio.musik.pitch_shift_semi(snd, pitch)

class MixExpr(Expr):
    sound1 = None
    sound2 = None
    def __init__(self, sound1, sound2) -> None:
        self.sound1 = sound1
        self.sound2 = sound2

    async def eval(self, store):
        snd1 = await self.sound1.eval(store)
        snd2 = await self.sound2.eval(store)
        return audio.musik.mix_sounds(snd1, snd2)

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