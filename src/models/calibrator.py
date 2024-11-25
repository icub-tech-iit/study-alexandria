import re
import os
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
            print(matches)
            return {k: eval(v) if v.isdigit() or '.' in v else v.strip('"') for k, v in matches}
        
        general_pattern = r'attribute (\w+) : \w+ default (\w+);'
        vector_pattern = r'attribute (\w+) : VectorValue default \[(.+?)\];'
        calib_order_pattern = r'attribute CALIB_ORDER : String default (\w+);'
        phase_pattern = r'attribute phase : phase \[\d+\];'

        calib = cls(None, None, None)
        general_block = re.search(r'part GENERAL {([^}]*)}', sysml_str)
        home_block = re.search(r'part HOME {([^}]*)}', sysml_str)   
        calibration_block = re.search(r'part CALIBRATION {([^}]*)}', sysml_str)
        calib_order_match = re.search(calib_order_pattern, sysml_str)
        phase_match = re.search(phase_pattern, sysml_str)

        if general_block:
            general_attrs = extract_attributes(general_block.group(1), general_pattern)
            calib.general = cls.GENERAL(
                joints = int(general_attrs['joints']),
                deviceName = str(general_attrs['deviceName'])
                # deviceName = super().from_sysml('/home/mgloria/iit/study-alexandria/sysml/device.sysml')
            )
        if home_block:
            home_attrs = extract_attributes(home_block.group(1), vector_pattern)
            calib.home = cls.HOME(
                positionHome=[float(x) for x in home_attrs['positionHome']],
                velocityHome=[float(x) for x in home_attrs['velocityHome']]
            )
        if calibration_block:
            calib_attrs = extract_attributes(calibration_block.group(1), vector_pattern)
            calib.calibration = cls.CALIBRATION(
                calibrationType=[float(x) for x in calib_attrs['calibrationType']],
                calibration1=[float(x) for x in calib_attrs['calibration1']],
                calibration2=[float(x) for x in calib_attrs['calibration2']],
                calibration3=[float(x) for x in calib_attrs['calibration3']],
                calibration4=[float(x) for x in calib_attrs['calibration4']],
                calibration5=[float(x) for x in calib_attrs['calibration5']],
                calibrationZero=[float(x) for x in calib_attrs['calibrationZero']],
                calibrationDelta=[float(x) for x in calib_attrs['calibrationDelta']],
            )
        if calib_order_match:
            calib.CALIB_ORDER = calib_order_match.group(1).split()
        if phase_match:
            calib.phase = Phase(cls.level, cls.type, cls.target)

        return calib

def main():
    calibrator = Calibrator.from_sysml('/home/mgloria/iit/study-alexandria/sysml/calibrator.sysml')
    print(calibrator)

if __name__ == "__main__":
    main()