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
