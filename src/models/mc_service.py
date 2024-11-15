from dataclasses import dataclass
from encoder import Encoder

class SERVICE:
    def __init__(self, type):
        self.type = type

    class PROPERTIES:
        @dataclass
        class ETHBOARD:
            type = str
        
        class JOINTMAPPING:
            @dataclass
            class ACTUATOR:
                type = list[str]
                port = list[str]
            
            class ENCODER1(Encoder):
                def __init__(self):
                    super().__init__()
            
            class ENCODER2(Encoder):
                def __init__(self):
                    super().__init__()
            