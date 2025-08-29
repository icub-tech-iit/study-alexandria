part def ErgoCubTorso {
    part torso_calib :> calibrator {
        :>> device_type = "parametricCalibratorEth";
        :>> device_name = "torso-calibrator";
        :>> GENERAL.joints = 3;
        :>> GENERAL.deviceName = "Torso_Calibrator";
        :>> HOME.positionHome = (0, -20, 0);
        :>> HOME.velocityHome = (10, 10, 10);
        :>> CALIBRATION.calibrationType = (10, 10, 10);
        :>> CALIB_ORDER = "(2) (0)";
        :>> startup.phase = "startup";
        :>> startup.type = "calibrate";
        :>> startup.target = "torso-torso-eb5-j0_2-mc";
        :>> interrupt1.phase = "interrupt1";
        :>> interrupt1.level = 1;
        :>> interrupt1.type = "park";
        :>> interrupt1.target = "torso-torso-eb5-j0_2-mc";
        :>> interrupt3.phase = "interrupt3";
        :>> interrupt3.level = 1;
        :>> interrupt3.type = "abort";
    }
        part torso_eb5_j0_2_eln :> electronics {
        :>> ETH_BOARD.ETH_BOARD_PROPERTIES.IpAddress = "10.0.1.5";
        :>> ETH_BOARD.ETH_BOARD_PROPERTIES.Type = "ems4";
        :>> ETH_BOARD.ETH_BOARD_SETTINGS.Name = "torso-eb5-j0_2";
        :>> ETH_BOARD.ETH_BOARD_SETTINGS.RUNNINGMODE.TXrateOfRegularROPs = 1;
    }
        part torso_eb5_j0_2_mec :> mechanicals {
        :>> GENERAL.Joints = 3;
        :>> GENERAL.AxisMap = (2, 0, 1);
        :>> GENERAL.AxisName = ("torso_roll", "torso_pitch", "torso_yaw");
        :>> GENERAL.AxisType = ("revolute", "revolute", "revolute");
        :>> GENERAL.Encoder = (182.044, 182.044, 182.044);
        :>> GENERAL.fullscalePWM = (32000, 32000, 32000);
        :>> GENERAL.ampsToSensor = (1000.0, 1000.0, 1000.0);
        :>> GENERAL.Gearbox_M2J = (100.0, 160.0, -100.0);
        :>> GENERAL.Gearbox_E2J = (64, 64, 64);
        :>> GENERAL.useMotorSpeedFbk = (1, 1, 1);
        :>> GENERAL.MotorType = ("MOOG_C2900576", "MOOG_C2900576", "MOOG_C2900576");
        :>> LIMITS.hardwareJntPosMin = (-25, -20, -45);
        :>> LIMITS.hardwareJntPosMax = (25, 65, 45);
        :>> LIMITS.rotorPosMin = (0, 0, 0);
        :>> LIMITS.rotorPosMax = (0, 0, 0);
        :>> _2FOC.HasHallSensor = (1, 1, 1);
        :>> _2FOC.HasTempSensor = (0, 0, 0);
        :>> _2FOC.HasRotorEncoder = (1, 1, 1);
        :>> _2FOC.HasRotorEncoderIndex = (1, 1, 1);
        :>> _2FOC.HasSpeedEncoder = (0, 0, 0);
        :>> _2FOC.RotorIndexOffset = (66, 85, 228);
        :>> _2FOC.MotorPoles = (8, 8, 8);
        :>> JOINTSET_CFG.numberofsets = 3;
        :>> JOINTSET_CFG.JOINTSET_0.listofjoints = (0);
        :>> JOINTSET_CFG.JOINTSET_1.listofjoints = (1);
        :>> JOINTSET_CFG.JOINTSET_2.listofjoints = (2);
    }
    part torso_eb5_j0_2_mc :> motorControl {
        :>> includes = ("../../general.xml", "../../hardware/electronics/torso_eb5_j0_2_eln.xml", "../../hardware/mechanicals/torso_eb5_j0_2_mec.xml", "./torso_eb5_j0_2_mc_service.xml");
        :>> device_type = "embObjMotionControl";
        :>> device_name = "torso-eb5-j0_2-mc";
        :>> LIMITS.jntPosMin = (-23, -18, -43);
        :>> LIMITS.jntPosMax = (23, 45, 43);
        :>> LIMITS.jntVelMax = (120, 120, 120);
        :>> LIMITS.motorOverloadCurrents = (18000, 18000, 18000);
        :>> LIMITS.motorNominalCurrents = (13770, 16000, 15000);
        :>> LIMITS.motorPeakCurrents = (14000, 16000, 15000);
        :>> LIMITS.motorPwmLimit = (16000, 16000, 16000);
        :>> TIMEOUTS.velocity = (100, 100, 100);
        :>> IMPEDANCE.stiffness = (0.0, 0.0, 0.0);
        :>> IMPEDANCE.damping = (0.0, 0.0, 0.0);
        :>> CONTROLS.positionControl = ("POS_PID_DEFAULT", "POS_PID_DEFAULT", "POS_PID_DEFAULT");
        :>> CONTROLS.velocityControl = ("POS_PID_DEFAULT", "POS_PID_DEFAULT", "POS_PID_DEFAULT");
        :>> CONTROLS.mixedControl = ("POS_PID_DEFAULT", "POS_PID_DEFAULT", "POS_PID_DEFAULT");
        :>> CONTROLS.torqueControl = ("TRQ_PID_DEFAULT", "TRQ_PID_DEFAULT", "TRQ_PID_DEFAULT");
        :>> CONTROLS.currentPid = ("2FOC_CUR_CONTROL", "2FOC_CUR_CONTROL", "2FOC_CUR_CONTROL");
        :>> CONTROLS.speedPid = ("2FOC_VEL_CONTROL", "2FOC_VEL_CONTROL", "2FOC_VEL_CONTROL");
        :>> POS_PID_DEFAULT.kp = (10000, 10000, -1500);
        :>> POS_PID_DEFAULT.kd = (0.0, 0.0, 0.0);
        :>> POS_PID_DEFAULT.ki = (8000, 5000, -1000);
        :>> POS_PID_DEFAULT.maxOutput = (10000, 10000, 8000);
        :>> POS_PID_DEFAULT.maxInt = (10000, 5000, 1000);
        :>> POS_PID_DEFAULT.stictionUp = (0, 0, 0);
        :>> POS_PID_DEFAULT.stictionDown = (0, 0, 0);
        :>> POS_PID_DEFAULT.kff = (0, 0, 0);
        :>> TRQ_PID_DEFAULT.kp = (0, 0, 0);
        :>> TRQ_PID_DEFAULT.kd = (0.0, 0.0, 0.0);
        :>> TRQ_PID_DEFAULT.ki = (0.0, 0.0, 0.0);
        :>> TRQ_PID_DEFAULT.maxOutput = (25, 25, 25);
        :>> TRQ_PID_DEFAULT.maxInt = (1.56, 1.56, 1.56);
        :>> TRQ_PID_DEFAULT.ko = (0, 0, 0);
        :>> TRQ_PID_DEFAULT.stictionUp = (0, 0, 0);
        :>> TRQ_PID_DEFAULT.stictionDown = (0, 0, 0);
        :>> TRQ_PID_DEFAULT.kff = (1, 1, 1);
        :>> TRQ_PID_DEFAULT.viscousPos = (0.0016, 0.003, -0.003);
        :>> TRQ_PID_DEFAULT.viscousNeg = (0.0016, 0.003, -0.003);
        :>> TRQ_PID_DEFAULT.coulombPos = (0, 0, 0);
        :>> TRQ_PID_DEFAULT.coulombNeg = (0, 0, 0);
        :>> TRQ_PID_DEFAULT.velocityThres = (0, 0, 0);
        :>> TRQ_PID_DEFAULT.filterType = (0, 0, 0);
        :>> TRQ_PID_DEFAULT.ktau = (0.63, 0.63, 0.63);
        :>> _2FOC_CUR_CONTROL.kp = (8, 8, 8);
        :>> _2FOC_CUR_CONTROL.kd = (0.0, 0.0, 0.0);
        :>> _2FOC_CUR_CONTROL.ki = (2, 2, 2);
        :>> _2FOC_CUR_CONTROL.shift = (10, 10, 10);
        :>> _2FOC_CUR_CONTROL.maxOutput = (32000, 32000, 32000);
        :>> _2FOC_CUR_CONTROL.maxInt = (32000, 32000, 32000);
        :>> _2FOC_CUR_CONTROL.kff = (0, 0, 0);
        :>> _2FOC_VEL_CONTROL.kp = (12, 12, 12);
        :>> _2FOC_VEL_CONTROL.kd = (0.0, 0.0, 0.0);
        :>> _2FOC_VEL_CONTROL.ki = (16, 16, 16);
        :>> _2FOC_VEL_CONTROL.shift = (10, 10, 10);
        :>> _2FOC_VEL_CONTROL.maxOutput = (32000, 32000, 32000);
        :>> _2FOC_VEL_CONTROL.maxInt = (32000, 32000, 32000);
        :>> _2FOC_VEL_CONTROL.kff = (0, 0, 0);
    }
    part torso_eb5_j0_2_mc_service :> service {
        :>> SERVICE.type = "eomn_serv_MC_foc";
        :>> SERVICE.PROPERTIES.ETHBOARD.type = "ems4";
        :>> SERVICE.PROPERTIES.CANBOARDS.type = "foc";
        :>> SERVICE.PROPERTIES.CANBOARDS.PROTOCOL.major = 1;
        :>> SERVICE.PROPERTIES.CANBOARDS.PROTOCOL.minor = 6;
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ACTUATOR.type = ("eomc_act_foc", "eomc_act_foc", "eomc_act_foc");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ACTUATOR._port = ("CAN1:2:0", "CAN1:3:0", "CAN1:1:0");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER1.type = ("amo", "amo", "amo");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER1._port = ("CONN:P7", "CONN:P8", "CONN:P6");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER1.position = ("atjoint", "atjoint", "atjoint");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER1.resolution = (16384, 16384, 16384);
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER1.tolerance = (0.703, 0.703, 0.703);
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER2.type = ("roie", "roie", "roie");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER2._port = ("CAN1:2:0", "CAN1:3:0", "CAN1:1:0");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER2.position = ("atmotor", "atmotor", "atmotor");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER2.resolution = (14400, 14400, 14400);
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER2.tolerance = (3.6, 3.6, 3.6);
    }
    part torso_eb22_skin :> skin {
        :>> includes = ("../../general.xml", "./torso_eb22_skinSpec.xml");
        :>> device_name = "torso-eb22-skin";
        :>> device_type = "embObjSkin";
        :>> patches.skinCanAddrsPatch1 = (7, 8, 9, 10);
    }
    part torso_eb22_skinSpec :> skinSpec {
        :>> defaultCfgBoard.skinType = 0;
    }

    part torso_mc_wrapper :> wrapper {
        :>> folder_name = "wrappers/motorControl/";
        :>> device_name = "torso-mc_nws_yarp";
        :>> device_type = "controlBoard_nws_yarp";
        :>> period = 0.001;
        :>> name = "/ergocub/torso";
        :>> startup.phase = "startup";
        :>> startup.type = "attach";
        :>> startup.level = 10;
        :>> startup.elementName = "device";
        :>> startup.elementValue = "torso-mc_remapper";
        :>> shutdown.phase = "shutdown";
        :>> shutdown.type = "detach";
        :>> shutdown.level = 15;
    }
    part torso_mc_remapper :> remapper {
        :>> folder_name = "wrappers/motorControl/";
        :>> device_type = "controlboardremapper";
        :>> device_name = "torso-mc_remapper";
        :>> elementName = "torso_joints";
        :>> elementValue = ("( 0  2  0  2 )");
        :>> joints = 3;
        :>> startup.phase = "startup";
        :>> startup.type = "attach";
        :>> startup.level = 5;
        :>> startup.elementName = "torso_joints";
        :>> startup.elementValue = ("torso-eb5-j0_2-mc");
        :>> shutdown.phase = "shutdown";
        :>> shutdown.type = "detach";
        :>> shutdown.level = 20;
    }
}