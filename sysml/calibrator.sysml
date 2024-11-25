import ScalarValues::*;
import VectorValues::*;
part calibrator : device {
    part GENERAL {
        attribute joints : Integer default 1;
        attribute deviceName : String default "foo";
    }
    part HOME {
        attribute positionHome : VectorValue;
        attribute velocityHome : VectorValue;
    }
    part CALIBRATION {
        attribute calibrationType : VectorValue;
        attribute calibration1 : VectorValue;
        attribute calibration2 : VectorValue;
        attribute calibration3 : VectorValue;
        attribute calibration4 : VectorValue;
        attribute calibration5 : VectorValue;
        attribute calibrationZero : VectorValue;
        attribute calibrationDelta : VectorValue;
    }
    attribute CALIB_ORDER : String;
    attribute phase : phase [3];
}