from dataclasses import dataclass

@dataclass
class Phase:
    level = int
    type = str
    target = str