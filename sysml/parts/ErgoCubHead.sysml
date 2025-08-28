part def ErgoCubHead {
    part head_calib :> calibrator {
        :>> device_type = "parametricCalibratorEth";
        :>> device_name = "head-calibrator";
        :>> GENERAL.joints = 4;
        :>> GENERAL.deviceName = "HeadV3_Calibrator";
        :>> HOME.positionHome = (15, 0, 0, 0);
        :>> HOME.velocityHome = (10, 10, 10, 10);
        :>> CALIBRATION.calibrationType = (12, 12, 12, 12);
        :>> CALIB_ORDER = "(0 1 2) (3)";
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
    part head_eb20_j0_1_eln :> electronics {
        :>> ETH_BOARD.ETH_BOARD_PROPERTIES.IpAddress = "10.0.1.20";
        :>> ETH_BOARD.ETH_BOARD_SETTINGS.Name = "head-eb20-j0_1";
        :>> ETH_BOARD.ETH_BOARD_SETTINGS.RUNNINGMODE.TXrateOfRegularROPs = 1;
    }
    part head_eb21_j2_3_eln :> electronics {
        :>> ETH_BOARD.ETH_BOARD_PROPERTIES.IpAddress = "10.0.1.21";
        :>> ETH_BOARD.ETH_BOARD_SETTINGS.Name = "head-eb21-j2_3";
        :>> ETH_BOARD.ETH_BOARD_SETTINGS.RUNNINGMODE.TXrateOfRegularROPs = 1;
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
        :>> LIMITS.hardwareJntPosMin = (-45, -20);
        :>> LIMITS.hardwareJntPosMax = (+22, +20);
        :>> LIMITS.rotorPosMin = (0, 0);
        :>> LIMITS.rotorPosMax = (0, 0);
        :>> COUPLINGS.matrixJ2M = (1.000, 1.000, 0.000, 0.000,
        -1.000, 1.000, 0.000, 0.000,
        0.000, 0.000, 1.000, 0.000,
        0.000, 0.000, 0.000, 1.000);
        :>> COUPLINGS.matrixM2J = (0.500, -0.500, 0.000, 0.000,
        0.500, 0.500, 0.000, 0.000,
        0.000, 0.000, 1.000, 0.000,
        0.000, 0.000, 0.000, 1.000);
        :>> JOINTSET_CFG.numberofsets = 1;
        :>> JOINTSET_CFG.JOINTSET_0.listofjoints = (0, 1);
    }
    part head_eb21_j2_3_mec :> mechanicals {
        :>> GENERAL.Joints = 2;
        :>> GENERAL.AxisMap = (0, 1);
        :>> GENERAL.AxisName = ("neck_yaw", "camera_tilt");
        :>> GENERAL.AxisType = ("revolute", "revolute");
        :>> GENERAL.Encoder = (182.044, 182.044);
        :>> GENERAL.fullscalePWM = (3360, 3360);
        :>> GENERAL.ampsToSensor = (1000.0, 1000.0);
        :>> GENERAL.Gearbox_M2J = (100, -141);
        :>> GENERAL.Gearbox_E2J = (1, 1);
        :>> GENERAL.useMotorSpeedFbk = (1, 1);
        :>> GENERAL.MotorType = ("DC", "DC");
        :>> LIMITS.hardwareJntPosMin = (-45, -30);
        :>> LIMITS.hardwareJntPosMax = (+45, +30);
        :>> LIMITS.rotorPosMin = (0, 0);
        :>> LIMITS.rotorPosMax = (0, 0);
        :>> COUPLINGS.matrixJ2M = (1.000, 0.000, 0.000, 0.000,
        0.000, 1.000, 0.000, 0.000,
        0.000, 0.000, 1.000, 0.000,
        0.000, 0.000, 0.000, 1.000);
        :>> COUPLINGS.matrixM2J = (1.000, 0.000, 0.000, 0.000,
        0.000, 1.000, 0.000, 0.000,
        0.000, 0.000, 1.000, 0.000,
        0.000, 0.000, 0.000, 1.000);
        :>> JOINTSET_CFG.numberofsets = 2;
        :>> JOINTSET_CFG.JOINTSET_0.listofjoints = (0);
        :>> JOINTSET_CFG.JOINTSET_1.listofjoints = (1);
    }
    part head_eb20_j0_1_mc :> motorControl {
        :>> includes = ("../../general.xml", "../../hardware/electronics/head_eb20_j0_1_eln.xml", "../../hardware/mechanicals/head_eb20_j0_1_mec.xml", "./head_eb20_j0_1_mc_service.xml");
        :>> device_type = "embObjMotionControl";
        :>> device_name = "head-eb20-j0_1-mc";
        :>> LIMITS.jntPosMax = (+22, +20);
        :>> LIMITS.jntPosMin = (-40, -20);
        :>> LIMITS.motorNominalCurrents = (2000, 2000);
        :>> POS_PID_DEFAULT.kp = (-180, +178);
        :>> POS_PID_DEFAULT.kd = (-5.39, +4.46);
        :>> POS_PID_DEFAULT.ki = (-507, +514);
    }
    part head_eb21_j2_3_mc :> motorControl {
        :>> includes = ("../../general.xml", "../../hardware/electronics/head_eb21_j2_3_eln.xml", "../../hardware/mechanicals/head_eb21_j2_3_mec.xml", "./head_eb21_j2_3_mc_service.xml");
        :>> device_type = "embObjMotionControl";
        :>> device_name = "head-eb21-j2_3-mc";
        :>> LIMITS.jntPosMin = (-45, -30);
        :>> LIMITS.jntPosMax = (+45, +30);
        :>> LIMITS.motorOverloadCurrents = (2000, 2000);
        :>> LIMITS.motorNominalCurrents = (700, 700);
        :>> LIMITS.motorPeakCurrents = (1500, 1500);
        :>> POS_PID_DEFAULT.kp = (1100.0, 557);
        :>> POS_PID_DEFAULT.kd = (0.0, 0.0);
        :>> POS_PID_DEFAULT.ki = (0.0, 2798);
    }
    part head_eb20_j0_1_mc_service :> service {
        :>> SERVICE.type = "eomn_serv_MC_mc4plus";
        :>> SERVICE.PROPERTIES.ETHBOARD.type = "mc4plus";
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ACTUATOR.type = ("pwm", "pwm");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ACTUATOR._port = ("CONN:P3", "CONN:P4");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER1.type = ("aea", "aea");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER1._port = ("CONN:P11", "CONN:P10");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER1.position = ("atjoint", "atjoint");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER1.resolution = (4096, -4096);
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER1.tolerance = (0.703, 0.703);
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER2.type = ("qenc", "qenc");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER2._port = ("CONN:P3", "CONN:P4");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER2.position = ("atmotor", "atmotor");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER2.resolution = (2048, 2048);
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER2.tolerance = (0, 0);
    }
    part head_eb21_j2_3_mc_service :> service {
        :>> SERVICE.type = "eomn_serv_MC_mc4plus";
        :>> SERVICE.PROPERTIES.ETHBOARD.type = "mc4plus";
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ACTUATOR.type = ("pwm", "pwm");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ACTUATOR._port = ("CONN:P3", "CONN:P4");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER1.type = ("aea", "aea");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER1._port = ("CONN:P11", "CONN:P10");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER1.position = ("atjoint", "atjoint");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER1.resolution = (4096, 4096);
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER1.tolerance = (0.703, 0.703);
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER2.type = ("qenc", "qenc");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER2._port = ("CONN:P3", "CONN:P4");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER2.position = ("atmotor", "atmotor");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER2.resolution = (2048, 2048);
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER2.tolerance = (0, 0);
    }
    part head_inertial :> inertial {
        :>> includes = ("../../general.xml", "../../hardware/electronics/head_eb21_j2_3_eln.xml");
        :>> device_name = "head-inertial";
        :>> device_type = "embObjIMU";
        :>> SERVICE.type = "eomn_serv_AS_inertials3";
        :>> SERVICE.PROPERTIES.CANBOARDS.type = "rfe";
        :>> SERVICE.PROPERTIES.CANBOARDS.PROTOCOL.major = 2;
        :>> SERVICE.PROPERTIES.SENSORS.id = ("rfeimu_acc", "rfeimu_gyro", "rfeimu_mag", "rfeimu_eul", "rfeimu_status");
        :>> SERVICE.PROPERTIES.SENSORS.sensorName = ("head_imu_0", "head_imu_0", "head_imu_0", "head_imu_0", "head_imu_0");
        :>> SERVICE.PROPERTIES.SENSORS.type = ("eoas_imu_acc", "eoas_imu_gyr", "eoas_imu_mag", "eoas_imu_eul", "eoas_imu_status");
        :>> SERVICE.PROPERTIES.SENSORS.boardType = ("rfe", "rfe", "rfe", "rfe", "rfe");
        :>> SERVICE.PROPERTIES.SENSORS.location = ("CAN1:1", "CAN1:1", "CAN1:1", "CAN1:1", "CAN1:1");
        :>> SERVICE.SETTINGS.acquisitionRate = 10;
        :>> SERVICE.SETTINGS.enabledSensors = ("rfeimu_acc", "rfeimu_gyro", "rfeimu_mag", "rfeimu_eul", "rfeimu_status");
    }
    part realsense1 :> realsense {
        :>> folder_name = "sensors/";
        :>> device_type = "realsense2";
        :>> device_name = "realsense2dev";
        :>> SETTINGS.alignmentFrame = "RGB";
        :>> HW_DESCRIPTION.clipPlanes = (0.2, 10.0);
    }
    part head_mc_wrapper :> wrapper {
        :>> folder_name = "wrappers/motorControl/";
        :>> device_name = "head-mc_nws_yarp";
        :>> device_type = "controlBoard_nws_yarp";
        :>> period = 0.01;
        :>> name = "/ergocub/head";
        :>> startup.phase = "startup";
        :>> startup.type = "attach";
        :>> startup.level = 10;
        :>> startup.elementName = "device";
        :>> startup.elementValue = ("head-mc_remapper");
        :>> shutdown.phase = "shutdown";
        :>> shutdown.type = "detach";
        :>> shutdown.level = 15;
    }
    part head_mc_remapper :> remapper {
        :>> folder_name = "wrappers/motorControl/";
        :>> device_type = "controlboardremapper";
        :>> device_name = "head-mc_remapper";
        :>> elementName = ("head_joints1", "head_joints2");
        :>> elementValue = ("( 0  1  0  1 )", "( 2  3  0  1 )");
        :>> joints = 6;
        :>> startup.phase = "startup";
        :>> startup.type = "attach";
        :>> startup.level = 5;
        :>> startup.elementName = ("head_joints1", "head_joints2");
        :>> startup.elementValue = ("head-eb20-j0_1-mc", "head-eb21-j2_3-mc");
        :>> shutdown.phase = "shutdown";
        :>> shutdown.type = "detach";
        :>> shutdown.level = 20;
    }
    part realsense_nws_yarp :> wrapper {
        :>> folder_name = "wrappers/camera/";
        :>> device_name = "RGBDWrapperyarp";
        :>> device_type = "rgbdSensor_nws_yarp";
        :>> period = 0.03;
        :>> name = "/depthCamera";
        :>> startup.phase = "startup";
        :>> startup.type = "attach";
        :>> startup.level = 10;
        :>> startup.elementName = "subdevicergbd";
        :>> startup.elementValue = ("realsenseD450");
        :>> shutdown.phase = "shutdown";
        :>> shutdown.type = "detach";
        :>> shutdown.level = 13;
    }
    part head_inertials_wrapper :> wrapper {
        :>> folder_name = "wrappers/inertials/";
        :>> device_name = "head-inertials_wrapper";
        :>> device_type = "multipleanalogsensorsserver";
        :>> period = 10;
        :>> name = "/ergocub/head/inertials";
        :>> startup.phase = "startup";
        :>> startup.type = "attach";
        :>> startup.level = 5;
        :>> startup.elementName = "SetOfIMUs";
        :>> startup.elementValue = ("head-inertial");
        :>> shutdown.phase = "shutdown";
        :>> shutdown.type = "detach";
        :>> shutdown.level = 5;
    }
}