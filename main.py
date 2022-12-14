from antlr4 import CommonTokenStream, InputStream
from dist.musikParser import musikParser as MusikParser
from dist.musikLexer import musikLexer as MusikLexer
import audio.musik
from expr.antlrToProgram import AntlrToProgram
import sys
import asyncio

def __main__():
    fileName = sys.argv[1]
    exprParser = getParser(fileName)
    antlrAST = exprParser.prog()
    prog = AntlrToProgram().visit(antlrAST)

    audio.musik.MusicManager.start_up()
    
    loop = asyncio.get_event_loop()
    loop.run_until_complete(prog.run())

    audio.musik.MusicManager.shut_down()
    
def getParser(fileName: str) -> MusikParser:
    data = None
    with open(fileName) as f:
        data = f.read()
    input = InputStream(data)
    lexer = MusikLexer(input)
    tokens = CommonTokenStream(lexer)
    return MusikParser(tokens)


if __name__ == '__main__':
    __main__()
