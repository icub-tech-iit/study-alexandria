from dataclasses import dataclass, is_dataclass, fields
from lxml import etree
from utils import Utils
class Mechanicals:
    @dataclass
    class GENERAL:
        MotioncontrolVersion: int
        Joints: int
        AxisMap: list[int]
        AxisName: list[str]
        AxisType: list[str]
        Encoder: list[float]
        fullscalePWM: list[int]
        ampsToSensor: list[float]
        Gearbox_M2J: list[float]
        Gearbox_E2J: list[int]
        useMotorSpeedFbk: list[int]
        MotorType: list[str]
        Verbose: int
    @dataclass
    class LIMITS:
        hardwareJntPosMin: list[int]
        hardwareJntPosMax: list[int]
        rotorPosMin: list[int]
        rotorPosMax: list[int]
    @dataclass
    class _2FOC:
        HasHallSensor: list[int]
        HasTempSensor: list[int]
        HasRotorEncoder: list[int]
        HasRotorEncoderIndex: list[int]
        HasSpeedEncoder: list[int]
        RotorIndexOffset: list[int]
        MotorPoles: list[int]         
    @dataclass
    class COUPLINGS:
        matrixJ2M: list[list[float]]
        matrixM2J: list[list[float]]
        matrixE2J: list[list[float]]
    @dataclass
    class JOINTSET_CFG:
        numberofsets: int
        @dataclass
        class JOINTSET_0:
            listofjoints: list[int]
            constraintName: str
            param1: int
            param2: int
        @dataclass
        class JOINTSET_1:
            listofjoints: list[int]
            constraintName: str
            param1: int
            param2: int
        @dataclass
        class JOINTSET_2:
            listofjoints: list[int]
            constraintName: str
            param1: int
            param2: int
        JOINTSET_0: JOINTSET_0
        JOINTSET_1: JOINTSET_1
        JOINTSET_2: JOINTSET_2

    @classmethod
    def from_sysml(cls, root_path):
        attr = dict(Utils.parse_sysml(root_path+'/mec.sysml').part_definitions.items())
        mec = cls()

        def set_parameters(instance, attributes):
            for key, value in attributes.items():
                if hasattr(instance, key):
                    subclass = getattr(instance, key)
                    if is_dataclass(subclass):
                        params = {param: [x for x in val['value'].strip("()").split(',')] if isinstance(val, dict) else val.strip('"')
                                for param, val in value.parameters.items()}
                        setattr(instance, key, subclass(**params))
                    if value.children:
                        set_parameters(getattr(instance, key), {child: value.children[child] for child in value.children})
        set_parameters(mec, attr)
        return mec
    
    def to_xml(self, root_path, file_name):
        nsmap = {'xi': 'http://www.w3.org/2001/XInclude'}
        root = etree.Element('params', {'robot': '', 'build': '1'}, nsmap=nsmap)
        
        Utils.check_subfolders_existance(root_path, file_name)
        
        def _dataclass_to_xml(parent, name, dataclass_instance):
            group_elem = etree.SubElement(parent, "group", {"name": name.upper().strip('_')})

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
            if is_dataclass(attr_value):
                _dataclass_to_xml(root, attr_name, attr_value)

        etree.indent(root, space='    ')
        doctype = '<!DOCTYPE params PUBLIC "-//YARP//DTD yarprobotinterface 3.0//EN" "http://www.yarp.it/DTD/yarprobotinterfaceV3.0.dtd">'
        xml_object = etree.tostring(root, pretty_print=True, xml_declaration=True, encoding='UTF-8', doctype=doctype)
        with open(root_path+'/'+file_name, "wb") as writer:
            writer.write(xml_object)

def main():
    pass

if __name__ == "__main__":
    main()