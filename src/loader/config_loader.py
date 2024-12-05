import json

class ConfigLoader:
    def load_config(filepath):
        with open(filepath, 'r') as file:
            return json.load(file)
