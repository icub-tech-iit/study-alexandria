from dataclasses import dataclass
from base import BaseClass

class skinSpec(BaseClass):
    def __init__(self, root_path):
        super().__init__()
    @dataclass
    class defaultCfgBoard:
        period: int
        skinType: int
        noLoad: str
        diagnostic: bool
    @dataclass
    class defaultCfgTriangle:
        enabled: bool
        shift: int
        cdcOffset: str
    @dataclass
    class specialCfgTriangles:
        numOfSets: int
        triangleSetCfg1: list[int]
        triangleSetCfg2: list[int]
        triangleSetCfg3: list[int]
        triangleSetCfg4: list[int]
        triangleSetCfg5: list[int]
        triangleSetCfg6: list[int]
        triangleSetCfg7: list[int]
        triangleSetCfg8: list[int]
        triangleSetCfg9: list[int]
        triangleSetCfg10: list[int]
        triangleSetCfg11: list[int]
        triangleSetCfg12: list[int]
        triangleSetCfg13: list[int]
        triangleSetCfg14: list[int]
        triangleSetCfg15: list[int]
        triangleSetCfg16: list[int]
        triangleSetCfg17: list[int]
        triangleSetCfg18: list[int]
        triangleSetCfg19: list[int]
        triangleSetCfg20: list[int]

    @classmethod
    def from_sysml(cls, root_path):
        return super().from_sysml(root_path)
    
    def to_xml(self, root_path, file_name):
        root = super().to_xml(root_path, file_name)

        self.generate_xml(root, root_path, file_name)

def main():
    pass

if __name__ == "__main__":
    main()