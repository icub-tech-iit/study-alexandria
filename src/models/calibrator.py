import re
from dataclasses import dataclass
from phase import Phase
from device import Device

class Calibrator(Device):
    def __init__(self, level, type, target):
        super().__init__() 
        self.CALIB_ORDER = list[float]
        self.phase = list[Phase(level, type, target)]
    
    @dataclass
    class GENERAL:
        joints: int
        deviceName: str
    @dataclass
    class HOME:
        positionHome = str
        velocityHome = str

    @dataclass
    class CALIBRATION:
        calibrationType = list[float]
        calibration1 = list[float]
        calibration2 = list[float]
        calibration3 = list[float]
        calibration4 = list[float]
        calibration5 = list[float]
        calibrationZero = list[float]
        calibrationDelta = list[float]

    @classmethod
    def from_sysml(cls, sysml_str):
        def extract_attributes(block, pattern):
            matches = re.findall(pattern, block)
            return {k: eval(v) if v.isdigit() or '.' in v else v.strip('"') for k, v in matches}

        general_pattern = r'attribute (\w+) : \w+ = (\w+);'
        vector_pattern = r'attribute (\w+) : VectorValue = \[(.+?)\];'
        calib_order_pattern = r'attribute CALIB_ORDER : String = (\w+);'
        phase_pattern = r'attribute phase : phase \[\d+\]  = (\w+);'

        instance = cls(None, None, None)
        general_block = re.search(r'part GENERAL {([^}]*)}', sysml_str)
        home_block = re.search(r'part HOME {([^}]*)}', sysml_str)   
        calibration_block = re.search(r'part CALIBRATION {([^}]*)}', sysml_str)

        if general_block:
            general_attrs = extract_attributes(general_block.group(1), general_pattern)
            instance.general = cls.GENERAL(
                joints=int(general_attrs['joints']),
                deviceName=str(general_attrs['deviceName'])
            )
        if home_block:
            home_attrs = extract_attributes(home_block.group(1), vector_pattern)
            instance.home = cls.HOME(
                positionHome=[float(x) for x in home_attrs['positionHome']],
                velocityHome=[float(x) for x in home_attrs['velocityHome']]
            )
            print(home_attrs['positionHome'])
        if calibration_block:
            calib_attrs = extract_attributes(calibration_block.group(1), vector_pattern)
            instance.calibration = cls.CALIBRATION(
                calibrationType=[float(x) for x in calib_attrs['calibrationType']],
                calibration1=[float(x) for x in calib_attrs['calibration1']],
                calibration2=[float(x) for x in calib_attrs['calibration2']],
                calibration3=[float(x) for x in calib_attrs['calibration3']],
                calibration4=[float(x) for x in calib_attrs['calibration4']],
                calibration5=[float(x) for x in calib_attrs['calibration5']],
                calibrationZero=[float(x) for x in calib_attrs['calibrationZero']],
                calibrationDelta=[float(x) for x in calib_attrs['calibrationDelta']],
            )

        # calib_order_match = re.search(calib_order_pattern, sysml_str)
        # if calib_order_match:
        #     instance.CALIB_ORDER = calib_order_match.group(1).split()

        phase_match = re.search(phase_pattern, sysml_str)
        if phase_match:
            instance.phase = Phase()

        return instance

def main():
    sysml_str = '''
    part GENERAL {
        attribute joints : Integer = 6;
        attribute deviceName : String = pippo;
    }
    part HOME {
        attribute positionHome : VectorValue = [1.0, 2.0, 3.0, 4.0, 5.0];
        attribute velocityHome : VectorValue = [1.0, 2.0, 3.0, 4.0, 5.0];
    }
    part CALIBRATION {
        attribute calibrationType : VectorValue = [1.0, 2.0, 3.0, 4.0, 5.0];
        attribute calibration1 : VectorValue = [1.0, 2.0, 3.0, 4.0, 5.0];
        attribute calibration2 : VectorValue = [1.0, 2.0, 3.0, 4.0, 5.0];
        attribute calibration3 : VectorValue = [1.0, 2.0, 3.0, 4.0, 5.0];
        attribute calibration4 : VectorValue = [1.0, 2.0, 3.0, 4.0, 5.0];
        attribute calibration5 : VectorValue = [1.0, 2.0, 3.0, 4.0, 5.0];
        attribute calibrationZero : VectorValue = [1.0, 2.0, 3.0, 4.0, 5.0];
        attribute calibrationZero : VectorValue = [1.0, 2.0, 3.0, 4.0, 5.0];
        attribute calibrationDelta : VectorValue = [1.0, 2.0, 3.0, 4.0, 5.0];
    }
    attribute CALIB_ORDER : String;
    attribute phase : phase [1];
    '''

    calibrator = Calibrator.from_sysml(sysml_str)
    print(calibrator)

if __name__ == "__main__":
    main()