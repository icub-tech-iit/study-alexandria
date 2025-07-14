from dataclasses import dataclass, is_dataclass
from utils import parse_sysml
from base import BaseClass

class Electronics(BaseClass):
    def __post_init__(self):
        super().__init__()
        self.is_device = False
    @dataclass
    class ETH_BOARD:
        @dataclass
        class ETH_BOARD_PROPERTIES:
            IpAddress: str
            IpPort: int
            Type: str
            maxSizeRXpacket: int
            maxSizeROP: int
        @dataclass
        class ETH_BOARD_SETTINGS:
            Name: str
            @dataclass
            class RUNNINGMODE:
                period: int
                maxTimeOfRXactivity: int
                maxTimeOfDOactivity: int
                maxTimeOfTXactivity: int
                TXrateOfRegularROPs: int
            RUNNINGMODE: RUNNINGMODE 
        @dataclass
        class ETH_BOARD_ACTIONS:
            @dataclass
            class MONITOR_ITS_PRESENCE:
                enabled: bool
                timeout: float
                periodOfMissingReport: float

            MONITOR_ITS_PRESENCE: MONITOR_ITS_PRESENCE 
        ETH_BOARD_PROPERTIES: ETH_BOARD_PROPERTIES 
        ETH_BOARD_SETTINGS: ETH_BOARD_SETTINGS  
        ETH_BOARD_ACTIONS: ETH_BOARD_ACTIONS 

    @classmethod
    def from_sysml(cls, root_path):
        attr = dict(reversed(parse_sysml(root_path+'templates/electronics.sysml').part_definitions.items()))
        board = cls()

        def set_parameters(instance, attributes):
            for key, value in attributes.items():
                if key == 'electronics':
                    board.includes = value.parameters['includes'].strip('"')
                    board.folder_name = value.parameters['folder_name'].strip('"')                    
                if hasattr(instance, key):
                    subclass = getattr(instance, key)
                    if is_dataclass(subclass):
                        params = {param: (val['value'] if isinstance(val, dict) else val).strip('"') 
                                for param, val in value.parameters.items()}
                        setattr(instance, key, subclass(**params))
                    if value.children:
                        set_parameters(getattr(instance, key), {child: value.children[child] for child in value.children})

        set_parameters(board, attr)
        return board

    def to_xml(self, root_path, file_name):
        root = super().to_xml(root_path, file_name)

        self.generate_xml(root, root_path, file_name)

def main():
    pass

if __name__ == "__main__":
    main()