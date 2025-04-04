import os

from antlr4 import FileStream, CommonTokenStream
from SysMLv2Lexer import SysMLv2Lexer
from SysMLv2Parser import SysMLv2Parser
from CustomVisitor import CustomVisitor, Element

class Utils:
    def __init__(self):
        pass

    def check_subfolders_existance(root_path, file_path):
        full_path = os.path.join(root_path, file_path)
        directory_path = os.path.dirname(full_path)

        if not os.path.exists(directory_path):
            os.makedirs(directory_path, exist_ok=True)
            
    def update(self, key, value):
        parts = key.split('.')
        obj = self
        for part in parts[1:-1]:
            obj = getattr(obj, part, None)
            if obj is None:
                raise AttributeError(f"Attribute {part} not found in {key}")
        if obj is not None:
            setattr(obj, parts[-1], value)

    def parse_sysml(file_path):
        input_stream = FileStream(file_path)
        lexer = SysMLv2Lexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = SysMLv2Parser(token_stream)

        visitor = CustomVisitor()
        tree = parser.model()
        visitor.visitModel(tree)

        return visitor
    
    def extract_overrides(override_parameters):
        overrides = {}
        for key, value in override_parameters:
            instance_name, param_name = key.split('.', 1)
            if instance_name not in overrides:
                overrides[instance_name] = {}
            overrides[instance_name][param_name] = value
        return overrides

def main():
    pass

if __name__ == '__main__':
    main()