from dataclasses import dataclass
import re
class Electronics:
    @dataclass
    class ETH_BOARD:
        @dataclass
        class ETH_BOARD_PROPERTIES:
            IpAddress: str
            IpPort: int
            Type: str
            maxSizeRXpacket: str
            maxSizeROP: str
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
        @dataclass
        class ETH_BOARD_ACTIONS:
            @dataclass
            class MONITOR_ITS_PRESENCE:
                enabled: bool
                timeout: float
                periodOfMissingReport: float
    
    @classmethod
    def from_sysml(cls, file_path):
        with open(file_path, 'r') as file:
            sysml_str = file.read()
    
        def extract_attributes(block, pattern):
            matches = re.findall(pattern, block)
            return {k: eval(v) if v.isdigit() or '.' in v else v.strip('"') for k, v in matches}
        
        general_pattern = r'attribute (\w+) : \w+ default \[(.+?)\];'
        board = cls()

        ethboard_block = re.search(r'part ETH_BOARD {([^}]*)}', sysml_str)
        properties_block = re.search(r'part ETH_BOARD_PROPERTIES {([^}]*)}', sysml_str)
        settings_block = re.search(r'part ETH_BOARD_SETTINGS {([^}]*)}', sysml_str)
        runningmode_block = re.search(r'part RUNNINGMODE {([^}]*)}', sysml_str)
        actions_block = re.search(r'part ETH_BOARD_ACTIONS {([^}]*)}', sysml_str)
        monitor_block = re.search(r'part MONITOR_ITS_PRESENCE {([^}]*)}', sysml_str)

        if ethboard_block:
            if properties_block:
                ethboard_attrs = extract_attributes(properties_block.group(1), general_pattern)
                print(ethboard_attrs)
                board.ethboard = cls.ETH_BOARD.ETH_BOARD_PROPERTIES(
                    IpAddress = str(ethboard_attrs['IpAddress']),
                    IpPort = int(ethboard_attrs['IpPort']),
                    Type = str(ethboard_attrs['Type']),
                    maxSizeRXpacket = str(ethboard_attrs['maxSizeRXpacket']),
                    maxSizeROP = str(ethboard_attrs['maxSizeROP'])
                )

        if settings_block:
            settings_attrs = extract_attributes(settings_block.group(1), sysml_str)
            # print(settings_block.group(1))
            # print(general_pattern)
            # print(settings_attrs)
            # board.settings = cls.ETH_BOARD.ETH_BOARD_SETTINGS(
            #     Name = str(settings_attrs['Name'])
            # )

        return board

def main():
    eln = Electronics.from_sysml('/home/mgloria/iit/study-alexandria/sysml/eln.sysml')
    print(eln)

if __name__ == "__main__":
    main()