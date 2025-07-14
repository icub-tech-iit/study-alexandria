from dataclasses import dataclass, is_dataclass, fields
from lxml import etree
from device import Device
from utils import parse_sysml

class motorControl(Device):
    def __init__(self, root_path):
        device = Device.from_sysml(root_path)
        device_fields = {f.name for f in fields(Device)}
        init_args = {k: v for k, v in device.__dict__.items() if k in device_fields}

        super().__init__(**init_args)

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
        attr = dict(parse_sysml(root_path+'/templates/motorControl.sysml').part_definitions.items())
        mc = cls(root_path)

        def set_parameters(instance, attributes):
            for key, value in attributes.items():
                if key == 'motorControl':
                    mc.includes = [include for include in value.parameters['includes']['value'].strip('()').split(',')]
                    mc.folder_name = value.parameters['folder_name'].strip('"')
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
        root = super().to_xml(root_path, file_name)

        self.generate_xml(root, root_path, file_name)

        # etree.indent(root, space='    ')
        # doctype = '<!DOCTYPE params PUBLIC "-//YARP//DTD yarprobotinterface 3.0//EN" "http://www.yarp.it/DTD/yarprobotinterfaceV3.0.dtd">'
        # xml_object = etree.tostring(root, pretty_print=True, xml_declaration=True, encoding='UTF-8', doctype=doctype)
        # with open(root_path+'/'+file_name, "wb") as writer:
        #     writer.write(xml_object)
def main():
    pass

if __name__ == "__main__":
    main()