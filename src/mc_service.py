from dataclasses import dataclass
from encoder import Encoder
from base import BaseClass

class Service(BaseClass):
    def __init__(self, root_path):
        super().__init__()

    @dataclass
    class SERVICE:
        type: list[str]
        @dataclass
        class PROPERTIES:
            @dataclass
            class ETHBOARD:
                type: str
            @dataclass
            class CANBOARDS:
                type: str
                @dataclass
                class PROTOCOL:
                    major: list[int]
                    minor: list[int]
                @dataclass
                class FIRMWARE:
                    major: list[int]
                    minor: list[int]
                    build: list[int]
                PROTOCOL: PROTOCOL
                FIRMWARE: FIRMWARE
            @dataclass
            class MAIS:
                location: str
            @dataclass
            class JOINTMAPPING:
                @dataclass
                class ACTUATOR:
                    type: list[str]
                    _port: list[str]
                ACTUATOR: ACTUATOR
                ENCODER1: Encoder = None
                ENCODER2: Encoder = None
            ETHBOARD: ETHBOARD
            CANBOARDS: CANBOARDS
            MAIS: MAIS
            JOINTMAPPING: JOINTMAPPING
        PROPERTIES: PROPERTIES
    SERVICE: SERVICE

    @classmethod
    def from_sysml(cls, root_path):
        return super().from_sysml(root_path)

    def to_xml(self, root_path, file_name):
        root = super().to_xml(root_path, file_name)

        self.generate_xml(root, root_path, file_name)
        
def main():
    pass

if __name__ == '__main__':
    main()