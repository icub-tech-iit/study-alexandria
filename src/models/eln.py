from dataclasses import dataclass, is_dataclass, asdict, fields
from lxml import etree
import re
class Electronics:
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
        @dataclass
        class ETH_BOARD_ACTIONS:
            @dataclass
            class MONITOR_ITS_PRESENCE:
                enabled: bool
                timeout: float
                periodOfMissingReport: float
    
    @classmethod
    def from_sysml(cls, root_path):
        with open(root_path+'/eln.sysml', 'r') as file:
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

        board.eth_board = cls.ETH_BOARD()
        board.eth_board_properties = cls.ETH_BOARD.ETH_BOARD_PROPERTIES(
            IpAddress = attr['IpAddress'],
            IpPort = attr['IpPort'],
            Type = attr['Type'],
            maxSizeRXpacket = attr['maxSizeRXpacket'],
            maxSizeROP = attr['maxSizeROP']
        )

        board.eth_board_settings = cls.ETH_BOARD.ETH_BOARD_SETTINGS(
            Name = attr['Name']
        )
        board.running_mode = cls.ETH_BOARD.ETH_BOARD_SETTINGS.RUNNINGMODE(
            period = attr['period'],
            maxTimeOfRXactivity = attr['maxTimeOfRXactivity'],
            maxTimeOfDOactivity = attr['maxTimeOfDOactivity'],
            maxTimeOfTXactivity = attr['maxTimeOfTXactivity'],
            TXrateOfRegularROPs = attr['TXrateOfRegularROPs']
        )

        board.eth_board_actions = cls.ETH_BOARD.ETH_BOARD_ACTIONS()
        board.monitor_its_presence = cls.ETH_BOARD.ETH_BOARD_ACTIONS.MONITOR_ITS_PRESENCE(
            enabled = attr['enabled'],
            timeout = attr['timeout'],
            periodOfMissingReport = attr['periodOfMissingReport']
        )

        return board

    def to_xml(self, root_path):
        nsmap = {'xi': 'http://www.w3.org/2001/XInclude'}
        root = etree.Element('params', {'robot': '', 'build': '1'}, nsmap=nsmap)

        def _dataclass_to_xml(parent, name, dataclass_instance):
            group_elem = etree.SubElement(parent, "group", {"name": name.upper()})
            for field_name, field_value in asdict(dataclass_instance).items():
                if fields(dataclass_instance):
                    param = etree.SubElement(group_elem, "param", {"name": field_name})
                    param.text = " ".join(map(str, field_value)) if isinstance(field_value, list) else str(field_value)                    
                else:
                    _dataclass_to_xml(group_elem, field_name, field_value)
        for attr_name, attr_value in self.__dict__.items():
            if is_dataclass(attr_value):
                _dataclass_to_xml(root, attr_name, attr_value)

        # Write to file
        etree.indent(root, space='    ')
        doctype = '<!DOCTYPE params PUBLIC "-//YARP//DTD yarprobotinterface 3.0//EN" "http://www.yarp.it/DTD/yarprobotinterfaceV3.0.dtd">'
        xml_object = etree.tostring(root, pretty_print=True, xml_declaration=True, encoding='UTF-8', doctype=doctype)
        with open(root_path + 'eln.xml', "wb") as writer:
            writer.write(xml_object)

def main():
    eln = Electronics.from_sysml('/home/mgloria/iit/study-alexandria/sysml/')
    eln.to_xml('/home/mgloria/iit/study-alexandria/sysml/')

if __name__ == "__main__":
    main()