from dataclasses import dataclass
import re
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

    @classmethod
    def from_sysml(cls, root_path, file_path):
        with open(root_path+file_path, 'r') as file:
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

        mec = cls()
        attr = extract_attributes(sysml_str, vector_pattern) | extract_attributes(sysml_str, general_pattern)
        mec.general = cls.GENERAL(
            MotioncontrolVersion = attr['MotioncontrolVersion'],
            Joints = attr['Joints'],
            AxisMap = [attr['AxisMap']],
            AxisName = [attr['AxisName']],
            AxisType = [attr['AxisType']],
            Encoder = [attr['Encoder']],
            fullscalePWM = [attr['fullscalePWM']],
            ampsToSensor = [attr['ampsToSensor']],
            Gearbox_M2J = [attr['Gearbox_M2J']],
            Gearbox_E2J = [attr['Gearbox_E2J']],
            useMotorSpeedFbk = [attr['useMotorSpeedFbk']],
            MotorType = [attr['MotorType']],
            Verbose = attr['Verbose']
        )

        mec.limits = cls.LIMITS(
            hardwareJntPosMin = [attr['hardwareJntPosMin']],
            hardwareJntPosMax = [attr['hardwareJntPosMax']],
            rotorPosMin = [attr['rotorPosMin']],
            rotorPosMax = [attr['rotorPosMax']]
        )

        mec.couplings = cls.COUPLINGS(
            matrixJ2M = [attr['matrixJ2M']],
            matrixM2J = [attr['matrixM2J']],
            matrixE2J = [attr['matrixE2J']]
        )

        mec.jointset_cfg = cls.JOINTSET_CFG(
            numberofsets = attr['numberofsets']
        )
        mec.jointset_0 = cls.JOINTSET_CFG(mec.jointset_cfg.numberofsets).JOINTSET_0(
            listofjoints = [attr['listofjoints']],
            constraintName = attr['constraintName'],
            param1 = attr['param1'],
            param2 = attr['param2']
        )

        return mec

def main():
    mec = Mechanicals.from_sysml('/home/mgloria/iit/study-alexandria/sysml','/mec.sysml')
    print(mec.jointset_0.constraintName)

if __name__ == "__main__":
    main()