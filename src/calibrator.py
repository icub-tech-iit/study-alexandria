from lxml import etree
from dataclasses import dataclass, fields, is_dataclass
from phase import Phase
from device import Device
from utils import Utils

class Calibrator(Device):
    def __init__(self, root_path):
        device = Device.from_sysml(root_path)
        super().__init__(**device.__dict__)
        self.CALIB_ORDER = list[float]
        self.startup = Phase
        self.interrupt1 = Phase
        self.interrupt3 = Phase
    
    @dataclass
    class GENERAL:
        joints: int
        deviceName: str
    @dataclass
    class HOME:
        positionHome: list[float]
        velocityHome: list[float]

    @dataclass
    class CALIBRATION:
        calibrationType: list[float]
        calibration1: list[float]
        calibration2: list[float]
        calibration3: list[float]
        calibration4: list[float]
        calibration5: list[float]
        calibrationZero: list[float]
        calibrationDelta: list[float]
        startupPosition: list[int]
        startupVelocity: list[int]
        startupMaxPwm: list[int]
        startupPosThreshold: list[int]

    @classmethod
    def from_sysml(cls, root_path):
        attr = Utils.parse_sysml(root_path+'/calibrator.sysml').part_definitions
        calib = cls(root_path)

        for key, value in attr.items():
            if hasattr(cls, key):
                subclass = getattr(cls, key)
                if is_dataclass(subclass):
                    params = {param: [x for x in val['value'].strip("()").split(',')] if isinstance(val, dict) else val.strip('"')
                                for param, val in value.parameters.items()}
                    setattr(calib, key, subclass(**params))
            elif key == 'calibrator':
                calib.CALIB_ORDER = [x for x in value.parameters['CALIB_ORDER'].strip('"').split(',')]
            elif key in ['startup', 'interrupt1', 'interrupt3']:
                setattr(calib, key, Phase.from_sysml(root_path))
        
        return calib

    def to_xml(self, root_path, file_name):
        nsmap = {'xi': 'http://www.w3.org/2001/XInclude'}
        root = etree.Element('device', {'name': str(self.name).strip('"'), 'type': str(self.type).strip('"')}, nsmap=nsmap)
        
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
                    param.text = str(field_value.replace('(', ' ').replace(')', ' ').replace(',', ' '))

        for attr_name, attr_value in self.__dict__.items():
            if isinstance(attr_value, Phase):
                continue
            if is_dataclass(attr_value):
                _dataclass_to_xml(root, attr_name, attr_value)
        
        calib_order = etree.SubElement(root, "param", {"name": "CALIB_ORDER"})
        calib_order.text = "".join(map(str, self.CALIB_ORDER))

        root.append(etree.XML(self.startup.to_xml()))
        root.append(etree.XML(self.interrupt1.to_xml()))
        root.append(etree.XML(self.interrupt3.to_xml()))

        etree.indent(root, space='    ')
        doctype = '<!DOCTYPE devices PUBLIC "-//YARP//DTD yarprobotinterface 3.0//EN" "http://www.yarp.it/DTD/yarprobotinterfaceV3.0.dtd">'
        xml_object = etree.tostring(root, pretty_print=True, xml_declaration=True, encoding='UTF-8', doctype=doctype)
        with open(root_path+"/"+file_name, "wb") as writer:
            writer.write(xml_object)

def main():
    pass

if __name__ == "__main__":
    main()