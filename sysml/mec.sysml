import ScalarValues::*;
part mechanicals {
	part GENERAL {
		attribute MotioncontrolVersion : Integer default 6;
		attribute Joints : Integer default 2;
		attribute AxisMap : Array {
			:>> dimensions default 2; 
			:>> elements : Integer[dimensions] default (0, 1); 
		}
		attribute AxisName : Array {
			:>> dimensions default 2; 
			:>> elements : String[dimensions] default ("axis1", "axis2"); 
		}
		attribute AxisType : Array {
			:>> dimensions default 1; 
			:>> elements : String[dimensions] default ("revolute", "revolute"); 
		}
		attribute Encoder : Array {
			:>> dimensions default 2; 
			:>> elements : Real[dimensions] default (0.0, 0.0); 
		}
		attribute fullscalePWM : Array {
			:>> dimensions default 2; 
			:>> elements : Integer[dimensions] default (0, 0); 
		}
		attribute ampsToSensor : Array {
			:>> dimensions default 2; 
			:>> elements : Real[dimensions] default (0.0, 0.0); 
		}
		attribute Gearbox_M2J : Array {
			:>> dimensions default 2; 
			:>> elements : Real[dimensions] default (0.0, 0.0); 
		}
		attribute Gearbox_E2J : Array {
			:>> dimensions default 2; 
			:>> elements : Integer[dimensions] default (1, 1); 
		}
		attribute useMotorSpeedFbk : Array {
			:>> dimensions default 2; 
			:>> elements : Integer[dimensions] default (1, 1); 
		}
		attribute MotorType : Array {
			:>> dimensions default 2; 
			:>> elements : String[dimensions] default ("DC", "DC"); 
		}
		attribute Verbose : Integer default 0;
	}
	part LIMITS {
		attribute hardwareJntPosMin : Array	{
			:>> dimensions default 2; 
			:>> elements : Integer[dimensions] default (-30, -30); 
		}
		attribute hardwareJntPosMax : Array	{
			:>> dimensions default 2; 
			:>> elements : Integer[dimensions] default (30, 30); 
		}
		attribute rotorPosMin : Array {
			:>> dimensions default 2; 
			:>> elements : Integer[dimensions] default (0, 0); 
		}
		attribute rotorPosMax : Array {
			:>> dimensions default 2; 
			:>> elements : Integer[dimensions] default (0, 0); 
		}
	}
	part _2FOC {
		attribute HasHallSensor : Array {
			:>> dimensions default 2; 
			:>> elements : Integer[dimensions] default (0, 0); 
		}
		attribute HasTempSensor : Array {
			:>> dimensions default 2; 
			:>> elements : Integer[dimensions] default (0, 0); 
		}
		attribute HasRotorEncoder : Array {
			:>> dimensions default 2; 
			:>> elements : Integer[dimensions] default (0, 0); 
		}
		attribute HasRotorEncoderIndex : Array {
			:>> dimensions default 2; 
			:>> elements : Integer[dimensions] default (0, 0); 
		}
		attribute HasSpeedEncoder : Array {
			:>> dimensions default 2; 
			:>> elements : Integer[dimensions] default (0, 0); 
		}
		attribute RotorIndexOffset : Array {
			:>> dimensions default 2; 
			:>> elements : Integer[dimensions] default (0, 0); 
		}
		attribute MotorPoles : Array {
			:>> dimensions default 2; 
			:>> elements : Integer[dimensions] default (0, 0); 
		}
	}
	part COUPLINGS {
		attribute matrixJ2M : Array {
			:>> dimensions default 3; 
			:>> elements : Real[dimensions] default (0.000, 0.000, 0.000, 0.000, 
			0.000, 0.000, 0.000, 0.000,
			0.000, 0.000, 0.000, 0.000,
			0.000, 0.000, 0.000, 0.000); 
		}
		attribute matrixM2J : Array {
			:>> dimensions default 3; 
			:>> elements : Real[dimensions] default (0.000, 0.000, 0.000, 0.000, 
			0.000, 0.000, 0.000, 0.000,
			0.000, 0.000, 0.000, 0.000,
			0.000, 0.000, 0.000, 0.000); 
		}
		attribute matrixE2J : Array {
			:>> dimensions default 3; 
			:>> elements : Real[dimensions] default (1.000, 0.000, 0.000, 0.000, 0.000, 0.000, 
			0.000, 1.000, 0.000, 0.000, 0.000, 0.000,
			0.000, 0.000, 1.000, 0.000, 0.000, 0.000,
			0.000, 0.000, 0.000, 1.000, 0.000, 0.000); 
		}
	}
	part JOINTSET_CFG {
		attribute numberofsets : Integer default 1;
		part JOINTSET_0 {
			attribute listofjoints : Array {
				:>> dimensions default 2; 
				:>> elements : Integer[dimensions] default (0, 1); 
			}
			attribute constraintName : String default "none";
			attribute param1 : Integer default 0;
			attribute param2 : Integer default 0;
		}
		part JOINTSET_1 {
			attribute listofjoints : Array {
				:>> dimensions default 2; 
				:>> elements : Integer[dimensions] default (0, 1); 
			}
			attribute constraintName : String default "none";
			attribute param1 : Integer default 0;
			attribute param2 : Integer default 0;
		}
		part JOINTSET_2 {
			attribute listofjoints : Array {
				:>> dimensions default 2; 
				:>> elements : Integer[dimensions] default (0, 1); 
			}
			attribute constraintName : String default "none";
			attribute param1 : Integer default 0;
			attribute param2 : Integer default 0;
		}
	}
}