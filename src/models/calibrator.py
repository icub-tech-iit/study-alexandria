import re
from dataclasses import dataclass
from phase import Phase
from device import Device

class Calibrator(Device):
    def __init__(self, level, type, target):
        super().__init__(None, None)
        self.CALIB_ORDER = list[float]
        self.phase = list[Phase(level, type, target)]
    
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
        phase_pattern = r'attribute (\w+) : \w+ (\[\d+\]);'

        calib = cls(None, None, None)
        device = Device(None, None).from_sysml('/home/mgloria/iit/study-alexandria/sysml/device.sysml')
        attr = extract_attributes(sysml_str, vector_pattern) | extract_attributes(sysml_str, general_pattern) | extract_attributes(sysml_str, phase_pattern)

        calib.general = cls.GENERAL(
            joints = attr['joints'],
            deviceName = device.name
        )

        calib.home = cls.HOME(
            positionHome = [attr['positionHome']],
            velocityHome = [attr['velocityHome']]
        )

        calib.calibration = cls.CALIBRATION(
            calibrationType = [attr['calibrationType']],
            calibration1 = [attr['calibration1']],
            calibration2 = [attr['calibration2']],
            calibration3 = [attr['calibration3']],
            calibration4 = [attr['calibration4']],
            calibration5 = [attr['calibration5']],
            calibrationZero = [attr['calibrationZero']],
            calibrationDelta = [attr['calibrationDelta']],
        )

        calib.CALIB_ORDER = attr['CALIB_ORDER']
        calib.phase = [Phase.from_sysml('/home/mgloria/iit/study-alexandria/sysml/phase.sysml') for i in attr['phase']]

        return calib

def main():
    calibrator = Calibrator.from_sysml('/home/mgloria/iit/study-alexandria/sysml/calibrator.sysml')
    print(calibrator.general.deviceName)

if __name__ == "__main__":
    main()