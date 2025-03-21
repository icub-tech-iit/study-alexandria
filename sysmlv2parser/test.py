from antlr4 import FileStream, CommonTokenStream
from SysMLv2Lexer import SysMLv2Lexer
from SysMLv2Parser import SysMLv2Parser
from CustomVisitor import CustomVisitor

def parse_sysml(file_path):
    input_stream = FileStream(file_path)
    lexer = SysMLv2Lexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = SysMLv2Parser(token_stream)

    visitor = CustomVisitor()
    tree = parser.model()
    visitor.visitModel(tree)

    for name, element in visitor.part_definitions.items():
        print("Part " + name, element)

parse_sysml("./sysml/phase.sysml")
