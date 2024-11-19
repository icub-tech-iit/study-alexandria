import ScalarValues::*;
import VectorValues::*;
part motorControl : device {
    part LIMITS {
        attribute jntPosMin : VectorValue;
        attribute jntPosMax : VectorValue;
        attribute jntVelMax : VectorValue;
        attribute motorOverloadCurrents : VectorValue;
        attribute motorNominalCurrents : VectorValue;
        attribute motorPeakCurrents : VectorValue;
        attribute MotorPwmLimit : VectorValue;
    }
    part TIMEOUTS {
        attribute velocity : VectorValue;
    }
    part IMPEDANCE {
        attribute stiffness : VectorValue;
        attribute damping : VectorValue;
    }
    part CONTROL {
        attribute positionControl : VectorValue;
        attribute velocityControl : VectorValue;
        attribute mixedControl : VectorValue;
        attribute torqueControl : VectorValue;
        attribute currentPid : VectorValue;
        attribute speedPid : VectorValue;
    }
    part POS_PID_DEFAULT {
        attribute controlLaw : String = "minjerk";
        attribute outputType : String = "pwm";
        attribute fbkControlUnits : String = "metric_units";
        attribute outputControlUnits : String = "machine_units";
        attribute kp : VectorValue;
        attribute kd : VectorValue;
        attribute ki : VectorValue;
        attribute maxOutput : VectorValue;
        attribute maxInt : VectorValue;
        attribute stictionUp : VectorValue;
        attribute stictionDown : VectorValue;
        attribute kff : VectorValue;
    }
}