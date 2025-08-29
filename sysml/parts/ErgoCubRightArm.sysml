part def ErgoCubRightArm {
    part right_arm_calib :> calibrator {
        :>> device_type = "parametricCalibratorEth";
        :>> device_name = "right_arm-calibrator";
        :>> GENERAL.joints = 13;
        :>> GENERAL.deviceName = "Right_Arm_Calibrator";
        :>> HOME.positionHome = (5, 30, 0, 10, 0, 0, 0, 30, 0, 0, 0, 0, 0);
        :>> HOME.velocityHome = (10, 10, 10, 10, 10, 10, 40, 40, 40, 40, 40, 40, 40);
        :>> CALIBRATION.calibrationType = (10, 10, 10, 10, 12, 12, 12, 12, 14, 12, 14, 14, 14);
        :>> CALIB_ORDER = "";
        :>> startup.phase = "startup";
        :>> startup.type = "calibrate";
        :>> startup.target = "right_arm-mc_remapper";
        :>> interrupt1.phase = "interrupt1";
        :>> interrupt1.level = 1;
        :>> interrupt1.type = "park";
        :>> interrupt1.target = "right_arm-mc_remapper";
        :>> interrupt3.phase = "interrupt3";
        :>> interrupt3.level = 1;
        :>> interrupt3.type = "abort";
    }
    part right_arm_eb1_j0_1_eln :> electronics {
        :>> ETH_BOARD.ETH_BOARD_PROPERTIES.IpAddress = "10.0.1.1";
        :>> ETH_BOARD.ETH_BOARD_PROPERTIES.Type = "ems4";
        :>> ETH_BOARD.ETH_BOARD_SETTINGS.Name = "right_arm-eb1-j0_1";
        :>> ETH_BOARD.ETH_BOARD_SETTINGS.RUNNINGMODE.TXrateOfRegularROPs = 1;
    }
    part right_arm_eb3_j2_3_eln :> electronics {
        :>> ETH_BOARD.ETH_BOARD_PROPERTIES.IpAddress = "10.0.1.3";
        :>> ETH_BOARD.ETH_BOARD_PROPERTIES.Type = "ems4";
        :>> ETH_BOARD.ETH_BOARD_SETTINGS.Name = "right_arm-eb3-j2_3";
        :>> ETH_BOARD.ETH_BOARD_SETTINGS.RUNNINGMODE.TXrateOfRegularROPs = 1;
    }
    part right_arm_eb30_j4_6_eln :> electronics {
        :>> ETH_BOARD.ETH_BOARD_PROPERTIES.IpAddress = "10.0.1.30";
        :>> ETH_BOARD.ETH_BOARD_PROPERTIES.Type = "amc";
        :>> ETH_BOARD.ETH_BOARD_SETTINGS.Name = "right_arm-eb30-j4_6";
        :>> ETH_BOARD.ETH_BOARD_SETTINGS.RUNNINGMODE.TXrateOfRegularROPs = 1;
    }
    part right_arm_eb22_j7_10_eln :> electronics {
        :>> ETH_BOARD.ETH_BOARD_PROPERTIES.IpAddress = "10.0.1.22";
        :>> ETH_BOARD.ETH_BOARD_PROPERTIES.Type = "mc4plus";
        :>> ETH_BOARD.ETH_BOARD_SETTINGS.Name = "right_arm-eb22-j7_10";
        :>> ETH_BOARD.ETH_BOARD_SETTINGS.RUNNINGMODE.TXrateOfRegularROPs = 1;
    }
    part right_arm_eb24_j11_12_eln :> electronics {
        :>> ETH_BOARD.ETH_BOARD_PROPERTIES.IpAddress = "10.0.1.24";
        :>> ETH_BOARD.ETH_BOARD_PROPERTIES.Type = "mc4plus";
        :>> ETH_BOARD.ETH_BOARD_SETTINGS.Name = "right_arm-eb24-j11_12";
        :>> ETH_BOARD.ETH_BOARD_SETTINGS.RUNNINGMODE.TXrateOfRegularROPs = 1;
    }
    part right_arm_eb1_j0_1_mec :> mechanicals {
        :>> GENERAL.Joints = 2;
        :>> GENERAL.AxisMap = (0, 1);
        :>> GENERAL.AxisName = ("r_shoulder_pitch", "r_shoulder_roll");
        :>> GENERAL.AxisType = ("revolute", "revolute");
        :>> GENERAL.Encoder = (182.044, 182.044);
        :>> GENERAL.fullscalePWM = (32000, 32000);
        :>> GENERAL.ampsToSensor = (1000.0, 1000.0);
        :>> GENERAL.Gearbox_M2J = (-100.0, -100.0);
        :>> GENERAL.Gearbox_E2J = (64, 64);
        :>> GENERAL.useMotorSpeedFbk = (1, 1);
        :>> GENERAL.MotorType = ("MOOG-BL-C2900576", "MOOG-BL-C2900576");
        :>> LIMITS.hardwareJntPosMin = (-170, -15);
        :>> LIMITS.hardwareJntPosMax = (35, 150);
        :>> LIMITS.rotorPosMin = (0, 0);
        :>> LIMITS.rotorPosMax = (0, 0);
        :>> _2FOC.HasHallSensor = (0, 0);
        :>> _2FOC.HasTempSensor = (0, 0);
        :>> _2FOC.HasRotorEncoder = (1, 1);
        :>> _2FOC.HasRotorEncoderIndex = (1, 1);
        :>> _2FOC.HasSpeedEncoder = (0, 0);
        :>> _2FOC.RotorIndexOffset = (227, 227);
        :>> _2FOC.MotorPoles = (8, 8);
        :>> JOINTSET_CFG.numberofsets = 2;
        :>> JOINTSET_CFG.JOINTSET_0.listofjoints = (0);
        :>> JOINTSET_CFG.JOINTSET_1.listofjoints = (1);
    }
    part right_arm_eb3_j2_3_mec :> mechanicals {
        :>> GENERAL.Joints = 2;
        :>> GENERAL.AxisMap = (0, 1);
        :>> GENERAL.AxisName = ("r_shoulder_yaw", "r_elbow");
        :>> GENERAL.AxisType = ("revolute", "revolute");
        :>> GENERAL.Encoder = (182.044, 182.044);
        :>> GENERAL.fullscalePWM = (3360, 3360);
        :>> GENERAL.ampsToSensor = (1000.0, 1000.0);
        :>> GENERAL.Gearbox_M2J = (-100.0, 100.0);
        :>> GENERAL.Gearbox_E2J = (32, 32);
        :>> GENERAL.useMotorSpeedFbk = (1, 1);
        :>> GENERAL.MotorType = ("MOOG-BL-C2900575", "MOOG-BL-C2900575");
        :>> LIMITS.hardwareJntPosMin = (-52, -5);
        :>> LIMITS.hardwareJntPosMax = (82, 120);
        :>> LIMITS.rotorPosMin = (0, 0);
        :>> LIMITS.rotorPosMax = (0, 0);
        :>> _2FOC.HasHallSensor = (0, 0);
        :>> _2FOC.HasTempSensor = (0, 0);
        :>> _2FOC.HasRotorEncoder = (1, 1);
        :>> _2FOC.HasRotorEncoderIndex = (1, 1);
        :>> _2FOC.HasSpeedEncoder = (0, 0);
        :>> _2FOC.RotorIndexOffset = (74, 333);
        :>> _2FOC.MotorPoles = (8, 8);
        :>> JOINTSET_CFG.numberofsets = 2;
        :>> JOINTSET_CFG.JOINTSET_0.listofjoints = (0);
        :>> JOINTSET_CFG.JOINTSET_1.listofjoints = (1);
    }
    part right_arm_eb30_j4_6_mec :> mechanicals {
        :>> GENERAL.Joints = 3;
        :>> GENERAL.AxisMap = (0, 1, 2);
        :>> GENERAL.AxisName = ("r_wrist_yaw", "r_wrist_roll", "r_wrist_pitch");
        :>> GENERAL.AxisType = ("revolute", "revolute", "revolute");
        :>> GENERAL.Encoder = (182.044, 182.044, 182.044);
        :>> GENERAL.fullscalePWM = (32000, 32000, 32000);
        :>> GENERAL.ampsToSensor = (1000.0, 1000.0, 1000.0);
        :>> GENERAL.Gearbox_M2J = (-392.0, -392.0, -392.0);
        :>> GENERAL.Gearbox_E2J = (2.0, 2.0, 2.0);
        :>> GENERAL.useMotorSpeedFbk = (0, 0, 0);
        :>> GENERAL.MotorType = ("FAULHABER", "FAULHABER", "FAULHABER");
        :>> LIMITS.hardwareJntPosMax = (92, 52, 32);
        :>> LIMITS.hardwareJntPosMin = (-92, -62, -32);
        :>> LIMITS.rotorPosMin = (0, 0, 0);
        :>> LIMITS.rotorPosMax = (0, 0, 0);
        :>> JOINTSET_CFG.JOINTSET_0.listofjoints = "(0 1 2)";
        :>> JOINTSET_CFG.JOINTSET_0._constraint = "ergocubwrist";
        :>> JOINTSET_CFG.JOINTSET_0.param1 = 20;
    }
    part right_arm_eb22_j7_10_mec :> mechanicals {
        :>> GENERAL.Joints = 4;
        :>> GENERAL.AxisMap = (0, 1, 2, 3);
        :>> GENERAL.AxisName = ("r_thumb_oc", "r_index_oc", "r_middle_oc", "r_ring_pinky_oc");
        :>> GENERAL.AxisType = ("revolute", "revolute", "revolute", "revolute");
        :>> GENERAL.Encoder = (182.044, 182.044, 182.044, 182.044);
        :>> GENERAL.fullscalePWM = (3360, 3360, 3360, 3360);
        :>> GENERAL.ampsToSensor = (1000.0, 1000.0, 1000.0, 1000.0);
        :>> GENERAL.Gearbox_M2J = (159, 159, 159, 159);
        :>> GENERAL.Gearbox_E2J = (1, 1, 1, 1);
        :>> GENERAL.useMotorSpeedFbk = (0, 0, 0, 0);
        :>> GENERAL.MotorType = ("DC", "DC", "DC", "DC");
        :>> LIMITS.hardwareJntPosMin = (0, 0, 0, 0);
        :>> LIMITS.hardwareJntPosMax = (90, 90, 90, 90); 
        :>> LIMITS.rotorPosMin = (-26000, -26000, -26000, -26000);
        :>> LIMITS.rotorPosMax = (-100, -100, -100, -100);
        :>> JOINTSET_CFG.numberofsets = 4;
        :>> JOINTSET_CFG.JOINTSET_0.listofjoints = (0);
        :>> JOINTSET_CFG.JOINTSET_1.listofjoints = (1);
        :>> JOINTSET_CFG.JOINTSET_2.listofjoints = (2);
        :>> JOINTSET_CFG.JOINTSET_3.listofjoints = (3);
    }
    part right_arm_eb24_j11_12_mec :> mechanicals {
        :>> GENERAL.Joints = 2;
        :>> GENERAL.AxisMap = (0, 1);
        :>> GENERAL.AxisName = ("r_thumb_add", "r_index_add");
        :>> GENERAL.AxisType = ("revolute", "revolute");
        :>> GENERAL.Encoder = (182.044, 182.044);
        :>> GENERAL.fullscalePWM = (3360, 3360);
        :>> GENERAL.ampsToSensor = (1000.0, 1000.0);
        :>> GENERAL.Gearbox_M2J = (159, 159);
        :>> GENERAL.Gearbox_E2J = (1, 1);
        :>> GENERAL.useMotorSpeedFbk = (0, 0);
        :>> GENERAL.MotorType = ("DC", "DC");
        :>> LIMITS.hardwareJntPosMin = (0, 6);
        :>> LIMITS.hardwareJntPosMax = (90, 20);
        :>> JOINTSET_CFG.numberofsets = 2;
        :>> JOINTSET_CFG.JOINTSET_0.listofjoints = (0);
        :>> JOINTSET_CFG.JOINTSET_1.listofjoints = (1);
    }
    part right_arm_eb1_j0_1_mc :> motorControl {
        :>> includes = ("../../general.xml", "../../hardware/electronics/right_arm_eb1_j0_1_eln.xml", "../../hardware/mechanicals/right_arm_eb1_j0_1_mec.xml", "./right_arm_eb1_j0_1_mc_service.xml");
        :>> device_type = "embObjMotionControl";
        :>> device_name = "right_arm-eb1-j0_1-mc";
        :>> LIMITS.jntPosMin = (-130, 0);
        :>> LIMITS.jntPosMax = (14, 130);
        :>> LIMITS.jntVelMax = (120, 120);
        :>> LIMITS.motorOverloadCurrents = (15000, 15000);
        :>> LIMITS.motorNominalCurrents = (5000, 5000);
        :>> LIMITS.motorPeakCurrents = (12000, 12000);
        :>> LIMITS.motorPwmLimit = (8000, 8000);
        :>> TIMEOUTS.velocity = (100, 100);
        :>> IMPEDANCE.stiffness = (0.3, 0.3);
        :>> IMPEDANCE.damping = (0.05, 0.05);
        :>> CONTROLS.positionControl = ("POS_PID_DEFAULT", "POS_PID_DEFAULT");
        :>> CONTROLS.velocityControl = ("POS_PID_DEFAULT", "POS_PID_DEFAULT");
        :>> CONTROLS.mixedControl = ("POS_PID_DEFAULT", "POS_PID_DEFAULT");
        :>> CONTROLS.torqueControl = ("TRQ_PID_DEFAULT", "TRQ_PID_DEFAULT");
        :>> CONTROLS.currentPid = ("2FOC_CUR_CONTROL", "2FOC_CUR_CONTROL");
        :>> CONTROLS.speedPid = ("2FOC_VEL_CONTROL", "2FOC_VEL_CONTROL");
        :>> POS_PID_DEFAULT.kp = (-4000, -1000);
        :>> POS_PID_DEFAULT.kd = (0.0, 0.0);
        :>> POS_PID_DEFAULT.ki = (-1000, -1000);
        :>> POS_PID_DEFAULT.maxOutput = (8000, 8000);
        :>> POS_PID_DEFAULT.maxInt = (2000, 2000);
        :>> TRQ_PID_DEFAULT.outputControlUnits = "dutycycle_percent";
        :>> TRQ_PID_DEFAULT.kp = (-3, -2);
        :>> TRQ_PID_DEFAULT.kd = (0, 0);
        :>> TRQ_PID_DEFAULT.ki = (-6, -4);
        :>> TRQ_PID_DEFAULT.maxOutput = (25, 25);
        :>> TRQ_PID_DEFAULT.maxInt = (1.56, 1.56);
        :>> TRQ_PID_DEFAULT.ko = (0, 0);
        :>> TRQ_PID_DEFAULT.stictionUp = (0, 0);
        :>> TRQ_PID_DEFAULT.stictionDown = (0, 0);
        :>> TRQ_PID_DEFAULT.kff = (1, 1);
        :>> TRQ_PID_DEFAULT.viscousPos = (-0.004, -0.004);
        :>> TRQ_PID_DEFAULT.viscousNeg = (-0.004, -0.004);
        :>> TRQ_PID_DEFAULT.coulombPos = (0, 0);
        :>> TRQ_PID_DEFAULT.coulombNeg = (0, 0);
        :>> TRQ_PID_DEFAULT.velocityThres = (0, 0);
        :>> TRQ_PID_DEFAULT.filterType = (0, 0);
        :>> TRQ_PID_DEFAULT.ktau = (-0.86, -0.72);
        :>> _2FOC_CUR_CONTROL.kp = (8, 8);
        :>> _2FOC_CUR_CONTROL.kd = (0, 0);
        :>> _2FOC_CUR_CONTROL.ki = (2, 2);
        :>> _2FOC_CUR_CONTROL.shift = (10, 10);
        :>> _2FOC_CUR_CONTROL.maxOutput = (32000, 32000);
        :>> _2FOC_CUR_CONTROL.maxInt = (32000, 32000);
        :>> _2FOC_CUR_CONTROL.kff = (0, 0);
        :>> _2FOC_VEL_CONTROL.kp = (12, 12);
        :>> _2FOC_VEL_CONTROL.kd = (0, 0);
        :>> _2FOC_VEL_CONTROL.ki = (16, 16);
        :>> _2FOC_VEL_CONTROL.shift = (10, 10);
        :>> _2FOC_VEL_CONTROL.maxOutput = (32000, 32000);
        :>> _2FOC_VEL_CONTROL.maxInt = (32000, 32000);
        :>> _2FOC_VEL_CONTROL.kff = (0, 0);
    }
    part right_arm_eb3_j2_3_mc :> motorControl {
        :>> includes = ("../../general.xml", "../../hardware/electronics/right_arm_eb3_j2_3_eln.xml", "../../hardware/mechanicals/right_arm_eb3_j2_3_mec.xml", "./right_arm_eb3_j2_3_mc_service.xml");
        :>> device_type = "embObjMotionControl";
        :>> device_name = "right_arm-eb3-j2_3-mc";
        :>> LIMITS.jntPosMin = (-50, -3);
        :>> LIMITS.jntPosMax = (80, 105);
        :>> LIMITS.jntVelMax = (120, 120);
        :>> LIMITS.motorOverloadCurrents = (15000, 15000);
        :>> LIMITS.motorNominalCurrents = (5000, 5000);
        :>> LIMITS.motorPeakCurrents = (9000, 9000);
        :>> LIMITS.motorPwmLimit = (8000, 8000);
        :>> TIMEOUTS.velocity = (100, 100);
        :>> IMPEDANCE.stiffness = (0.2, 0.1);
        :>> IMPEDANCE.damping = (0.05, 0.05);
        :>> CONTROLS.positionControl = ("POS_PID_DEFAULT", "POS_PID_DEFAULT");
        :>> CONTROLS.velocityControl = ("POS_PID_DEFAULT", "POS_PID_DEFAULT");
        :>> CONTROLS.mixedControl = ("POS_PID_DEFAULT", "POS_PID_DEFAULT");
        :>> CONTROLS.torqueControl = ("TRQ_PID_OUTPUT_CURR", "TRQ_PID_OUTPUT_CURR");
        :>> CONTROLS.currentPid = ("2FOC_CUR_CONTROL", "2FOC_CUR_CONTROL");
        :>> CONTROLS.speedPid = ("2FOC_VEL_CONTROL", "2FOC_VEL_CONTROL");
        :>> POS_PID_DEFAULT.kp = (-1000, 1000);
        :>> POS_PID_DEFAULT.kd = (0, 0);
        :>> POS_PID_DEFAULT.ki = (-1000, 1000);
        :>> POS_PID_DEFAULT.maxOutput = (8000, 8000);
        :>> POS_PID_DEFAULT.maxInt = (1000, 1000);
        :>> POS_PID_DEFAULT.stictionUp = (0, 0);
        :>> POS_PID_DEFAULT.stictionDown = (0, 0);
        :>> POS_PID_DEFAULT.kff = (0, 0);
        :>> TRQ_PID_DEFAULT.kp = (-2.5, 3);
        :>> TRQ_PID_DEFAULT.kd = (0, 0);
        :>> TRQ_PID_DEFAULT.ki = (-3.5, 4);
        :>> TRQ_PID_DEFAULT.maxOutput = (25, 25);
        :>> TRQ_PID_DEFAULT.maxInt = (1.56, 1.56);
        :>> TRQ_PID_DEFAULT.ko = (0, 0);
        :>> TRQ_PID_DEFAULT.stictionUp = (0, 0);
        :>> TRQ_PID_DEFAULT.stictionDown = (0, 0);
        :>> TRQ_PID_DEFAULT.kff = (1, 1);
        :>> TRQ_PID_DEFAULT.viscousPos = (-0.003, 0.0023);
        :>> TRQ_PID_DEFAULT.viscousNeg = (-0.003, 0.0023);
        :>> TRQ_PID_DEFAULT.coulombPos = (0, 0);
        :>> TRQ_PID_DEFAULT.coulombNeg = (0, 0);
        :>> TRQ_PID_DEFAULT.velocityThres = (0, 0);
        :>> TRQ_PID_DEFAULT.filterType = (0, 0);
        :>> TRQ_PID_DEFAULT.ktau = (-0.9, 0.7);
    }
    part right_arm_eb30_j4_6_mc :> motorControl {
    :>> includes = ("../../general.xml", "../../hardware/electronics/right_arm_eb30_j4_6_eln.xml", "../../hardware/mechanicals/right_arm_eb30_j4_6_mec.xml", "./right_arm_eb30_j4_6_mc_service.xml");
    :>> device_type = "embObjMotionControl";
    :>> device_name = "right_arm-eb30-j4_6-mc";
    :>> LIMITS.jntPosMin = (-90, -60, -30);
    :>> LIMITS.jntPosMax = (90, 50, 30);
    :>> LIMITS.jntVelMax = (90, 90, 90);
    :>> LIMITS.motorOverloadCurrents = (350, 350, 350);
    :>> LIMITS.motorNominalCurrents = (200, 200, 200);
    :>> LIMITS.motorPeakCurrents = (200, 200, 200);
    :>> LIMITS.motorPwmLimit = (16000, 16000, 16000);
    :>> TIMEOUTS.velocity = (100, 100, 100);
    :>> IMPEDANCE.stiffness = (0, 0, 0);
    :>> IMPEDANCE.damping = (0, 0, 0);
    :>> CONTROLS.positionControl = ("POS_PID_DEFAULT", "POS_PID_DEFAULT", "POS_PID_DEFAULT");
    :>> CONTROLS.velocityControl = ("POS_PID_DEFAULT", "POS_PID_DEFAULT", "POS_PID_DEFAULT");
    :>> CONTROLS.mixedControl = ("POS_PID_DEFAULT", "POS_PID_DEFAULT", "POS_PID_DEFAULT");
    :>> CONTROLS.torqueControl = ("none", "none", "none");
    :>> CONTROLS.currentPid = ("2FOC_CUR_CONTROL", "2FOC_CUR_CONTROL", "2FOC_CUR_CONTROL");
    :>> CONTROLS.speedPid = ("2FOC_VEL_CONTROL", "2FOC_VEL_CONTROL", "2FOC_VEL_CONTROL");
    :>> POS_PID_DEFAULT.kp = (-50, -50, -50);
    :>> POS_PID_DEFAULT.kd = (-8, -8, -8);
    :>> POS_PID_DEFAULT.ki = (-220, -220, -220);
    :>> POS_PID_DEFAULT.maxOutput = (500, 500, 500);
    :>> POS_PID_DEFAULT.maxInt = (200, 200, 200);
    :>> POS_PID_DEFAULT.stictionUp = (0, 0, 0);
    :>> POS_PID_DEFAULT.stictionDown = (0, 0, 0);
    :>> POS_PID_DEFAULT.kff = (0, 0, 0);
    :>> _2FOC_CUR_CONTROL.kp = (2, 2, 2);
    :>> _2FOC_CUR_CONTROL.kd = (0, 0, 0);
    :>> _2FOC_CUR_CONTROL.ki = (500, 500, 500);
    :>> _2FOC_CUR_CONTROL.shift = (0, 0, 0);
    :>> _2FOC_CUR_CONTROL.maxOutput = (32000, 32000, 32000);
    :>> _2FOC_CUR_CONTROL.maxInt = (32000, 32000, 32000);
    :>> _2FOC_CUR_CONTROL.kff = (0, 0, 0);
    :>> _2FOC_VEL_CONTROL.kff = (0, 0, 0);
    :>> _2FOC_VEL_CONTROL.kp = (12, 12, 12);
    :>> _2FOC_VEL_CONTROL.kd = (0, 0, 0);
    :>> _2FOC_VEL_CONTROL.ki = (16, 16, 16);
    :>> _2FOC_VEL_CONTROL.shift = (10, 10, 10);
    :>> _2FOC_VEL_CONTROL.maxOutput = (32000, 32000, 32000);
    :>> _2FOC_VEL_CONTROL.maxInt = (32000, 32000, 32000);
    }
    part right_arm_eb22_j7_10_mc :> motorControl {
        :>> includes = ("../../general.xml", "../../hardware/electronics/right_arm_eb22_j7_10_eln.xml", "../../hardware/mechanicals/right_arm_eb22_j7_10_mec.xml", "./right_arm_eb22_j7_10_mc_service.xml");
        :>> device_type = "embObjMotionControl";
        :>> device_name = "right_arm-eb22-j7_10-mc";
        :>> LIMITS.jntPosMin = (4, 4, 4, 4);
        :>> LIMITS.jntPosMax = (72, 85, 85, 85);
        :>> LIMITS.jntVelMax = (1000, 1000, 1000, 1000);
        :>> LIMITS.motorOverloadCurrents = (2000, 2000, 2000, 2000);
        :>> LIMITS.motorNominalCurrents = (1100, 1100, 1100, 1100);
        :>> LIMITS.motorPeakCurrents = (1500, 1500, 1500, 1500);
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
        :>> POS_PID_DEFAULT.kp = (-246, -246, -246, -381);
        :>> POS_PID_DEFAULT.kd = (0, 0, 0, 0);
        :>> POS_PID_DEFAULT.ki = (-33, -33, -33, -21);
        :>> POS_PID_DEFAULT.maxOutput = (2700, 2700, 2700, 2700);
        :>> POS_PID_DEFAULT.maxInt = (1000, 1000, 1000, 1000);
        :>> POS_PID_DEFAULT.stictionUp = (0, 0, 0, 0);
        :>> POS_PID_DEFAULT.stictionDown = (0, 0, 0, 0);
        :>> POS_PID_DEFAULT.kff = (0, 0, 0, 0);
    }
    part right_arm_eb24_j11_12_mc :> motorControl {
        :>> includes = ("../../general.xml", "../../hardware/electronics/right_arm_eb24_j11_12_eln.xml", "../../hardware/mechanicals/right_arm_eb24_j11_12_mec.xml", "./right_arm_eb24_j11_12_mc_service.xml");
        :>> device_type = "embObjMotionControl";
        :>> device_name = "right_arm-eb24-j11_12-mc";
        :>> LIMITS.jntPosMin = (0, 7);
        :>> LIMITS.jntPosMax = (85, 18);
        :>> LIMITS.jntVelMax = (1000, 1000);
        :>> LIMITS.motorOverloadCurrents = (2000, 2000);
        :>> LIMITS.motorNominalCurrents = (700, 700);
        :>> LIMITS.motorPeakCurrents = (1500, 1500);
        :>> LIMITS.motorPwmLimit = (3360, 3360);
        :>> TIMEOUTS.velocity = (100, 100);
        :>> IMPEDANCE.stiffness = (0.0, 0.0);
        :>> IMPEDANCE.damping = (0.0, 0.0);
        :>> CONTROLS.positionControl = ("POS_PID_DEFAULT", "POS_PID_DEFAULT");
        :>> CONTROLS.velocityControl = ("POS_PID_DEFAULT", "POS_PID_DEFAULT");
        :>> CONTROLS.mixedControl = ("POS_PID_DEFAULT", "POS_PID_DEFAULT");
        :>> CONTROLS.torqueControl = ("none", "none");
        :>> CONTROLS.currentPid = ("none", "none");
        :>> CONTROLS.speedPid = ("none", "none");
        :>> POS_PID_DEFAULT.kp = (200, 150);
        :>> POS_PID_DEFAULT.kd = (0, 0);
        :>> POS_PID_DEFAULT.ki = (10, 30);
        :>> POS_PID_DEFAULT.maxOutput = (1500, 3360);
        :>> POS_PID_DEFAULT.maxInt = (1000, 1000);
        :>> POS_PID_DEFAULT.stictionUp = (0, 0);
        :>> POS_PID_DEFAULT.stictionDown = (0, 0);
        :>> POS_PID_DEFAULT.kff = (0, 0);
    }
    part right_arm_eb2_j0_1_mc_service :> service {
        :>> SERVICE.type = "eomn_serv_MC_foc";
        :>> SERVICE.PROPERTIES.ETHBOARD.type = "ems4";
        :>> SERVICE.PROPERTIES.CANBOARDS.type = "foc";
        :>> SERVICE.PROPERTIES.CANBOARDS.PROTOCOL.major = 1;
        :>> SERVICE.PROPERTIES.CANBOARDS.PROTOCOL.minor = 6;
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ACTUATOR.type = ("foc", "foc");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ACTUATOR._port = ("CAN1:1:0", "CAN1:2:0");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER1.type = ("amo", "amo");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER1._port = ("CONN:P6", "CONN:P8");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER1.position = ("atjoint", "atjoint");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER1.resolution = (16384, -16384);
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER1.tolerance = (0.703, 0.703);
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER2.type = ("roie", "roie");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER2._port = ("CAN1:1:0", "CAN1:2:0");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER2.position = ("atmotor", "atmotor");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER2.resolution = (14400, 14400);
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER2.tolerance = (3.6, 3.6);
    }
    part right_arm_eb3_j2_3_mc_service :> service {
        :>> SERVICE.type = "eomn_serv_MC_foc";
        :>> SERVICE.PROPERTIES.ETHBOARD.type = "ems4";
        :>> SERVICE.PROPERTIES.CANBOARDS.type = "foc";
        :>> SERVICE.PROPERTIES.CANBOARDS.PROTOCOL.major = 1;
        :>> SERVICE.PROPERTIES.CANBOARDS.PROTOCOL.minor = 6;
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ACTUATOR.type = ("foc", "foc");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ACTUATOR._port = ("CAN1:1:0", "CAN1:2:0");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER1.type = ("amo", "amo");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER1._port = ("CONN:P6", "CONN:P8");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER1.position = ("atjoint", "atjoint");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER1.resolution = (-16384, -16384);
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER1.tolerance = (0.703, 0.703);
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER2.type = ("roie", "roie");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER2._port = ("CAN1:1:0", "CAN1:2:0");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER2.position = ("atmotor", "atmotor");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER2.resolution = (14400, 14400);
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER2.tolerance = (3.6, 3.6);
    }
    part right_arm_eb30_j4_6_mc_service :> service {
        :>> SERVICE.type = "eomn_serv_MC_foc";
        :>> SERVICE.PROPERTIES.ETHBOARD.type = "amc";
        :>> SERVICE.PROPERTIES.CANBOARDS.type = "amcbldc";
        :>> SERVICE.PROPERTIES.CANBOARDS.PROTOCOL.major = 2;
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ACTUATOR.type = ("foc", "foc", "foc");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ACTUATOR._port = ("CAN1:1:0", "CAN1:2:0", "CAN1:3:0");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER1.type = ("aea", "aea", "aea");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER1._port = ("CONN:J5_X1", "CONN:J5_X2", "CONN:J5_X3");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER1.position = ("atjoint", "atjoint", "atjoint");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER1.resolution = (4096, 4096, 4096);
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER1.tolerance = (0.4, 0.4, 0.4);
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER2.type = ("none", "none", "none");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER2._port = ("CAN1:1:0", "CAN1:2:0", "CAN1:3:0");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER2.position = ("atmotor", "atmotor", "atmotor");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER2.resolution = (0, 0, 0);
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER2.tolerance = (0, 0, 0);
    }
    part right_arm_eb22_j7_10_mc_service :> service {
        :>> SERVICE.type = "eomn_serv_MC_mc4plusfaps";
        :>> SERVICE.PROPERTIES.ETHBOARD.type = "mc4plus";
        :>> SERVICE.PROPERTIES.CANBOARDS.type = "mtb4c";
        :>> SERVICE.PROPERTIES.CANBOARDS.PROTOCOL.major = 2;
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ACTUATOR.type = ("pwm", "pwm", "pwm", "pwm");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ACTUATOR._port = ("CONN:P5", "CONN:P4", "CONN:P3", "CONN:P2");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER1.type = ("pos", "pos", "pos", "pos");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER1._port = ("POS:hand_thumb_oc", "POS:hand_index_oc", "POS:hand_middle_oc", "POS:hand_ring_pinky_oc");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER1.position = ("atjoint", "atjoint", "atjoint", "atjoint");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER1.resolution = (65535, 65535, 65535, 65535);
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER1.tolerance = (5, 5, 5, 5);
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER2.type = ("qenc", "qenc", "qenc", "qenc");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER2._port = ("CONN:P5", "CONN:P4", "CONN:P3", "CONN:P2");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER2.position = ("atmotor", "atmotor", "atmotor", "atmotor");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER2.resolution = (1600, 1600, 1600, 1600);
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER2.tolerance = (0, 0, 0, 0);
    }
    part right_arm_eb24_j11_12_mc_service :> service {
        :>> SERVICE.type = "eomn_serv_MC_mc4plusfaps";
        :>> SERVICE.PROPERTIES.ETHBOARD.type = "mc4plus";
        :>> SERVICE.PROPERTIES.CANBOARDS.type = "mtb4c";
        :>> SERVICE.PROPERTIES.CANBOARDS.PROTOCOL.major = 2;
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ACTUATOR.type = ("pwm", "pwm");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ACTUATOR._port = ("CONN:P2", "CONN:P5");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER1.type = ("pos", "pos");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER1._port = ("POS:hand_thumb_add", "POS:hand_index_add");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER1.position = ("atjoint", "atjoint");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER1.resolution = (65535, 65535);
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER1.tolerance = (5, 5);
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER2.type = ("none", "none");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER2._port = ("CONN:P2", "CONN:P5");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER2.position = ("atmotor", "atmotor");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER2.resolution = (-1600, 1600);
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER2.tolerance = (0, 0);
    }
    part right_arm_eb1_j0_1_inertial :> inertial {
        :>> includes = ("../../general.xml", "../../hardware/electronics/right_arm_eb1_j0_1_eln.xml");
        :>> device_name = "right_arm-eb1-j0_1-inertial";
        :>> device_type = "embObjIMU";
        :>> SERVICE.type = "eomn_serv_AS_inertials3";
        :>> SERVICE.PROPERTIES.CANBOARDS.type = "eobrd_strain2";
        :>> SERVICE.PROPERTIES.SENSORS.id = ("r_arm_ft_acc", "r_arm_ft_gyro", "r_arm_ft_mag", "r_arm_ft_eul", "r_arm_ft_status");
        :>> SERVICE.PROPERTIES.SENSORS.sensorName = ("r_arm_ft_imu", "r_arm_ft_imu", "r_arm_ft_imu", "r_arm_ft_imu", "r_arm_ft_imu");
        :>> SERVICE.PROPERTIES.SENSORS.type = ("eoas_imu_acc", "eoas_imu_gyr", "eoas_imu_mag", "eoas_imu_eul", "eoas_imu_status");
        :>> SERVICE.PROPERTIES.SENSORS.boardType = ("strain2", "strain2", "strain2", "strain2", "strain2");
        :>> SERVICE.PROPERTIES.SENSORS.location = ("CAN2:13", "CAN2:13", "CAN2:13", "CAN2:13", "CAN2:13");
        :>> SERVICE.SETTINGS.acquisitionRate = 10;
        :>> SERVICE.SETTINGS.enabledSensors = ("r_arm_ft_acc", "r_arm_ft_gyro", "r_arm_ft_mag", "r_arm_ft_eul", "r_arm_ft_status");
    }
    part right_arm_eb3_j2_3_inertial :> inertial {
        :>> includes = ("../../general.xml", "../../hardware/electronics/right_arm_eb3_j2_3_eln.xml");
        :>> SERVICE.type = "eomn_serv_AS_inertials3";
        :>> SERVICE.PROPERTIES.CANBOARDS.type = "mtb4";
        :>> SERVICE.PROPERTIES.CANBOARDS.PROTOCOL.major = 2;
        :>> SERVICE.PROPERTIES.SENSORS.id = ("IDacc", "IDgyr");
        :>> SERVICE.PROPERTIES.SENSORS.sensorName = ("r_hand_acc", "r_hand_gyro");
        :>> SERVICE.PROPERTIES.SENSORS.type = ("eoas_imu_acc", "eoas_imu_gyr");
        :>> SERVICE.PROPERTIES.SENSORS.boardType = ("mtb4", "mtb4");
        :>> SERVICE.PROPERTIES.SENSORS.location = ("CAN2:2", "CAN2:2");
        :>> SERVICE.SETTINGS.acquisitionRate = 50;
        :>> SERVICE.SETTINGS.enabledSensors = ("IDacc", "IDgyr");
    }
    part right_arm_eb1_j0_1_strain :> ft {
        :>> includes = ("../../general.xml", "../../hardware/electronics/right_arm_eb1_j0_1_eln.xml");
        :>> device_name = "right_arm-eb1-j0_1-strain";
        :>> device_type = "embObjFTsensor";
        :>> SERVICE.PROPERTIES.CANBOARDS.type = "strain2";
        :>> SERVICE.PROPERTIES.CANBOARDS.PROTOCOL.major = 2;
        :>> SERVICE.PROPERTIES.SENSORS.id = "r_arm_ft";
        :>> SERVICE.PROPERTIES.SENSORS.framename = "r_arm_ft";
        :>> SERVICE.PROPERTIES.SENSORS.location = "CAN2:13";
        :>> SERVICE.SETTINGS.enabledSensors = ("r_arm_ft");
    }
    part right_arm_eb24_j4_7_skin :> skin {
        :>> includes = ("../../general.xml", "../../hardware/electronics/right_arm_eb24_j4_7_eln.xml", "./right_arm_eb24_j4_7_skinSpec.xml");
        :>> device_name = "right_arm-eb24-j4_7-skin";
        :>> device_type = "embObjSkin";
        :>> patches.skinCanAddrsPatch1 = (14, 13, 12, 11, 10, 9, 8);
    }
    part right_arm_eb3_j2_3_skinSpec :> skinSpec {
        :>> defaultCfgBoard.skinType = 0;
        :>> defaultCfgTriangle.enabled = false;
        :>> specialCfgTriangles.numOfSets = 2;
    }
    part right_upperarm_eb1_skin :> skin {
        :>> includes = ("../../general.xml", "../../hardware/electronics/right_arm_eb1_j0_1_eln.xml", "./right_upperarm_eb1_skinSpec.xml");
        :>> device_name = "right_upperarm-eb1-skin";
        :>> device_type = "embObjSkin";
        :>> patches.skinCanAddrsPatch1 = (13);
    }
    part right_upperarm_eb2_skinSpec :> skinSpec;

    part right_arm_mc_wrapper :> wrapper {
        :>> folder_name = "wrappers/motorControl/";
        :>> device_name = "right_arm-mc_nws_yarp";
        :>> device_type = "controlBoard_nws_yarp";
        :>> period = 0.001;
        :>> name = "/ergocub/right_arm";
        :>> startup.phase = "startup";
        :>> startup.type = "attach";
        :>> startup.level = 10;
        :>> startup.elementName = "device";
        :>> startup.elementValue = "right_arm-mc_remapper";
        :>> shutdown.phase = "shutdown";
        :>> shutdown.type = "detach";
        :>> shutdown.level = 15;
    }
    part right_arm_mc_remapper :> remapper {
        :>> folder_name = "wrappers/motorControl/";
        :>> device_type = "controlboardremapper";
        :>> device_name = "right_arm-mc_remapper";
        :>> elementName = ("right_arm_joints1", "right_arm_joints2", "right_arm_joints3", "right_arm_joints4", "right_arm_joints5");
        :>> elementValue = ("( 0  1  0  1 )", "( 2  3  0  1 )", "( 4  6  0  2 )", "( 7  10  0  3 )", "( 11  12  0  1 )");
        :>> joints = 13;
        :>> startup.phase = "startup";
        :>> startup.type = "attach";
        :>> startup.level = 5;
        :>> startup.elementName = ("right_arm_joints1", "right_arm_joints2", "right_arm_joints3", "right_arm_joints4");
        :>> startup.elementValue = ("right_arm-eb1-j0_1-mc", "right_arm-eb3-j2_3-mc", "right_arm-eb30-j4_6-mc", "right_arm-eb22-j7_10-mc", "right_arm-eb24-j11_12-mc");
        :>> shutdown.phase = "shutdown";
        :>> shutdown.type = "detach";
        :>> shutdown.level = 20;
    }

    part right_arm_FT_wrapper :> wrapper {
        :>> folder_name = "wrappers/FT/";
        :>> device_name = "right_arm-FT_wrapper";
        :>> device_type = "multipleanalogsensorsserver";
        :>> period = 2;
        :>> name = "/ergocub/right_arm/FT";
        :>> startup.phase = "startup";
        :>> startup.type = "attach";
        :>> startup.level = 5;
        :>> startup.elementName = "FirstStrain";
        :>> startup.elementValue = "right_arm-eb1-j0_1-strain";
        :>> shutdown.phase = "shutdown";
        :>> shutdown.type = "detach";
        :>> shutdown.level = 5;
    }

    part right_arm_imu_wrapper :> wrapper {
        :>> folder_name = "wrappers/inertials/";
        :>> device_name = "right_arm-imu_wrapper";
        :>> device_type = "multipleanalogsensorsserver";
        :>> period = 10;
        :>> name = "/ergocub/right_arm/IMU";
        :>> startup.phase = "startup";
        :>> startup.type = "attach";
        :>> startup.level = 5;
        :>> startup.elementName = "SetOfIMUs";
        :>> startup.elementValue = "right_arm-eb1-j0_1-inertial";
        :>> shutdown.phase = "shutdown";
        :>> shutdown.type = "detach";
        :>> shutdown.level = 5;
    }
}