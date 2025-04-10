part def Head {
    part face_calib :> calibrator {
        :>> type = "parametricCalibratorEth";
        :>> name = "face-calibrator";
        :>> GENERAL.deviceName = "FaceV3_Calibrator";
        :>> CALIBRATION.calibrationType = 12;
        :>> startup.phase = "startup";
        :>> startup.type = "calibrate";
        :>> startup.target = "face-mc_remapper";
        :>> interrupt1.phase = "interrupt1";
        :>> interrupt1.level = 1;
        :>> interrupt1.type = "park";
        :>> interrupt1.target = "face-mc_remapper";
        :>> interrupt3.phase = "interrupt3";
        :>> interrupt3.level = 1;
        :>> interrupt3.type = "abort";
    }
    part head_calib :> calibrator {
        :>> type = "parametricCalibratorEth";
        :>> name = "head-calibrator";
        :>> GENERAL.joints = 6;
        :>> GENERAL.deviceName = "HeadV3_Calibrator";
        :>> HOME.positionHome = (0, 0, 0, 0, 0, 0);
        :>> HOME.velocityHome = (10, 10, 10, 10, 10, 10);
        :>> CALIBRATION.calibrationType = (12, 12, 12, 12, 5, 5);
        :>> CALIB_ORDER = "(0 1 2) (3) (4 5)";
        :>> startup.phase = "startup";
        :>> startup.type = "calibrate";
        :>> startup.target = "head-mc_remapper";
        :>> interrupt1.phase = "interrupt1";
        :>> interrupt1.level = 1;
        :>> interrupt1.type = "park";
        :>> interrupt1.target = "head-mc_remapper";
        :>> interrupt3.phase = "interrupt3";
        :>> interrupt3.level = 1;
        :>> interrupt3.type = "abort";
    }

    part face_eb22_j0_eln :> electronics {
        :>> ETH_BOARD.ETH_BOARD_PROPERTIES.IpAddress = "10.0.1.22";
        :>> ETH_BOARD.ETH_BOARD_SETTINGS.Name = "face-eb22-j0";
    }
    part head_eb20_j0_1_eln :> electronics {
        :>> ETH_BOARD.ETH_BOARD_PROPERTIES.IpAddress = "10.0.1.20";
        :>> ETH_BOARD.ETH_BOARD_SETTINGS.Name = "head-eb20-j0_1";
        :>> ETH_BOARD.ETH_BOARD_SETTINGS.RUNNINGMODE.TXrateOfRegularROPs = 5;
    }
    part head_eb21_j2_5_eln :> electronics {
        :>> ETH_BOARD.ETH_BOARD_PROPERTIES.IpAddress = "10.0.1.21";
        :>> ETH_BOARD.ETH_BOARD_SETTINGS.Name = "head-eb21-j2_5";
        :>> ETH_BOARD.ETH_BOARD_SETTINGS.RUNNINGMODE.TXrateOfRegularROPs = 5;
    }

    part pc104 :> PC104 {
        
    }

    part face_eb22_j0_mec :> mechanicals {
        :>> GENERAL.Joints = 1;
        :>> GENERAL.AxisMap = 0;
        :>> GENERAL.AxisName = "eyelids";
        :>> GENERAL.AxisType = "revolute";
        :>> GENERAL.Encoder = 182.044;
        :>> GENERAL.fullscalePWM = 3360;
        :>> GENERAL.ampsToSensor = 1000.0;
        :>> GENERAL.Gearbox_M2J = -16;
        :>> GENERAL.Gearbox_E2J = 2.38;
        :>> GENERAL.useMotorSpeedFbk = 1;
        :>> GENERAL.MotorType = "DC";
        :>> LIMITS.hardwareJntPosMin = -5;
        :>> LIMITS.hardwareJntPosMax = 65;
        :>> LIMITS.rotorPosMin = 0;
        :>> LIMITS.rotorPosMax = 0;
        :>> JOINTSET_CFG.JOINTSET_0.listofjoints = 0;
    }
    part head_eb20_j0_1_mec :> mechanicals {
        :>> GENERAL.Joints = 2;
        :>> GENERAL.AxisMap = (0, 1);
        :>> GENERAL.AxisName = ("neck_pitch", "neck_roll");
        :>> GENERAL.AxisType = ("revolute", "revolute");
        :>> GENERAL.Encoder = (182.044, 182.044);
        :>> GENERAL.fullscalePWM = (3360, 3360);
        :>> GENERAL.ampsToSensor = (1000.0, 1000.0);
        :>> GENERAL.Gearbox_M2J = (161.68, 161.68);
        :>> GENERAL.Gearbox_E2J = (1, 1);
        :>> GENERAL.useMotorSpeedFbk = (1, 1);
        :>> GENERAL.MotorType = ("DC", "DC");
        :>> LIMITS.hardwareJntPosMin = (-30, -20);
        :>> LIMITS.hardwareJntPosMax = (+22, +20);
        :>> LIMITS.rotorPosMin = (0, 0);
        :>> LIMITS.rotorPosMax = (0, 0);
        :>> JOINTSET_CFG.numberofsets = 1;
        :>> JOINTSET_CFG.JOINTSET_0.listofjoints = (0, 1);
    }
    part head_eb21_j2_5_mec :> mechanicals {
        :>> GENERAL.Joints = 4;
        :>> GENERAL.AxisMap = (0, 1, 2, 3);
        :>> GENERAL.AxisName = ("neck_yaw", "eyes_tilt", "eyes_version", "eyes_vergence");
        :>> GENERAL.AxisType = ("revolute", "revolute", "revolute", "revolute");
        :>> GENERAL.Encoder = (182.044, 182.044, 182.044, 182.044);
        :>> GENERAL.fullscalePWM = (3360, 3360, 3360, 3360);
        :>> GENERAL.ampsToSensor = (1000.0, 1000.0, 1000.0, 1000.0);
        :>> GENERAL.Gearbox_M2J = (100, -141, 50, 50);
        :>> GENERAL.Gearbox_E2J = (1, 1, 1, 1);
        :>> GENERAL.useMotorSpeedFbk = (1, 1, 1, 1);
        :>> GENERAL.MotorType = ("DC", "DC", "DC", "DC");
        :>> LIMITS.hardwareJntPosMin = (-45, -30, -45, 0);
        :>> LIMITS.hardwareJntPosMax = (+45, +30, +45, +45);
        :>> LIMITS.rotorPosMin = (0, 0, 0, 0);
        :>> LIMITS.rotorPosMax = (0, 0, 0, 0);
        :>> JOINTSET_CFG.numberofsets = 3;
        :>> JOINTSET_CFG.JOINTSET_0.listofjoints = (0);
        :>> JOINTSET_CFG.JOINTSET_1.listofjoints = (1);
        :>> JOINTSET_CFG.JOINTSET_2.listofjoints = (2, 3);
    }

    part face_eb22_j0_mc :> motorControl {
        :>> type = "embObjMotionControl";
        :>> name = "face-eb22-j0-mc";
        :>> LIMITS.jntPosMin = -5;
        :>> LIMITS.jntPosMax = +65;
        :>> LIMITS.motorOverloadCurrents = 2000;
        :>> LIMITS.motorNominalCurrents = 700;
        :>> LIMITS.motorPeakCurrents = 1000;
        :>> LIMITS.jntVelMax = 1000;
        :>> LIMITS.motorPwmLimit = 3300;
        :>> TIMEOUTS.velocity = 100;
        :>> IMPEDANCE.stiffness = 0.0;
        :>> IMPEDANCE.damping = 0.0;
        :>> CONTROLS.positionControl = "POS_PID_DEFAULT";
        :>> CONTROLS.velocityControl = "POS_PID_DEFAULT";
        :>> CONTROLS.mixedControl = "POS_PID_DEFAULT";
        :>> CONTROLS.torqueControl = "none";
        :>> CONTROLS.currentPid = "none";
        :>> CONTROLS.speedPid = "none";
        :>> POS_PID_DEFAULT.kp = 600.0;
        :>> POS_PID_DEFAULT.kd = 0.0;
        :>> POS_PID_DEFAULT.ki = 100.0;
        :>> POS_PID_DEFAULT.maxOutput = 3360;
        :>> POS_PID_DEFAULT.maxInt = 3360;
        :>> POS_PID_DEFAULT.stictionUp = 0;
        :>> POS_PID_DEFAULT.stictionDown = 0;
        :>> POS_PID_DEFAULT.kff = 0;
    }
    part head_eb20_j0_1_mc :> motorControl {
        :>> type = "embObjMotionControl";
        :>> name = "head-eb20-j0_1-mc";
        :>> LIMITS.jntPosMax = (+22, +20);
    }
    part head_eb21_j2_5_mc :> motorControl {
        :>> type = "embObjMotionControl";
        :>> name = "head-eb21-j2_5-mc";
        :>> LIMITS.jntPosMin = (-45, -30, -30, 0);
        :>> LIMITS.jntPosMax = (+45, +30, +30, +20);
        :>> LIMITS.jntVelMax = (1000, 1000, 1000, 1000);
        :>> LIMITS.motorOverloadCurrents = (2000, 2000, 2500, 2500);
        :>> LIMITS.motorNominalCurrents = (700, 700, 700, 700);
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
        :>> POS_PID_DEFAULT.kp = (1100.0, -1000, 3500, 4500);
        :>> POS_PID_DEFAULT.kd = (0.0, 0.0, 0.0, 0.0);
        :>> POS_PID_DEFAULT.ki = (0.0, -100, 600.0, 600.0);
        :>> POS_PID_DEFAULT.maxOutput = (3360, 3360, 3360, 3360);
        :>> POS_PID_DEFAULT.maxInt = (3360, 3360, 3360, 3360);
        :>> POS_PID_DEFAULT.stictionUp = (0, 0, 0, 0);
        :>> POS_PID_DEFAULT.stictionDown = (0, 0, 0, 0);
        :>> POS_PID_DEFAULT.kff = (0, 0, 0, 0);
    }

    part face_eb22_j0_mc_service :> service {
        :>> SERVICE.type = "eomn_serv_MC_mc4plus";
        :>> SERVICE.PROPERTIES.ETHBOARD.type = "mc4plus";
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ACTUATOR.type = "pwm";
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ACTUATOR.portName = "CONN:P2";
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER1.portName = "CONN:P10";
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER1.resolution = -4096;
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER2.type = "none";
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER2.portName = "none";
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER2.position = "none";
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER2.resolution = 0;
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER2.tolerance = 0;
    }
    part head_eb20_j0_1_mc_service :> service {
        :>> SERVICE.type = "eomn_serv_MC_mc4plus";
        :>> SERVICE.PROPERTIES.ETHBOARD.type = "mc4plus";
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ACTUATOR.type = ("pwm", "pwm");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ACTUATOR.portName = ("CONN:P3", "CONN:P4");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER1.type = ("aea", "aea");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER1.portName = ("CONN:P11", "CONN:P10");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER1.position = ("atjoint", "atjoint");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER1.resolution = (4096, -4096);
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER1.tolerance = (0.703, 0.703);
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER2.type = ("qenc", "qenc");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER2.portName = ("CONN:P3", "CONN:P4");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER2.position = ("atmotor", "atmotor");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER2.resolution = (2048, 2048);
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER2.tolerance = (0, 0);
    }
    part head_eb21_j2_5_mc_service :> service {
        :>> SERVICE.type = "eomn_serv_MC_mc4plus";
        :>> SERVICE.PROPERTIES.ETHBOARD.type = "mc4plus";
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ACTUATOR.type = ("pwm", "pwm", "pwm", "pwm");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ACTUATOR.portName = ("CONN:P3", "CONN:P2", "CONN:P5", "CONN:P4");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER1.type = ("aea", "aea", "aea", "aea");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER1.portName = ("CONN:P11", "CONN:P10", "CONN:none", "CONN:none");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER1.position = ("atjoint", "atjoint", "none", "none");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER1.resolution = (4096, 4096, 0, 0);
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER1.tolerance = (0.703, 0.703, 0, 0);
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER2.type = ("qenc", "qenc", "qenc", "qenc");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER2.portName = ("CONN:P3", "CONN:P2", "CONN:P5", "CONN:P4");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER2.position = ("atmotor", "atmotor", "atmotor", "atmotor");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER2.resolution = (2048, 2048, 2048, 2048);
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER2.tolerance = (0, 0, 0, 0);
    }
    part head_inertial :> inertial {
        :>> name = "head-inertial";
        :>> type = "embObjIMU";
        :>> SERVICE.type = "eomn_serv_AS_inertials3";
        :>> SERVICE.PROPERTIES.CANBOARDS.type = "rfe";
        :>> SERVICE.PROPERTIES.CANBOARDS.PROTOCOL.major = 2;
        :>> SERVICE.PROPERTIES.SENSORS.id = ("rfeimu_acc", "rfeimu_gyro", "rfeimu_mag", "rfeimu_eul", "rfeimu_status");
        :>> SERVICE.PROPERTIES.SENSORS.sensorName = ("head_imu_0", "head_imu_0", "head_imu_0", "head_imu_0", "head_imu_0");
        :>> SERVICE.PROPERTIES.SENSORS.type = ("eoas_imu_acc", "eoas_imu_gyr", "eoas_imu_mag", "eoas_imu_eul", "eoas_imu_status");
        :>> SERVICE.PROPERTIES.SENSORS.boardType = ("rfe", "rfe", "rfe", "rfe", "rfe");
        :>> SERVICE.PROPERTIES.SENSORS.location = ("CAN1:1", "CAN1:1", "CAN1:1", "CAN1:1", "CAN1:1");
        :>> SERVICE.PROPERTIES.SETTINGS.acquisitionRate = 10;
        :>> SERVICE.PROPERTIES.SETTINGS.enabledSensors = ("rfeimu_acc", "rfeimu_gyro", "rfeimu_mag", "rfeimu_eul", "rfeimu_status");
    }
}