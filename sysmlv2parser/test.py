from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker
from SysMLv2Lexer import SysMLv2Lexer
from SysMLv2Parser import SysMLv2Parser
from SysMLv2Visitor import SysMLv2Visitor
from CustomVisitor import CustomVisitor

def parse_sysml(file_path):
    input_stream = FileStream(file_path)
    lexer = SysMLv2Lexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = SysMLv2Parser(token_stream)

    visitor = CustomVisitor()
    tree = parser.model()
    visitor.visit(tree)
    print(visitor.visitModel(tree))

parse_sysml("./sysml/mec.sysml")
