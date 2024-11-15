from dataclasses import dataclass

@dataclass
class Encoder:
    type = list[str]
    port = list[str]
    position = list[str]
    resolution = list[int]
    tolerance = list[float]