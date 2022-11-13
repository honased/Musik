from antlr4 import CommonTokenStream, InputStream
from dist.musikParser import musikParser as MusikParser
from dist.musikLexer import musikLexer as MusikLexer
from expr.antlrToProgram import AntlrToProgram
import sys
import asyncio

def __main__():
    fileName = sys.argv[1]
    exprParser = getParser(fileName)
    antlrAST = exprParser.prog()
    prog = AntlrToProgram().visit(antlrAST)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(prog.run())
    
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
