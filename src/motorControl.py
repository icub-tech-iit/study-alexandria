from dataclasses import dataclass, fields
from device import Device

class MotorControl(Device):
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
        return super().from_sysml(root_path)
    
    def to_xml(self, root_path, file_name):
        root = super().to_xml(root_path, file_name)

        self.generate_xml(root, root_path, file_name)

def main():
    pass

if __name__ == "__main__":
    main()