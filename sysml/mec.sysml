import ScalarValues::*;
import VectorValues::*;
part GENERAL {
	attribute MotioncontrolVersion : Integer;
	attribute Joints : Integer;
	attribute AxisMap : VectorValue;
	attribute AxisName : VectorValue;
	attribute AxisType : VectorValue;
	attribute Encoder : VectorValue;
	attribute fullscalePWM : VectorValue;
	attribute ampsToSensor : VectorValue;
	attribute Gearbox_M2J : VectorValue;
	attribute Gearbox_E2J : VectorValue;
	attribute useMotorSpeedFbk : VectorValue;
	attribute MotorType : VectorValue;
	attribute Verbose : Integer;
}
part LIMITS {
	attribute hardwareJntPosMin : VectorValue;
	attribute hardwareJntPosMax : VectorValue;
	attribute rotorPosMin : VectorValue;
	attribute rotorPosMax : VectorValue;
}
part COUPLINGS {
	attribute matrixJ2M : VectorValue;
	attribute matrixM2J : VectorValue;
	attribute matrixE2J : VectorValue;
}
part JOINTSET_CFG {
	attribute numberofsets : Integer;
	part JOINTSET [2] {
		attribute listofjoints : VectorValue;
		attribute constraintName : String;
		attribute param1 : Integer;
		attribute param2 : Integer;
	}
}