from dataclasses import dataclass, is_dataclass, fields
from lxml import etree
from utils import Utils

class Electronics:
    def __init__(self):
        self.includes = str
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
        attr = dict(reversed(Utils.parse_sysml(root_path+'/eln.sysml').part_definitions.items()))
        board = cls()

        def set_parameters(instance, attributes):
            for key, value in attributes.items():
                if key == 'electronics':
                    board.includes = value.parameters['includes'].strip('"')
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
        xi_ns = 'http://www.w3.org/2001/XInclude'
        nsmap = {'xi': xi_ns}
        root = etree.Element('params', {'robot': '', 'build': '1'}, nsmap=nsmap)

        Utils.check_subfolders_existance(root_path, file_name)

        def _dataclass_to_xml(parent, name, dataclass_instance):
            group_elem = etree.SubElement(parent, "group", {"name": name.upper()})

            for field in fields(dataclass_instance):
                field_name = field.name
                field_value = getattr(dataclass_instance, field_name)
                
                if is_dataclass(field_value):
                    _dataclass_to_xml(group_elem, field_name, field_value) 
                elif isinstance(field_value, list):
                    if any(isinstance(i, list) for i in field_value):
                        param = etree.SubElement(group_elem, "param", {"name": field_name})
                        formatted_text = "\n".join(
                            "   ".join(map(str, row)) for row in field_value
                        )
                        param.text = f"\n{formatted_text}\n"
                    else:
                        param = etree.SubElement(group_elem, "param", {"name": field_name})
                        param.text = "   ".join(map(str, field_value))
                else:
                    param = etree.SubElement(group_elem, "param", {"name": field_name})
                    param.text = str(field_value)

        for attr_name, attr_value in self.__dict__.items():
            if attr_name == 'includes':	
                etree.SubElement(root, f'{{{xi_ns}}}include', href=attr_value)
            if is_dataclass(attr_value):
                _dataclass_to_xml(root, attr_name, attr_value)

        etree.indent(root, space='    ')
        doctype = '<!DOCTYPE params PUBLIC "-//YARP//DTD yarprobotinterface 3.0//EN" "http://www.yarp.it/DTD/yarprobotinterfaceV3.0.dtd">'
        xml_object = etree.tostring(root, pretty_print=True, xml_declaration=True, encoding='UTF-8', doctype=doctype)
        with open(root_path+"/"+file_name, "wb") as writer:
            writer.write(xml_object)

def main():
    pass

if __name__ == "__main__":
    main()