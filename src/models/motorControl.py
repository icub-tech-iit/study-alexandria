from dataclasses import dataclass, is_dataclass, asdict, fields
from lxml import etree
from device import Device
import re

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

    @classmethod
    def from_sysml(cls, root_path):
        with open(root_path+'/motorControl.sysml', 'r') as file:
            sysml_str = file.read()

        def extract_attributes(block, pattern):
            matches = re.findall(pattern, block)
            attributes = {}
            for match in matches:
                key = match[0]
                value = None
                if match[1]:
                    try:
                        value = float(match[1])
                    except ValueError:
                        value = match[1]
                elif match[2]:
                    value = int(match[2])
                else:
                    value = match[3]
                attributes[key] = value
            return attributes
        
        general_pattern = r'attribute (\w+) : \w+ default (?:(\d+(\.\d*)?)|"([^"]*)");' #catch integer/float with sign or quoted string
        vector_pattern = r'attribute (\w+) :\s*\w+\s*{\s*:\s*>>\s*dimensions\s*default\s*\d+;\s*:\s*>>\s*elements\s*:\s*\w+\[\w+\]\s*default\s*\(([^)]+)\);'
        mc = cls(root_path)

        attr = extract_attributes(sysml_str, vector_pattern) | extract_attributes(sysml_str, general_pattern)
        mc.limits = cls.LIMITS(
            jntPosMin = [attr['jntPosMin']],
            jntPosMax = [attr['jntPosMax']],
            jntVelMax = [attr['jntVelMax']],
            motorOverloadCurrents = [attr['motorOverloadCurrents']],
            motorNominalCurrents = [attr['motorNominalCurrents']],
            motorPeakCurrents = [attr['motorPeakCurrents']],
            motorPwmLimit = [attr['motorPwmLimit']]
        )
        mc.timeouts = cls.TIMEOUTS(
            velocity = [attr['velocity']]
        )
        mc.impedance = cls.IMPEDANCE(
            stiffness = [attr['stiffness']],
            damping = [attr['damping']]
        )
        mc.controls = cls.CONTROLS(
            positionControl = [attr['positionControl']],
            velocityControl = [attr['velocityControl']],
            mixedControl = [attr['mixedControl']],
            torqueControl = [attr['torqueControl']],
            currentPid = [attr['currentPid']],
            speedPid = [attr['speedPid']]
        )
        mc.pos_pid = cls.POS_PID_DEFAULT(
            controlLaw = attr['controlLaw'],
            outputType = attr['outputType'],
            fbkControlUnits = attr['fbkControlUnits'],
            outputControlUnits = attr['outputControlUnits'],
            kp = [attr['kp']],
            kd = [attr['kd']],
            ki = [attr['ki']],
            maxOutput = [attr['maxOutput']],
            maxInt = [attr['maxInt']],
            stictionUp = [attr['stictionUp']],
            stictionDown = [attr['stictionDown']],
            kff = [attr['kff']]
        )
        return mc
    
    def to_xml(self, root_path):
        nsmap = {'xi': 'http://www.w3.org/2001/XInclude'}
        root = etree.Element('device', {'name': ' ', 'type': 'device_type'}, nsmap=nsmap)
        
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
            if is_dataclass(attr_value):
                _dataclass_to_xml(root, attr_name, attr_value)

        etree.indent(root, space='    ')
        doctype = '<!DOCTYPE params PUBLIC "-//YARP//DTD yarprobotinterface 3.0//EN" "http://www.yarp.it/DTD/yarprobotinterfaceV3.0.dtd">'
        xml_object = etree.tostring(root, pretty_print=True, xml_declaration=True, encoding='UTF-8', doctype=doctype)
        with open(root_path + 'motorControl.xml', "wb") as writer:
            writer.write(xml_object)
def main():
    motor_control = motorControl.from_sysml('/home/mgloria/iit/study-alexandria/sysml')
    print(motor_control.controls.positionControl)
    motor_control.to_xml('/home/mgloria/iit/study-alexandria/sysml/')

if __name__ == "__main__":
    main()