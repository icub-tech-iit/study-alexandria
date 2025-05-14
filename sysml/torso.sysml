part def Torso {
    part torso_calib :> calibrator {
        :>> type = "parametricCalibratorEth";
        :>> name = "torso-calibrator";
        :>> GENERAL.joints = 3;
        :>> GENERAL.deviceName = "Torso_Calibrator";
        :>> HOME.positionHome = (0, 0, -20);
        :>> HOME.velocityHome = (10, 10, 10);
        :>> CALIBRATION.calibrationType = (12, 12, 12);
        :>> CALIB_ORDER = "(0 1 2)";
        :>> startup.phase = "startup";
        :>> startup.type = "calibrate";
        :>> startup.target = "torso-mc_remapper";
        :>> interrupt1.phase = "interrupt1";
        :>> interrupt1.level = 1;
        :>> interrupt1.type = "park";
        :>> interrupt1.target = "torso-mc_remapper";
        :>> interrupt3.phase = "interrupt3";
        :>> interrupt3.level = 1;
        :>> interrupt3.type = "abort";
    }
        part torso_eb5_j0_2_eln :> electronics {
        :>> ETH_BOARD.ETH_BOARD_PROPERTIES.IpAddress = "10.0.1.5";
        :>> ETH_BOARD.ETH_BOARD_PROPERTIES.Type = "ems4";
        :>> ETH_BOARD.ETH_BOARD_SETTINGS.Name = "torso-eb5-j0_2";
        :>> ETH_BOARD.ETH_BOARD_SETTINGS.RUNNINGMODE.TXrateOfRegularROPs = 5;
    }
        part torso_eb5_j0_2_mec :> mechanicals {
        :>> GENERAL.Joints = 3;
        :>> GENERAL.AxisMap = (0, 1, 2);
        :>> GENERAL.AxisName = ("torso_roll", "torso_pitch", "torso_yaw");
        :>> GENERAL.AxisType = ("revolute", "revolute", "revolute");
        :>> GENERAL.Encoder = (182.044, 182.044, 182.044);
        :>> GENERAL.fullscalePWM = (32000, 32000, 32000);
        :>> GENERAL.ampsToSensor = (1000.0, 1000.0, 1000.0);
        :>> GENERAL.Gearbox_M2J = (-100.0, -100.0, -100.0);
        :>> GENERAL.Gearbox_E2J = (1, 1, 1);
        :>> GENERAL.useMotorSpeedFbk = (1, 1, 1);
        :>> GENERAL.MotorType = ("BLL_MOOG", "BLL_MOOG", "BLL_MOOG");
        :>> LIMITS.hardwareJntPosMin = (-30, -20, -50);
        :>> LIMITS.hardwareJntPosMax = (30, 70, 50);
        :>> LIMITS.rotorPosMin = (0, 0, 0);
        :>> LIMITS.rotorPosMax = (0, 0, 0);
        :>> _2FOC.HasHallSensor = (1, 1, 1);
        :>> _2FOC.HasTempSensor = (0, 0, 0);
        :>> _2FOC.HasRotorEncoder = (1, 1, 1);
        :>> _2FOC.HasRotorEncoderIndex = (0, 0, 0);
        :>> _2FOC.HasSpeedEncoder = (0, 0, 0);
        :>> _2FOC.RotorIndexOffset = (0, 0, 0);
        :>> _2FOC.MotorPoles = (8, 8, 8);
        :>> COUPLINGS.matrixJ2M = (0.500, -0.500, 0.000, 0.000,
        0.500, 0.500, 0.000, 0.000,
        0.000, 0.000, 1.000, 0.000,
        0.000, 0.000, 0.000, 1.000);
        :>> COUPLINGS.matrixM2J = (0.500, 0.500, 0.000, 0.000,
        -0.500, 0.500, 0.000, 0.000,
        0.275, 0.275, 0.550, 0.000,
        0.000, 0.000, 0.000, 1.000);
        :>> JOINTSET_CFG.JOINTSET_0.listofjoints = (0, 1, 2);
    }
    part torso_eb5_j0_2_mc :> motorControl {
        :>> includes = ("../../general.xml", "../../hardware/electronics/torso_eb5_j0_2_eln.xml", "../../hardware/mechanicals/torso_eb5_j0_2_mec.xml", "./torso_eb5_j0_2_mc_service.xml");
        :>> type = "embObjMotionControl";
        :>> name = "torso-eb5-j0_2-mc";
        :>> LIMITS.jntPosMin = (-50, -30, -20);
        :>> LIMITS.jntPosMax = (50, 30, 70);
        :>> LIMITS.jntVelMax = (1000, 1000, 1000);
        :>> LIMITS.motorOverloadCurrents = (15000, 15000, 15000);
        :>> LIMITS.motorNominalCurrents = (4000, 4000, 4000);
        :>> LIMITS.motorPeakCurrents = (5000, 5000, 5000);
        :>> LIMITS.motorPwmLimit = (10000, 10000, 10000);
        :>> TIMEOUTS.velocity = (100, 100, 100);
        :>> IMPEDANCE.stiffness = (0.0, 0.0, 0.0);
        :>> IMPEDANCE.damping = (0.0, 0.0, 0.0);
        :>> CONTROLS.positionControl = ("POS_PID_DEFAULT", "POS_PID_DEFAULT", "POS_PID_DEFAULT");
        :>> CONTROLS.velocityControl = ("POS_PID_DEFAULT", "POS_PID_DEFAULT", "POS_PID_DEFAULT");
        :>> CONTROLS.mixedControl = ("POS_PID_DEFAULT", "POS_PID_DEFAULT", "POS_PID_DEFAULT");
        :>> CONTROLS.torqueControl = ("TRQ_PID_DEFAULT", "TRQ_PID_DEFAULT", "TRQ_PID_DEFAULT");
        :>> CONTROLS.currentPid = ("2FOC_CUR_CONTROL", "2FOC_CUR_CONTROL", "2FOC_CUR_CONTROL");
        :>> CONTROLS.speedPid = ("2FOC_VEL_CONTROL", "2FOC_VEL_CONTROL", "2FOC_VEL_CONTROL");
        :>> POS_PID_DEFAULT.kp = (-711.11, -1066.66, -1066.66);
        :>> POS_PID_DEFAULT.kd = (0.0, 0.0, 0.0);
        :>> POS_PID_DEFAULT.ki = (-7111.09, -10666.64, -14222.18);
        :>> POS_PID_DEFAULT.maxOutput = (8000, 8000, 16000);
        :>> POS_PID_DEFAULT.maxInt = (750, 1000, 1000);
        :>> POS_PID_DEFAULT.stictionUp = (0, 0, 0);
        :>> POS_PID_DEFAULT.stictionDown = (0, 0, 0);
        :>> POS_PID_DEFAULT.kff = (0, 0, 0);
        :>> TRQ_PID_DEFAULT.kp = (-450, -400, -400);
        :>> TRQ_PID_DEFAULT.kd = (0.0, 0.0, 0.0);
        :>> TRQ_PID_DEFAULT.ki = (0.0, 0.0, 0.0);
        :>> TRQ_PID_DEFAULT.maxOutput = (8000, 8000, 8000);
        :>> TRQ_PID_DEFAULT.maxInt = (500, 500, 500);
        :>> TRQ_PID_DEFAULT.ko = (0, 0, 0);
        :>> TRQ_PID_DEFAULT.stictionUp = (0, 0, 0);
        :>> TRQ_PID_DEFAULT.stictionDown = (-2, -2, -2);
        :>> TRQ_PID_DEFAULT.kff = (1, 1, 1);
        :>> TRQ_PID_DEFAULT.viscousPos = (-0.0016, -0.003, -0.003);
        :>> TRQ_PID_DEFAULT.viscousNeg = (-0.0016, -0.003, -0.003);
        :>> TRQ_PID_DEFAULT.coulombPos = (0, 0, 0);
        :>> TRQ_PID_DEFAULT.coulombNeg = (0, 0, 0);
        :>> TRQ_PID_DEFAULT.velocityThres = (0, 0, 0);
        :>> TRQ_PID_DEFAULT.filterType = (0, 0, 0);
        :>> TRQ_PID_DEFAULT.ktau = (-200, -200, -200);
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
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ACTUATOR.type = ("eomc_act_foc", "foc", "foc");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ACTUATOR.portName = ("CAN1:3:0", "CAN1:4:0", "CAN1:1:0");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER1.type = ("eomc_enc_aea", "aea", "aea");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER1.portName = ("CONN:P6", "CONN:P7", "CONN:P8");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER1.position = ("eomc_pos_atjoint", "atjoint", "atjoint");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER1.resolution = (4096, 4096, 4096);
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER1.tolerance = (0.703, 0.703, 0.703);
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER2.type = ("roie", "roie", "roie");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER2.portName = ("CAN1:3:0", "CAN1:4:0", "CAN1:1:0");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER2.position = ("atmotor", "atmotor", "atmotor");
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER2.resolution = (-14400, -14400, -14400);
        :>> SERVICE.PROPERTIES.JOINTMAPPING.ENCODER2.tolerance = (0, 0, 0);
    }
    part torso_eb22_skin :> skin {
        :>> includes = ("../../general.xml", "../../hardware/electronics/face_eb22_j0_eln.xml");
        :>> name = "torso-eb22-skin";
        :>> type = "embObjSkin";
        :>> patches.skinCanAddrsPatch1 = (7, 8, 9, 10);
    }
    part torso_eb22_skinSpec :> skinSpec {
    }

    part torso_mc_wrapper :> wrapper_mc {
        :>> name = "torso-mc_nws_yarp";
        :>> type = "controlBoard_nws_yarp";
        :>> period = 0.01;
        :>> portName = "/icub/torso";
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
        :>> type = "controlboardremapper";
        :>> name = "torso-mc_remapper";
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
    part torso_inertials_wrapper :> wrapper_inertial {
        :>> name = "torso-inertials_wrapper";
        :>> type = "multipleanalogsensorsserver";
        :>> period = 10;
        :>> portName = "/icub/torso/inertials";
        :>> startup.phase = "startup";
        :>> startup.type = "attach";
        :>> startup.level = 5;
        :>> startup.elementName = "SetOfIMUs";
        :>> startup.elementValue = "torso-inertial_remapper";
        :>> shutdown.phase = "shutdown";
        :>> shutdown.type = "detach";
        :>> shutdown.level = 5;
    }
}