from dataclasses import dataclass

@dataclass
class Phase:
    def __init__(self, level, type, target):
        self.level = level
        self.type = type
        self.target = target