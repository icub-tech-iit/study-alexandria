import ScalarValues::*;

part calibrator : device {
    part GENERAL {
        attribute joints : Integer default 1;
        attribute deviceName : String default "foo";
    }
    part HOME {
        attribute positionHome : Array {
            :>> dimensions default 1;
            :>> elements : Integer[dimensions] default (0);
        }
        attribute velocityHome : Array {
            :>> dimensions default 1;
            :>> elements : Integer[dimensions] default (10);
        }
    }
    part CALIBRATION {
        attribute calibrationType : Array {
            :>> dimensions default 1;
            :>> elements : Integer[dimensions] default (10);
        }
        attribute calibration1 : Array {
            :>> dimensions default 1;
            :>> elements : Integer[dimensions] default (0);
        }
        attribute calibration2 : Array {
            :>> dimensions default 1;
            :>> elements : Integer[dimensions] default (0);
        }
        attribute calibration3 : Array {
            :>> dimensions default 1;
            :>> elements : Integer[dimensions] default (0);
        }
        attribute calibration4 : Array {
            :>> dimensions default 1;
            :>> elements : Integer[dimensions] default (0);
        }
        attribute calibration5 : Array {
            :>> dimensions default 1;
            :>> elements : Integer[dimensions] default (0);
        }
        attribute calibrationZero : Array {
            :>> dimensions default 1;
            :>> elements : Integer[dimensions] default (0);
        }
        attribute calibrationDelta : Array {
            :>> dimensions default 1;
            :>> elements : Integer[dimensions] default (0);
        }
    }
    attribute CALIB_ORDER : String default "(0)";
    attribute phase : phase [3];
}