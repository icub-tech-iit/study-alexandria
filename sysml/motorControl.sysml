import ScalarValues::*;

part motorControl : device {
    part LIMITS {
        attribute jntPosMin : Array {
            :>> dimensions default 2; 
            :>> elements : Integer[dimensions] default (-30, -20);
        }
        attribute jntPosMax : Array {
            :>> dimensions default 2;
            :>> elements : Integer[dimensions] default (30, 20);
        }
        attribute jntVelMax : Array {
            :>> dimensions default 2;
            :>> elements : Integer[dimensions] default (1000, 1000);
        }
        attribute motorOverloadCurrents : Array {
            :>> dimensions default 2;
            :>> elements : Integer[dimensions] default (5000, 5000);
        }
        attribute motorNominalCurrents : Array {
            :>> dimensions default 2;
            :>> elements : Integer[dimensions] default (1500, 1500);
        }
        attribute motorPeakCurrents : Array {
            :>> dimensions default 2;
            :>> elements : Integer[dimensions] default (3000, 3000);
        }
        attribute motorPwmLimit : Array {
            :>> dimensions default 2;
            :>> elements : Integer[dimensions] default (3360, 3360);
        }
    }
    part TIMEOUTS {
        attribute velocity : Array {
            :>> dimensions default 2;
            :>> elements : Integer[dimensions] default (100, 100);
        }
    }
    part IMPEDANCE {
        attribute stiffness : Array {
            :>> dimensions default 2;
            :>> elements : Real[dimensions] default (0.0, 0.0);
        }
        attribute damping : Array {
            :>> dimensions default 2;
            :>> elements : Real[dimensions] default (0.0, 0.0);
        }
    }
    part CONTROLS {
        attribute positionControl : Array {
            :>> dimensions default 2;
            :>> elements : String[dimensions] default ("POS_PID_DEFAULT", "POS_PID_DEFAULT");
        }
        attribute velocityControl : Array {
            :>> dimensions default 2;
            :>> elements : String[dimensions] default ("POS_PID_DEFAULT, POS_PID_DEFAULT");
        }
        attribute mixedControl : Array {
            :>> dimensions default 2;
            :>> elements : String[dimensions] default ("POS_PID_DEFAULT, POS_PID_DEFAULT");
        }
        attribute torqueControl : Array {
            :>> dimensions default 2;
            :>> elements : String[dimensions] default ("none", "none");
        }
        attribute currentPid : Array {
            :>> dimensions default 2;
            :>> elements : String[dimensions] default ("none", "none");
        }
        attribute speedPid : Array {
            :>> dimensions default 2;
            :>> elements : String[dimensions] default ("none", "none");
        }
    }
    part POS_PID_DEFAULT {
        attribute controlLaw : String default "minjerk";
        attribute outputType : String default "pwm";
        attribute fbkControlUnits : String default "metric_units";
        attribute outputControlUnits : String default "machine_units";
        attribute kp : Array {
            :>> dimensions default 2;
            :>> elements : Real[dimensions] default (-300, 300);
        }
        attribute kd : Array {
            :>> dimensions default 2;
            :>> elements : Integer[dimensions] default (0, 0);
        }
        attribute ki : Array {
            :>> dimensions default 2;
            :>> elements : Integer[dimensions] default (-100, +100);
        }
        attribute maxOutput : Array {
            :>> dimensions default 2;
            :>> elements : Integer[dimensions] default (3360,3360);
        }
        attribute maxInt : Array {
            :>> dimensions default 2;
            :>> elements : Integer[dimensions] default (3360, 3360);
        }
        attribute stictionUp : Array {
            :>> dimensions default 2;
            :>> elements : Integer[dimensions] default (0, 0);
        }
        attribute stictionDown : Array {
            :>> dimensions default 2;
            :>> elements : Integer[dimensions] default (0, 0);
        }
        attribute kff : Array {
            :>> dimensions default 2;
            :>> elements : Integer[dimensions] default (0, 0);
        }
    }
}