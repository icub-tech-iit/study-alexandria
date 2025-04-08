from dataclasses import dataclass, is_dataclass, asdict, fields
from lxml import etree
from device import Device
from utils import Utils

class motorControl(Device):
    def __init__(self, root_path):
        self.root_path = root_path
        device = Device.from_sysml(root_path)
        super().__init__(**device.__dict__)

    @dataclass
    class LIMITS:
        jntPosMin: list[int]
        jntPosMax: list[int]
        jntVelMax: list[int]
        motorOverloadCurrents: list[int]
        motorNominalCurrents: list[int]
        motorPeakCurrents: list[int]
        motorPwmLimit: list[int]
    
    @dataclass
    class TIMEOUTS:
        velocity: list[int]

    @dataclass
    class IMPEDANCE:
        stiffness: list[float]
        damping: list[float]

    @dataclass
    class CONTROLS:
        positionControl: list[str]
        velocityControl: list[str]
        mixedControl: list[str]
        torqueControl: list[str]
        currentPid: list[str]
        speedPid: list[str]

    @dataclass
    class POS_PID_DEFAULT:
        controlLaw: str
        outputType: str
        fbkControlUnits: str
        outputControlUnits: str
        kp: list[int]
        kd: list[int]
        ki: list[int]
        maxOutput: list[int]
        maxInt: list[int]
        stictionUp: list[int]
        stictionDown: list[int]
        kff: list[int]
    @dataclass
    class TRQ_PID_DEFAULT:
        controlLaw: str
        outputType: str
        fbkControlUnits: str
        outputControlUnits: str
        kp: list[int]
        kd: list[int]
        ki: list[int]
        maxOutput: list[int]
        maxInt: list[int]
        ko: list[int]
        stictionUp: list[int]
        stictionDown: list[int]
        kff: list[int]
        viscousPos: list[float]
        viscousNeg: list[float]
        coulombPos: list[int]
        coulombNeg: list[int]
        velocityThres: list[int]
        filterType: list[int]
        ktau: list[int]
    @dataclass
    class _2FOC_CUR_CONTROL:
        controlLaw: str
        fbkControlUnits: str
        outputControlUnits: str
        kp: list[int]
        kd: list[int]
        ki: list[int]
        shift: list[int]
        maxOutput: list[int]
        maxInt: list[int]
        kff: list[int]
    @dataclass
    class _2FOC_VEL_CONTROL:
        controlLaw: str
        fbkControlUnits: str
        outputControlUnits: str
        kff: list[int]
        kp: list[int]
        kd: list[int]
        ki: list[int]
        shift: list[int]
        maxOutput: list[int]
        maxInt: list[int]
        
    @classmethod
    def from_sysml(cls, root_path):
        attr = dict(Utils.parse_sysml(root_path+'/motorControl.sysml').part_definitions.items())
        mc = cls(root_path)

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

        set_parameters(mc, attr)
        return mc
    
    def to_xml(self, root_path, file_name):
        nsmap = {'xi': 'http://www.w3.org/2001/XInclude'}
        root = etree.Element('device', {'name': ' ', 'type': 'device_type'}, nsmap=nsmap)
        
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