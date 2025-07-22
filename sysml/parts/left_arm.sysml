part def LeftArm {
    part left_arm_calib :> calibrator {
        :>> device_type = "parametricCalibratorEth";
        :>> device_name = "left_arm-calibrator";
        :>> GENERAL.joints = 16;
        :>> GENERAL.deviceName = "Left_Arm_Calibrator";
        :>> HOME.positionHome = (-30, 30, 0, 45, 0, 0, 0, 35, 65, 0, 0, 0, 0, 0, 0, 0);
        :>> HOME.velocityHome = (10, 10, 10, 10, 30, 30, 30, 60, 30, 30, 30, 30, 30, 30, 30, 30);
        :>> CALIBRATION.calibrationType = (12, 12, 12, 12, 5, 12, 12, 7, 7, 6, 6, 6, 6, 6, 6, 6);
        :>> CALIB_ORDER = "(0 1 2 3) (4) (5 6 7) (8 9 11 13) (10 12 14 15)";
        :>> startup.phase = "startup";
        :>> startup.type = "calibrate";
        :>> startup.target = "left_arm-mc_remapper";
        :>> interrupt1.phase = "interrupt1";
        :>> interrupt1.level = 1;
        :>> interrupt1.type = "park";
        :>> interrupt1.target = "left_arm-mc_remapper";
        :>> interrupt3.phase = "interrupt3";
        :>> interrupt3.level = 1;
        :>> interrupt3.type = "abort";
    }
    part left_arm_eb1_j0_3_eln :> electronics {
        :>> ETH_BOARD.ETH_BOARD_PROPERTIES.IpAddress = "10.0.1.1";
        :>> ETH_BOARD.ETH_BOARD_PROPERTIES.Type = "ems4";
        :>> ETH_BOARD.ETH_BOARD_SETTINGS.Name = "left_arm-eb1-j0_3";
        :>> ETH_BOARD.ETH_BOARD_SETTINGS.RUNNINGMODE.TXrateOfRegularROPs = 5;
    }
    part left_arm_eb24_j4_7_eln :> electronics {
        :>> ETH_BOARD.ETH_BOARD_PROPERTIES.IpAddress = "10.0.1.24";
        :>> ETH_BOARD.ETH_BOARD_PROPERTIES.Type = "mc4plus";
        :>> ETH_BOARD.ETH_BOARD_SETTINGS.Name = "left_arm-eb24-j4_7";
    }
    part left_arm_eb25_j8_11_eln :> electronics {
        :>> ETH_BOARD.ETH_BOARD_PROPERTIES.IpAddress = "10.0.1.25";
        :>> ETH_BOARD.ETH_BOARD_PROPERTIES.Type = "mc4plus";
        :>> ETH_BOARD.ETH_BOARD_SETTINGS.Name = "left_arm-eb25-j8_11";
        :>> ETH_BOARD.ETH_BOARD_SETTINGS.RUNNINGMODE.TXrateOfRegularROPs = 5;
    }
    part left_arm_eb26_j12_15_eln :> electronics {
        :>> ETH_BOARD.ETH_BOARD_PROPERTIES.IpAddress = "10.0.1.26";
        :>> ETH_BOARD.ETH_BOARD_PROPERTIES.Type = "mc4plus";
        :>> ETH_BOARD.ETH_BOARD_SETTINGS.Name = "left_arm-eb26-j12_15";
        :>> ETH_BOARD.ETH_BOARD_SETTINGS.RUNNINGMODE.TXrateOfRegularROPs = 5;
    }
    part left_arm_eb1_j0_3_mec :> mechanicals {
        :>> GENERAL.Joints = 4;
        :>> GENERAL.AxisMap = (0, 1, 2, 3);
        :>> GENERAL.AxisName = ("l_shoulder_pitch", "l_shoulder_roll", "l_shoulder_yaw", "l_elbow");
        :>> GENERAL.AxisType = ("revolute", "revolute", "revolute", "revolute");
        :>> GENERAL.Encoder = (182.044, 182.044, 182.044, 182.044);
        :>> GENERAL.fullscalePWM = (32000, 32000, 32000, 32000);
        :>> GENERAL.ampsToSensor = (1000.0, 1000.0, 1000.0, 1000.0);
        :>> GENERAL.Gearbox_M2J = (100.0, 100.0, 100.0, 100.0);
        :>> GENERAL.Gearbox_E2J = (1, 1, 1, 1);
        :>> GENERAL.useMotorSpeedFbk = (1, 1, 1, 1);
        :>> GENERAL.MotorType = ("BLL_MOOG", "BLL_MOOG", "BLL_MOOG", "BLL_MOOG");
        :>> LIMITS.hardwareJntPosMin = (-95.5, 0, -32, 15);
        :>> LIMITS.hardwareJntPosMax = (8, 160, 80, 106); 
        :>> LIMITS.rotorPosMin = (0, 0, 0, 0);
        :>> LIMITS.rotorPosMax = (0, 0, 0, 0);
        :>> _2FOC.HasHallSensor = (1, 1, 1, 1);
        :>> _2FOC.HasTempSensor = (0, 0, 0, 0);
        :>> _2FOC.HasRotorEncoder = (1, 1, 1, 1);
        :>> _2FOC.HasRotorEncoderIndex = (0, 0, 0, 0);
        :>> _2FOC.HasSpeedEncoder = (0, 0, 0, 0);
        :>> _2FOC.RotorIndexOffset = (0, 0, 0, 0);
        :>> _2FOC.MotorPoles = (8, 8, 8, 8);
        :>> COUPLINGS.matrixJ2M = (1.000, 0.000, 0.000, 0.000,
        -1.625, 1.625, 0.000, 0.000,
        0.000, 0.000, 1.625, 0.000,
        0.000, 0.000, 0.000, 1.000);
        :>> COUPLINGS.matrixM2J = (1.000, 0.000, 0.000, 0.000,
        1.000, 0.615, 0.000, 0.000,
        0.000, -0.615, 0.615, 0.000,
        0.000, 0.000, 0.000, 1.000);
        :>> JOINTSET_CFG.numberofsets = 2;
        :>> JOINTSET_CFG.JOINTSET_0.listofjoints = (0, 1, 2);
        :>> JOINTSET_CFG.JOINTSET_1.listofjoints = (3);
    }
    part left_arm_eb24_j4_7_mec :> mechanicals {
        :>> GENERAL.Joints = 4;
        :>> GENERAL.AxisMap = (0, 1, 2, 3);
        :>> GENERAL.AxisName = ("l_wrist_prosup", "l_wrist_pitch", "l_wrist_yaw", "l_hand_finger");
        :>> GENERAL.AxisType = ("revolute", "revolute", "revolute", "revolute");
        :>> GENERAL.Encoder = (182.044, 182.044, 182.044, 182.044);
        :>> GENERAL.fullscalePWM = (3360, 3360, 3360, 3360);
        :>> GENERAL.ampsToSensor = (1000.0, 1000.0, 1000.0, 1000.0);
        :>> GENERAL.Gearbox_M2J = (-100.0, 159.0, 159.0, 256.0);
        :>> GENERAL.Gearbox_E2J = (1, 1, 1, 1);
        :>> GENERAL.useMotorSpeedFbk = (1, 1, 1, 1);
        :>> GENERAL.MotorType = ("DC", "DC", "DC", "DC");
        :>> LIMITS.hardwareJntPosMin = (-90, -80, -15, 10);
        :>> LIMITS.hardwareJntPosMax = (90, 30, 35, 60); 
        :>> LIMITS.rotorPosMin = (0, 0, 0, 0);
        :>> LIMITS.rotorPosMax = (0, 0, 0, 0);
        :>> _2FOC.HasHallSensor = (1, 1, 1, 1);
        :>> _2FOC.HasTempSensor = (0, 0, 0, 0);
        :>> _2FOC.HasRotorEncoder = (1, 1, 1, 1);
        :>> _2FOC.HasRotorEncoderIndex = (0, 0, 0, 0);
        :>> _2FOC.HasSpeedEncoder = (0, 0, 0, 0);
        :>> _2FOC.RotorIndexOffset = (0, 0, 0, 0);
        :>> _2FOC.MotorPoles = (8, 8, 8, 8);
        :>> COUPLINGS.matrixJ2M = (1.000, 0.000, 0.000, 0.000,
        0.000, 1.000, 0.000, 0.000,
        0.000, -1.000, 1.000, 0.000,
        0.000, 0.000, 0.000, 1.000);
        :>> COUPLINGS.matrixM2J = (1.000, 0.000, 0.000, 0.000,
        0.000, 1.000, 1.000, 0.000,
        0.000, 0.000, 1.000, 0.000,
        0.000, 0.000, 0.000, 1.000);
        :>> JOINTSET_CFG.numberofsets = 3;
        :>> JOINTSET_CFG.JOINTSET_0.listofjoints = (0);
        :>> JOINTSET_CFG.JOINTSET_1.listofjoints = (1, 2);
        :>> JOINTSET_CFG.JOINTSET_2.listofjoints = (3);
    }
    part left_arm_eb25_j8_11_mec :> mechanicals {
        :>> GENERAL.Joints = 4;
        :>> GENERAL.AxisMap = (0, 1, 2, 3);
        :>> GENERAL.AxisName = ("l_thumb_oppose", "l_thumb_proximal", "l_thumb_distal", "l_index_proximal");
        :>> GENERAL.AxisType = ("revolute", "revolute", "revolute", "revolute");
        :>> GENERAL.Encoder = (182.044, 182.044, 182.044, 182.044);
        :>> GENERAL.fullscalePWM = (3360, 3360, 3360, 3360);
        :>> GENERAL.ampsToSensor = (1000.0, 1000.0, 1000.0, 1000.0);
        :>> GENERAL.Gearbox_M2J = (256, 256, 256, 256);
        :>> GENERAL.Gearbox_E2J = (1, 1, 1, 1);
        :>> GENERAL.useMotorSpeedFbk = (1, 1, 1, 1);
        :>> GENERAL.MotorType = ("DC", "DC", "DC", "DC");
        :>> LIMITS.hardwareJntPosMin = (10, 0, 0, 0);
        :>> LIMITS.hardwareJntPosMax = (90, 90, 180, 90); 
        :>> LIMITS.rotorPosMin = (0, 0, -70000, -5120);
        :>> LIMITS.rotorPosMax = (0, 0, 5120, 32000);
        :>> _2FOC.HasHallSensor = (1, 1, 1, 1);
        :>> _2FOC.HasTempSensor = (0, 0, 0, 0);
        :>> _2FOC.HasRotorEncoder = (1, 1, 1, 1);
        :>> _2FOC.HasRotorEncoderIndex = (0, 0, 0, 0);
        :>> _2FOC.HasSpeedEncoder = (0, 0, 0, 0);
        :>> _2FOC.RotorIndexOffset = (0, 0, 0, 0);
        :>> _2FOC.MotorPoles = (8, 8, 8, 8);
        :>> COUPLINGS.matrixJ2M = (1.000, 0.000, 0.000, 0.000,
        -1.000, 1.000, 0.000, 0.000,
        0.000, 0.000, 1.000, 0.000,
        0.000, 0.000, 0.000, 1.000);
        :>> COUPLINGS.matrixM2J = (1.000, 0.000, 0.000, 0.000,
        1.000, 1.000, 0.000, 0.000,
        0.000, 0.000, 1.000, 0.000,
        0.000, 0.000, 0.000, 1.000);
        :>> JOINTSET_CFG.numberofsets = 3;
        :>> JOINTSET_CFG.JOINTSET_0.listofjoints = (0, 1);
        :>> JOINTSET_CFG.JOINTSET_1.listofjoints = (2);
        :>> JOINTSET_CFG.JOINTSET_2.listofjoints = (3);
    }
    part left_arm_eb26_j12_15_mec :> mechanicals {
        :>> GENERAL.Joints = 4;
        :>> GENERAL.AxisMap = (0, 1, 2, 3);
        :>> GENERAL.AxisName = ("l_index_distal", "l_middle_proximal", "l_middle_distal", "l_pinky");
        :>> GENERAL.AxisType = ("revolute", "revolute", "revolute", "revolute");
        :>> GENERAL.Encoder = (182.044, 182.044, 182.044, 182.044);
        :>> GENERAL.fullscalePWM = (3360, 3360, 3360, 3360);
        :>> GENERAL.ampsToSensor = (1000.0, 1000.0, 1000.0, 1000.0);
        :>> GENERAL.Gearbox_M2J = (256, 256, 256, 256);
        :>> GENERAL.Gearbox_E2J = (1, 1, 1, 1);
        :>> GENERAL.useMotorSpeedFbk = (1, 1, 1, 1);
        :>> GENERAL.MotorType = ("DC", "DC", "DC", "DC");
        :>> LIMITS.hardwareJntPosMin = (0, 0, 0, 0);
        :>> LIMITS.hardwareJntPosMax = (180, 90, 180, 270); 
        :>> LIMITS.rotorPosMin = (-5120, -5120, -65000, -5120);
        :>> LIMITS.rotorPosMax = (65000, 32000, 5120, 65000);
        :>> _2FOC.HasHallSensor = (1, 1, 1, 1);
        :>> _2FOC.HasTempSensor = (0, 0, 0, 0);
        :>> _2FOC.HasRotorEncoder = (1, 1, 1, 1);
        :>> _2FOC.HasRotorEncoderIndex = (0, 0, 0, 0);
        :>> _2FOC.HasSpeedEncoder = (0, 0, 0, 0);
        :>> _2FOC.RotorIndexOffset = (0, 0, 0, 0);
        :>> _2FOC.MotorPoles = (8, 8, 8, 8);
        :>> COUPLINGS.matrixJ2M = (1.000, 0.000, 0.000, 0.000,
        0.000, 1.000, 0.000, 0.000,
        0.000, 0.000, 1.000, 0.000,
        0.000, 0.000, 0.000, 1.000);
        :>> COUPLINGS.matrixM2J = (1.000, 0.000, 0.000, 0.000,
        1.000, 1.000, 0.000, 0.000,
        0.000, 0.000, 1.000, 0.000,
        0.000, 0.000, 0.000, 1.000);
        :>> JOINTSET_CFG.numberofsets = 4;
        :>> JOINTSET_CFG.JOINTSET_0.listofjoints = (0);
        :>> JOINTSET_CFG.JOINTSET_1.listofjoints = (1);
        :>> JOINTSET_CFG.JOINTSET_2.listofjoints = (2);
        :>> JOINTSET_CFG.JOINTSET_3.listofjoints = (3);
    }
    part left_arm_eb1_j0_3_mc :> motorControl {
        :>> includes = ("../../general.xml", "../../hardware/electronics/left_arm_eb1_j0_3_eln.xml", "../../hardware/mechanicals/left_arm_eb1_j0_3_mec.xml", "./left_arm_eb1_j0_3_mc_service.xml");
        :>> device_type = "embObjMotionControl";
        :>> device_name = "left_arm-eb1-j0_3-mc";
        :>> LIMITS.jntPosMin = (-95.5, 0, -32, 15);
        :>> LIMITS.jntPosMax = (8, 160, 80, 106);
        :>> LIMITS.jntVelMax = (1000, 1000, 1000, 1000);
        :>> LIMITS.motorOverloadCurrents = (15000, 15000, 15000, 15000);
        :>> LIMITS.motorNominalCurrents = (4500, 4500, 4500, 4000);
        :>> LIMITS.motorPeakCurrents = (5500, 5500, 5500, 5000);
        :>> LIMITS.motorPwmLimit = (10000, 10000, 10000, 10000);
        :>> TIMEOUTS.velocity = (100, 100, 100, 100);
        :>> IMPEDANCE.stiffness = (0.1, 0.1, 0.1, 0.1);
        :>> IMPEDANCE.damping = (0.05, 0.05, 0.05, 0.05);
        :>> CONTROLS.positionControl = ("POS_PID_DEFAULT", "POS_PID_DEFAULT", "POS_PID_DEFAULT", "POS_PID_DEFAULT");
        :>> CONTROLS.velocityControl = ("POS_PID_DEFAULT", "POS_PID_DEFAULT", "POS_PID_DEFAULT", "POS_PID_DEFAULT");
        :>> CONTROLS.mixedControl = ("POS_PID_DEFAULT", "POS_PID_DEFAULT", "POS_PID_DEFAULT", "POS_PID_DEFAULT");
        :>> CONTROLS.torqueControl = ("TRQ_PID_DEFAULT", "TRQ_PID_DEFAULT", "TRQ_PID_DEFAULT", "TRQ_PID_DEFAULT");
        :>> CONTROLS.currentPid = ("2FOC_CUR_CONTROL", "2FOC_CUR_CONTROL", "2FOC_CUR_CONTROL", "2FOC_CUR_CONTROL");
        :>> CONTROLS.speedPid = ("2FOC_VEL_CONTROL", "2FOC_VEL_CONTROL", "2FOC_VEL_CONTROL", "2FOC_VEL_CONTROL");
        :>> POS_PID_DEFAULT.kp = (711.11, 1066.66, 711.11, 1066.66);
        :>> POS_PID_DEFAULT.kd = (0.0, 0.0, 0.0, 0.0);
        :>> POS_PID_DEFAULT.ki = (7111.09, 10666.64, 7111.09, 10666.64);
        :>> POS_PID_DEFAULT.maxOutput = (8000, 8000, 8000, 8000);
        :>> POS_PID_DEFAULT.maxInt = (200, 200, 200, 1000);
        :>> POS_PID_DEFAULT.stictionUp = (0, 0, 0, 0);
        :>> POS_PID_DEFAULT.stictionDown = (0, 0, 0, 0);
        :>> POS_PID_DEFAULT.kff = (0, 0, 0, 0);
        :>> TRQ_PID_DEFAULT.kp = (200, 200, 250, 300);
        :>> TRQ_PID_DEFAULT.kd = (0, 0, 0, 0);
        :>> TRQ_PID_DEFAULT.ki = (0, 0, 0, 0);
        :>> TRQ_PID_DEFAULT.maxOutput = (8000, 8000, 8000, 8000);
        :>> TRQ_PID_DEFAULT.maxInt = (500, 500, 500, 500);
        :>> TRQ_PID_DEFAULT.ko = (0, 0, 0, 0);
        :>> TRQ_PID_DEFAULT.stictionUp = (0.5, 0.5, 1, 1.7);
        :>> TRQ_PID_DEFAULT.stictionDown = (-0.7, -0.7, -0.8, -1.2);
        :>> TRQ_PID_DEFAULT.kff = (1, 1, 1, 1);
        :>> TRQ_PID_DEFAULT.viscousPos = (0.0030, 0.0006, 0.0007, 0.0007);
        :>> TRQ_PID_DEFAULT.viscousNeg = (0.0030, 0.0006, 0.0007, 0.0007);
        :>> TRQ_PID_DEFAULT.coulombPos = (0, 0, 0, 0);
        :>> TRQ_PID_DEFAULT.coulombNeg = (0, 0, 0, 0);
        :>> TRQ_PID_DEFAULT.velocityThres = (0, 0, 0, 0);
        :>> TRQ_PID_DEFAULT.filterType = (0, 0, 0, 0);
        :>> TRQ_PID_DEFAULT.ktau = (180, 464, 463, 449);
        :>> _2FOC_CUR_CONTROL.kp = (8, 8, 8, 8);
        :>> _2FOC_CUR_CONTROL.kd = (0, 0, 0, 0);
        :>> _2FOC_CUR_CONTROL.ki = (2, 2, 2, 2);
        :>> _2FOC_CUR_CONTROL.shift = (10, 10, 10, 10);
        :>> _2FOC_CUR_CONTROL.maxOutput = (32000, 32000, 32000, 32000);
        :>> _2FOC_CUR_CONTROL.maxInt = (32000, 32000, 32000, 32000);
        :>> _2FOC_CUR_CONTROL.kff = (0, 0, 0, 0);
        :>> _2FOC_VEL_CONTROL.kp = (12, 12, 12, 12);
        :>> _2FOC_VEL_CONTROL.kd = (0, 0, 0, 0);
        :>> _2FOC_VEL_CONTROL.ki = (16, 16, 16, 16);
        :>> _2FOC_VEL_CONTROL.shift = (10, 10, 10, 10);
        :>> _2FOC_VEL_CONTROL.maxOutput = (32000, 32000, 32000, 32000);
        :>> _2FOC_VEL_CONTROL.maxInt = (32000, 32000, 32000, 32000);
        :>> _2FOC_VEL_CONTROL.kff = (0, 0, 0, 0);
    }
    part left_arm_eb24_j4_7_mc :> motorControl {
        :>> includes = ("../../general.xml", "../../hardware/electronics/left_arm_eb24_j4_7_eln.xml", "../../hardware/mechanicals/left_arm_eb24_j4_7_mec.xml", "./left_arm_eb24_j4_7_mc_service.xml");
        :>> device_type = "embObjMotionControl";
        :>> device_name = "left_arm-eb24-j4_7-mc";
        :>> LIMITS.jntPosMin = (-85, -70, -15, 10);
        :>> LIMITS.jntPosMax = (85, 25, 35, 60);
        :>> LIMITS.jntVelMax = (1000, 1000, 1000, 1000);
        :>> LIMITS.motorOverloadCurrents = (10000, 2000, 2000, 2000);
        :>> LIMITS.motorNominalCurrents = (5000, 1000, 1000, 600);
        :>> LIMITS.motorPeakCurrents = (5000, 2000, 2000, 1000);
        :>> LIMITS.motorPwmLimit = (3360, 3360, 3360, 3360);
        :>> TIMEOUTS.velocity = (100, 100, 100, 100);
        :>> IMPEDANCE.stiffness = (0.0, 0.0, 0.0, 0.0);
        :>> IMPEDANCE.damping = (0.0, 0.0, 0.0, 0.0);
        :>> CONTROLS.positionControl = ("POS_PID_DEFAULT", "POS_PID_DEFAULT", "POS_PID_DEFAULT", "POS_PID_DEFAULT");
        :>> CONTROLS.velocityControl = ("POS_PID_DEFAULT", "POS_PID_DEFAULT", "POS_PID_DEFAULT", "POS_PID_DEFAULT");
        :>> CONTROLS.mixedControl = ("POS_PID_DEFAULT", "POS_PID_DEFAULT", "POS_PID_DEFAULT", "POS_PID_DEFAULT");
        :>> CONTROLS.torqueControl = ("TRQ_PID_DEFAULT", "none", "none", "none");
        :>> CONTROLS.currentPid = ("none", "none", "none", "none");
        :>> CONTROLS.speedPid = ("none", "none", "none", "none");
        :>> POS_PID_DEFAULT.kp = (-200.0, -500.0, -500.0, -500.0);
        :>> POS_PID_DEFAULT.kd = (0.0, 0.0, 0.0, 0.0);
        :>> POS_PID_DEFAULT.ki = (-200.0, -50.0, -50.0, -50.0);
        :>> POS_PID_DEFAULT.maxOutput = (3360, 3360, 3360, 3360);	
        :>> POS_PID_DEFAULT.maxInt = (3360, 3360, 3360, 3360);
        :>> POS_PID_DEFAULT.stictionUp = (0, 0, 0, 0);
        :>> POS_PID_DEFAULT.stictionDown = (0, 0, 0, 0);
        :>> POS_PID_DEFAULT.kff = (0, 0, 0, 0);
        :>> TRQ_PID_DEFAULT.kp = (-1000, 0, 0, 0);
        :>> TRQ_PID_DEFAULT.kd = (0, 0, 0, 0);
        :>> TRQ_PID_DEFAULT.ki = (0, 0, 0, 0);
        :>> TRQ_PID_DEFAULT.maxOutput = (3360, 0, 0, 0);
        :>> TRQ_PID_DEFAULT.maxInt = (500, 0, 0, 0);
        :>> TRQ_PID_DEFAULT.ko = (0, 0, 0, 0);
        :>> TRQ_PID_DEFAULT.stictionUp = (0, 0, 0, 0);
        :>> TRQ_PID_DEFAULT.stictionDown = (0, 0, 0, 0);
        :>> TRQ_PID_DEFAULT.kff = (0, 0, 0, 0);
        :>> TRQ_PID_DEFAULT.viscousPos = (0, 0, 0, 0);
        :>> TRQ_PID_DEFAULT.viscousNeg = (0, 0, 0, 0);
        :>> TRQ_PID_DEFAULT.coulombPos = (0, 0, 0, 0);
        :>> TRQ_PID_DEFAULT.coulombNeg = (0, 0, 0, 0);
        :>> TRQ_PID_DEFAULT.velocityThres = (0, 0, 0, 0);
        :>> TRQ_PID_DEFAULT.filterType = (0, 0, 0, 0);
        :>> TRQ_PID_DEFAULT.ktau = (1, 0, 0, 0);
    }
    part left_arm_eb25_j8_11_mc :> motorControl {
        :>> includes = ("../../general.xml", "../../hardware/electronics/left_arm_eb25_j8_11_eln.xml", "../../hardware/mechanicals/left_arm_eb25_j8_11_mec.xml", "./left_arm_eb25_j8_11_mc_service.xml");
        :>> device_type = "embObjMotionControl";
        :>> device_name = "left_arm-eb25-j8_11-mc";
        :>> LIMITS.jntPosMin = (10, 0, 0, 0);
        :>> LIMITS.jntPosMax = (90, 90, 180, 90);
        :>> LIMITS.jntVelMax = (1000, 1000, 1000, 1000);
        :>> LIMITS.motorOverloadCurrents = (2000, 2000, 2000, 2000);
        :>> LIMITS.motorNominalCurrents = (600, 600, 600, 600);
        :>> LIMITS.motorPeakCurrents = (1000, 1000, 1000, 1000);
        :>> LIMITS.motorPwmLimit = (3360, 3360, 3360, 3360);
        :>> TIMEOUTS.velocity = (100, 100, 100, 100);
        :>> IMPEDANCE.stiffness = (0.0, 0.0, 0.0, 0.0);
        :>> IMPEDANCE.damping = (0.0, 0.0, 0.0, 0.0);
        :>> CONTROLS.positionControl = ("POS_PID_DEFAULT", "POS_PID_DEFAULT", "POS_PID_DEFAULT", "POS_PID_DEFAULT");
        :>> CONTROLS.velocityControl = ("POS_PID_DEFAULT", "POS_PID_DEFAULT", "POS_PID_DEFAULT", "POS_PID_DEFAULT");
        :>> CONTROLS.mixedControl = ("POS_PID_DEFAULT", "POS_PID_DEFAULT", "POS_PID_DEFAULT", "POS_PID_DEFAULT");
        :>> CONTROLS.torqueControl = ("none", "none", "none", "none");
        :>> CONTROLS.currentPid = ("none", "none", "none", "none");
        :>> CONTROLS.speedPid = ("none", "none", "none", "none");
        :>> POS_PID_DEFAULT.kp = (-150.0, 400.0, 500.0, 500.0);
        :>> POS_PID_DEFAULT.kd = (0.0, 0.0, 0.0, 0.0);
        :>> POS_PID_DEFAULT.ki = (-15.0, 40.0, 50.0, 50.0);
        :>> POS_PID_DEFAULT.maxOutput = (3360, 3360, 3360, 3360);	
        :>> POS_PID_DEFAULT.maxInt = (3360, 3360, 3360, 3360);
        :>> POS_PID_DEFAULT.stictionUp = (0, 0, 0, 0);
        :>> POS_PID_DEFAULT.stictionDown = (0, 0, 0, 0);
        :>> POS_PID_DEFAULT.kff = (0, 0, 0, 0);
    }
    part left_arm_eb26_j12_15_mc :> motorControl {
        :>> includes = ("../../general.xml", "../../hardware/electronics/left_arm_eb26_j12_15_eln.xml", "../../hardware/mechanicals/left_arm_eb26_j12_15_mec.xml", "./left_arm_eb26_j12_15_mc_service.xml");
        :>> device_type = "embObjMotionControl";
        :>> device_name = "left_arm-eb26-j12_15-mc";
        :>> LIMITS.jntPosMin = (0, 0, 0, 0);
        :>> LIMITS.jntPosMax = (180, 90, 180, 270);
        :>> LIMITS.jntVelMax = (1000, 1000, 1000, 1000);
        :>> LIMITS.motorOverloadCurrents = (2000, 2000, 2000, 2000);
        :>> LIMITS.motorNominalCurrents = (600, 600, 600, 600);
        :>> LIMITS.motorPeakCurrents = (1000, 1000, 1000, 1000);
        :>> LIMITS.motorPwmLimit = (3360, 3360, 3360, 3360);
        :>> TIMEOUTS.velocity = (100, 100, 100, 100);
        :>> IMPEDANCE.stiffness = (0.0, 0.0, 0.0, 0.0);
        :>> IMPEDANCE.damping = (0.0, 0.0, 0.0, 0.0);
        :>> CONTROLS.positionControl = ("POS_PID_DEFAULT", "POS_PID_DEFAULT", "POS_PID_DEFAULT", "POS_PID_DEFAULT");
        :>> CONTROLS.velocityControl = ("POS_PID_DEFAULT", "POS_PID_DEFAULT", "POS_PID_DEFAULT", "POS_PID_DEFAULT");
        :>> CONTROLS.mixedControl = ("POS_PID_DEFAULT", "POS_PID_DEFAULT", "POS_PID_DEFAULT", "POS_PID_DEFAULT");
        :>> CONTROLS.torqueControl = ("none", "none", "none", "none");
        :>> CONTROLS.currentPid = ("none", "none", "none", "none");
        :>> CONTROLS.speedPid = ("none", "none", "none", "none");
        :>> POS_PID_DEFAULT.kp = (-500.0, 500.0, 500.0, -200.0);
        :>> POS_PID_DEFAULT.kd = (0.0, 0.0, 0.0, 0.0);
        :>> POS_PID_DEFAULT.ki = (-50.0, 50.0, 50.0, -20.0);
        :>> POS_PID_DEFAULT.maxOutput = (3360, 3360, 3360, 3360);	
        :>> POS_PID_DEFAULT.maxInt = (3360, 3360, 3360, 3360);
        :>> POS_PID_DEFAULT.stictionUp = (0, 0, 0, 0);
        :>> POS_PID_DEFAULT.stictionDown = (0, 0, 0, 0);
        :>> POS_PID_DEFAULT.kff = (0, 0, 0, 0);
    }
    part left_arm_eb1_j0_3_mc_service :> service {
        :>> SERVICE.type = "eomn_serv_MC_foc";
        :>> SERVICE.PROPERTIES.ETHBOARD.type = "ems4";
        :>> SERVICE.PROPERTIES.CANBOARDS.type = "foc";
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ACTUATOR.type = ("eomc_act_foc", "foc", "foc", "foc");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ACTUATOR._port = ("CAN1:1:0", "CAN1:2:0", "CAN1:3:0", "CAN1:4:0");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER1.type = ("eomc_enc_aea", "aea", "aea", "aea");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER1._port = ("CONN:P6", "CONN:P7", "CONN:P8", "CONN:P9");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER1.position = ("eomc_pos_atjoint", "atjoint", "atjoint", "atjoint");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER1.resolution = (-4096, -4096, 4096, -4096);
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER1.tolerance = (0.703, 0.703, 0.703, 0.703);
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER2.type = ("roie", "roie", "roie", "roie");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER2._port = ("CAN1:1:0", "CAN1:2:0", "CAN1:3:0", "CAN1:4:0");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER2.position = ("atmotor", "atmotor", "atmotor", "atmotor");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER2.resolution = (-14400, -14400, -14400, -14400);
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER2.tolerance = (0, 0, 0, 0);
    }
    part left_arm_eb24_j4_7_mc_service :> service {
        :>> SERVICE.type = "eomn_serv_MC_mc4plus";
        :>> SERVICE.PROPERTIES.ETHBOARD.type = "mc4plus";
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ACTUATOR.type = ("pwm", "pwm", "pwm", "pwm");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ACTUATOR._port = ("CONN:P5", "CONN:P2", "CONN:P4", "CONN:P3");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER1.type = ("qenc", "aea", "aea", "absanalog");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER1._port = ("CONN:P5", "CONN:P10", "CONN:P11", "CONN:P3");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER1.position = ("atjoint", "atjoint", "atjoint", "atjoint");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER1.resolution = (1, -4096, 4096, 65535);
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER1.tolerance = (0, 0.703, 0.703, 0);
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER2.type = ("qenc", "qenc", "qenc", "none");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER2._port = ("CONN:P5", "CONN:P2", "CONN:P4", "CONN:none");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER2.position = ("atmotor", "atmotor", "atmotor", "none");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER2.resolution = (-2048, 1600, 1600, 1);
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER2.tolerance = (0, 0, 0, 0);
    }
    part left_arm_eb25_j8_11_mc_service :> service {
        :>> SERVICE.type = "eomn_serv_MC_mc4plusmais";
        :>> SERVICE.PROPERTIES.ETHBOARD.type = "mc4plus";
        :>> SERVICE.PROPERTIES.CANBOARDS.type = "mais";
        :>> SERVICE.PROPERTIES.MAIS.location = "CAN1:14";
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ACTUATOR.type = ("pwm", "pwm", "pwm", "pwm");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ACTUATOR._port = ("CONN:P3", "CONN:P2", "CONN:P4", "CONN:P5");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER1.type = ("absanalog", "mais", "mais", "mais");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER1._port = ("CONN:P3", "MAIS:thumbproximal", "MAIS:thumbdistal", "MAIS:indexproximal");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER1.position = ("atjoint", "atjoint", "atjoint", "atjoint");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER1.resolution = (65535, 65535, 65535, 65535);
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER1.tolerance = (0, 0, 0, 0);
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER2.type = ("none", "qenc", "qenc", "qenc");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER2._port = ("CONN:none", "CONN:P2", "CONN:P4", "CONN:P5");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER2.position = ("none", "atmotor", "atmotor", "atmotor");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER2.resolution = (1, 40, 40, 40);
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER2.tolerance = (0, 0, 0, 0);
    }
    part left_arm_eb26_j12_15_mc_service :> service {
        :>> SERVICE.type = "eomn_serv_MC_mc4plusmais";
        :>> SERVICE.PROPERTIES.ETHBOARD.type = "mc4plus";
        :>> SERVICE.PROPERTIES.CANBOARDS.type = "mais";
        :>> SERVICE.PROPERTIES.MAIS.location = "CAN1:14";
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ACTUATOR.type = ("pwm", "pwm", "pwm", "pwm");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ACTUATOR._port = ("CONN:P3", "CONN:P2", "CONN:P4", "CONN:P5");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER1.type = ("mais", "mais", "mais", "mais");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER1._port = ("MAIS:indexdistal", "MAIS:mediumproximal", "MAIS:mediumdistal", "MAIS:littlefingers");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER1.position = ("atjoint", "atjoint", "atjoint", "atjoint");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER1.resolution = (65535, 65535, 65535, 65535);
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER1.tolerance = (0, 0, 0, 0);
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER2.type = ("qenc", "qenc", "qenc", "qenc");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER2._port = ("CONN:P3", "CONN:P2", "CONN:P4", "CONN:P5");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER2.position = ("atmotor", "atmotor", "atmotor", "atmotor");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER2.resolution = (40, 40, 40, 40);
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER2.tolerance = (0, 0, 0, 0);
    }
    part left_arm_eb1_IMU :> inertial {
        :>> includes = ("../../general.xml", "../../hardware/electronics/left_arm_eb1_j0_3_eln.xml");
        :>> device_name = "left_arm-eb1-imu";
        :>> device_type = "embObjIMU";
        :>> SERVICE.type = "eomn_serv_AS_inertials3";
        :>> SERVICE.PROPERTIES.CANBOARDS.type = "eobrd_strain2";
        :>> SERVICE.PROPERTIES.CANBOARDS.PROTOCOL.major = 2;
        :>> SERVICE.PROPERTIES.SENSORS.id = ("l_arm_ft_acc", "l_arm_ft_gyro", "l_arm_ft_mag", "l_arm_ft_eul", "l_arm_ft_status");
        :>> SERVICE.PROPERTIES.SENSORS.sensorName = ("l_arm_ft_imu", "l_arm_ft_imu", "l_arm_ft_imu", "l_arm_ft_imu", "l_arm_ft_imu");
        :>> SERVICE.PROPERTIES.SENSORS.type = ("eoas_imu_acc", "eoas_imu_gyr", "eoas_imu_mag", "eoas_imu_eul", "eoas_imu_status");
        :>> SERVICE.PROPERTIES.SENSORS.boardType = ("strain2", "strain2", "strain2", "strain2", "strain2");
        :>> SERVICE.PROPERTIES.SENSORS.location = ("CAN2:13", "CAN2:13", "CAN2:13", "CAN2:13", "CAN2:13");
        :>> SERVICE.SETTINGS.acquisitionRate = 10;
        :>> SERVICE.SETTINGS.enabledSensors = ("l_arm_ft_acc", "l_arm_ft_gyro", "l_arm_ft_mag", "l_arm_ft_eul", "l_arm_ft_status");
    }
    part left_arm_eb1_j0_3_strain :> ft {
        :>> includes = ("../../general.xml", "../../hardware/electronics/left_arm_eb1_j0_3_eln.xml");
        :>> device_name = "left_arm-eb1-j0_3-strain";
        :>> device_type = "embObjFTsensor";
        :>> SERVICE.PROPERTIES.CANBOARDS.type = "strain2";
        :>> SERVICE.PROPERTIES.CANBOARDS.PROTOCOL.major = 2;
        :>> SERVICE.PROPERTIES.SENSORS.id = "l_arm_ft";
        :>> SERVICE.PROPERTIES.SENSORS.framename = "l_arm_ft";
        :>> SERVICE.PROPERTIES.SENSORS.location = "CAN2:13";
        :>> SERVICE.SETTINGS.enabledSensors = ("l_arm_ft");
    }
    part left_arm_cartesian :> cartesian {
        :>> device_name = "left_arm-cartesian";
        :>> device_type = "cartesiancontrollerserver";
        :>> GENERAL.ControllerName = "icub/cartesianController/left_arm";
        :>> GENERAL.SolverNameToConnect = "cartesianSolver/left_arm";
        :>> GENERAL.KinematicType = "left_v2.7";
        :>> DRIVER_1.Key = "left_arm";
        :>> startup.phase = "startup";
        :>> startup.level = 15;
        :>> startup.type = "attach";
        :>> startup.elementName = ("torso", "left_arm");
        :>> startup.elementValue = ("torso-mc_remapper", "left_arm-mc_remapper");
        :>> shutdown.phase = "shutdown";
        :>> shutdown.level = 15;
        :>> shutdown.type = "detach";
    }
    part left_arm_eb24_j4_7_skin :> skin {
        :>> includes = ("../../general.xml", "../../hardware/electronics/left_arm_eb24_j4_7_eln.xml");
        :>> device_name = "left_arm-eb24-j4_7-skin";
        :>> device_type = "embObjSkin";
        :>> patches.skinCanAddrsPatch1 = (14, 13, 12, 11, 10, 9, 8);
    }
    part left_arm_eb24_j4_7_skinSpec :> skinSpec {
    }
    part left_arm_eb26_j12_15_mais :> mais {
        :>> includes = ("../../general.xml", "../../hardware/electronics/left_arm_eb26_j12_15_eln.xml");
        :>> device_name = "left_arm-eb26-j12_15-mais";
        :>> device_type = "embObjMais";
        :>> SERVICE.PROPERTIES.SENSORS.id = "l_hand_mais";
        :>> SERVICE.PROPERTIES.SENSORS.location = "CAN1:14";
        :>> SERVICE.SETTINGS.enabledSensors = "l_hand_mais";
    }

    part left_arm_mc_wrapper :> wrapper {
        :>> folder_name = "wrappers/motorControl/";
        :>> device_name = "left_arm-mc_nws_yarp";
        :>> device_type = "controlBoard_nws_yarp";
        :>> period = 0.01;
        :>> name = "/icub/left_arm";
        :>> startup.phase = "startup";
        :>> startup.type = "attach";
        :>> startup.level = 10;
        :>> startup.elementName = "device";
        :>> startup.elementValue = "left_arm-mc_remapper";
        :>> shutdown.phase = "shutdown";
        :>> shutdown.type = "detach";
        :>> shutdown.level = 15;
    }
    part left_arm_mc_remapper :> remapper {
        :>> folder_name = "wrappers/motorControl/";
        :>> device_type = "controlboardremapper";
        :>> device_name = "left_arm-mc_remapper";
        :>> elementName = ("left_arm_joints1", "left_arm_joints2", "left_arm_joints3", "left_arm_joints4");
        :>> elementValue = ("( 0  3  0  3 )", "( 4  7  0  3 )", "( 8 11  0  3 )", "(12 15  0  3 )");
        :>> joints = 16;
        :>> startup.phase = "startup";
        :>> startup.type = "attach";
        :>> startup.level = 5;
        :>> startup.elementName = ("left_arm_joints1", "left_arm_joints2", "left_arm_joints3", "left_arm_joints4");
        :>> startup.elementValue = ("left_arm-eb1-j0_3-mc", "left_arm-eb24-j4_7-mc", "left_arm-eb25-j8_11-mc", "left_arm-eb26-j12_15-mc");
        :>> shutdown.phase = "shutdown";
        :>> shutdown.type = "detach";
        :>> shutdown.level = 20;
    }

    part left_arm_FT_wrapper :> wrapper {
        :>> folder_name = "wrappers/FT/";
        :>> device_name = "left_arm-FT_wrapper";
        :>> device_type = "multipleanalogsensorsserver";
        :>> period = 10;
        :>> name = "/icub/left_arm/FT";
        :>> startup.phase = "startup";
        :>> startup.type = "attach";
        :>> startup.level = 5;
        :>> startup.elementName = "FirstStrain";
        :>> startup.elementValue = "left_arm-eb1-j0_3-strain";
        :>> shutdown.phase = "shutdown";
        :>> shutdown.type = "detach";
        :>> shutdown.level = 5;
    }

    part left_arm_mais_wrapper :> wrapper {
        :>> folder_name = "wrappers/MAIS/";
        :>> device_name = "left_arm-mais_wrapper";
        :>> device_type = "multipleanalogsensorsserver";
        :>> period = 10;
        :>> name = "/icub/left_arm/MAIS";
        :>> startup.phase = "startup";
        :>> startup.type = "attach";
        :>> startup.level = 5;
        :>> startup.elementName = "leftMais";
        :>> startup.elementValue = "left_arm-eb26-j12_15-mais";
        :>> shutdown.phase = "shutdown";
        :>> shutdown.type = "detach";
        :>> shutdown.level = 5;
    }

    part left_arm_inertials_wrapper :> wrapper {
        :>> folder_name = "wrappers/inertials/";
        :>> device_name = "left_arm-inertials_wrapper";
        :>> device_type = "multipleanalogsensorsserver";
        :>> period = 10;
        :>> name = "/icub/left_arm/inertials";
        :>> startup.phase = "startup";
        :>> startup.type = "attach";
        :>> startup.level = 5;
        :>> startup.elementName = "SetOfIMUs";
        :>> startup.elementValue = "left_arm-inertials_remapper";
        :>> shutdown.phase = "shutdown";
        :>> shutdown.type = "detach";
        :>> shutdown.level = 5;
    }
}