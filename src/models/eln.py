from dataclasses import dataclass
import re
class Electronics:
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
        class ETH_BOARD_ACTIONS:
            @dataclass
            class MONITOR_ITS_PRESENCE:
                enabled: bool
                timeout: float
                periodOfMissingReport: float
    
    @classmethod
    def from_sysml(cls, root_path, file_path):
        with open(root_path+file_path, 'r') as file:
            sysml_str = file.read()
    
        def extract_attributes(block, pattern):
            matches = re.findall(pattern, block)
            attributes = {}
            for match in matches:
                key = match[0]
                if match[1]:
                    value = float(match[1])
                elif match[2]:
                    value = int(match[2])
                else:
                    value = match[3]
                attributes[key] = value
            return attributes
        
        general_pattern = r'attribute (\w+) : \w+ default (?:(\d+(\.\d*)?)|"([^"]*)");' #catch integer/float with sign or quoted string
        # general_pattern = r'attribute (\w+) : \w+ default (?:(\d+)|"([^"]*)");'
        board = cls()
        attr = extract_attributes(sysml_str, general_pattern)

        board.eth_board = cls.ETH_BOARD.ETH_BOARD_PROPERTIES(
            IpAddress = attr['IpAddress'],
            IpPort = attr['IpPort'],
            Type = attr['Type'],
            maxSizeRXpacket = attr['maxSizeRXpacket'],
            maxSizeROP = attr['maxSizeROP']
        )

        board.ethboard_settings = cls.ETH_BOARD.ETH_BOARD_SETTINGS(
            Name = attr['Name']
        )
        board.running_mode = cls.ETH_BOARD.ETH_BOARD_SETTINGS.RUNNINGMODE(
            period = attr['period'],
            maxTimeOfRXactivity = attr['maxTimeOfRXactivity'],
            maxTimeOfDOactivity = attr['maxTimeOfDOactivity'],
            maxTimeOfTXactivity = attr['maxTimeOfTXactivity'],
            TXrateOfRegularROPs = attr['TXrateOfRegularROPs']
        )

        board.monitor_its_presence = cls.ETH_BOARD.ETH_BOARD_ACTIONS.MONITOR_ITS_PRESENCE(
            enabled = attr['enabled'],
            timeout = attr['timeout'],
            periodOfMissingReport = attr['periodOfMissingReport']
        )

        return board

def main():
    eln = Electronics.from_sysml('/home/mgloria/iit/study-alexandria/sysml','/eln.sysml')
    print(eln.eth_board.Type)

if __name__ == "__main__":
    main()