from dataclasses import dataclass
from device import Device
import re

class motorControl(Device):
    def __init__(self):
        super().__init__(None, None)

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
    def from_sysml(cls, file_path):
        with open(file_path, 'r') as file:
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
        mc = cls()

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

def main():
    motor_control = motorControl.from_sysml('/home/mgloria/iit/study-alexandria/sysml/motorControl.sysml')
    print(motor_control.controls.positionControl)

if __name__ == "__main__":
    main()