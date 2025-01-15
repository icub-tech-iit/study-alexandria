import os
import re

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
            # print("Updated", key, "with", value)

def main():
    pass

if __name__ == '__main__':
    main()