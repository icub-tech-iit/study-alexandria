from lxml import etree
from dataclasses import dataclass, fields, is_dataclass
from phase import Phase
from action import Action
from device import Device
from utils import Utils

class Cartesian(Device):
    def __init__(self, root_path):
        device = Device.from_sysml(root_path)
        super().__init__(**device.__dict__)
        self.startup = Action
        self.shutdown = Phase
        self.folder_name = str
    
    @dataclass
    class GENERAL:
        ControllerName: str
        ControllerPeriod: int
        TaskRefVelPeriodFactor: int
        SolverNameToConnect: str
        KinematicPart: str
        KinematicType: str
        PositionControl: str
        NumberOfDrivers: int
    @dataclass
    class DRIVER_0:
        Key: str
        JointsOrder: str
        MinAbsVels: list[float]
    @dataclass
    class DRIVER_1:
        Key: str
        JointsOrder: str
        MinAbsVels: list[float]
    @dataclass
    class PLANT_MODEL:
        plant_compensator: str
        smith_predictor: str
        joint_0: list[str]
        joint_1: list[str]
        joint_2: list[str]
        joint_3: list[str]
        joint_4: list[str]
        joint_5: list[str]
        joint_6: list[str]
        joint_7: list[str]
        joint_8: list[str]
        joint_9: list[str]

    @classmethod
    def from_sysml(cls, root_path):
        attr = Utils.parse_sysml(root_path+'/cartesian.sysml').part_definitions
        cartesian = cls(root_path)

        for key, value in attr.items():
            if hasattr(cls, key):
                subclass = getattr(cls, key)
                if is_dataclass(subclass):
                    params = {param: [x for x in val['value'].strip("()").split(',')] if isinstance(val, dict) else val.strip('"')
                                for param, val in value.parameters.items()}
                    setattr(cartesian, key, subclass(**params))
            elif key in ['shutdown']:
                setattr(cartesian, key, Phase.from_sysml(root_path))
            elif key in ['startup']:
                setattr(cartesian, key, Action.from_sysml(root_path))
            elif key == 'cartesian':
                cartesian.folder_name = value.parameters['folder_name'].strip('"')
        return cartesian

    def to_xml(self, root_path, file_name):
        nsmap = {'xi': 'http://www.w3.org/2001/XInclude'}
        root = etree.Element('device', {'name': str(self.device_name).strip('"'), 'type': str(self.type).strip('"')}, nsmap=nsmap)
        
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
            if attr_name == 'folder_name':
                continue
            if isinstance(attr_value, Phase) or isinstance(attr_value, Action):
                continue
            if is_dataclass(attr_value):
                _dataclass_to_xml(root, attr_name, attr_value)

        root.append(etree.XML(self.startup.to_xml()))
        root.append(etree.XML(self.shutdown.to_xml()))

        etree.indent(root, space='    ')
        doctype = '<!DOCTYPE devices PUBLIC "-//YARP//DTD yarprobotinterface 3.0//EN" "http://www.yarp.it/DTD/yarprobotinterfaceV3.0.dtd">'
        xml_object = etree.tostring(root, pretty_print=True, xml_declaration=True, encoding='UTF-8', doctype=doctype)
        with open(root_path+"/"+file_name, "wb") as writer:
            writer.write(xml_object)

def main():
    pass

if __name__ == "__main__":
    main()