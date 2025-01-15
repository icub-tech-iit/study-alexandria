abstract part head {
    // part calibration [2] :> calibrator {
        // :>> device::type = "parametricCalibratorEth";
        // attribute attach :> phase {
        //     :>> level = 10;
        // }
        // attribute interrupt1 :> phase {
        //     :>> type = "park";
        // }
        // attribute interrupt3 :> phase {
        //     :>> type = "abort";
        // }
    // }
    part calibrator1 :> calibrator = "calibrators/face-calib.xml" {
        :>> GENERAL.deviceName = "FaceV3_Calibrator";
        :>> HOME.velocityHome = (0, 20);
        :>> CALIBRATION.calibrationType = 12;
        :>> CALIBRATION.calibration1 = -7656;
        attribute attach :> phase {
            :>> level = 10;
        }
    }
    part calibrator2 :> calibrator = "calibrators/head-calib.xml" {
        :>> GENERAL.joints = 6;
        :>> GENERAL.deviceName = "HeadV3_Calibrator";
        :>> HOME.positionHome = (0, 0, 0, 0, 0, 0);
        :>> HOME.velocityHome = (10, 10, 10, 10, 10, 10);
        :>> CALIBRATION.calibrationType = (12, 12, 12, 12, 12, 12);
        :>> CALIBRATION.calibration1 = (31583, 17391, 59087, 5743, 3000, 3000);
        :>> CALIBRATION.calibration2 = (0, 0, 0, 0, 8192, 8192);
        :>> CALIBRATION.calibration3 = (0, 0, 0, 0, 0, 0);
        :>> CALIBRATION.calibration4 = (0, 0, 0, 0, 0, 0);
        :>> CALIBRATION.calibration5 = (0, 0, 0, 0, 0, 0);
        :>> CALIBRATION.calibrationZero = (0, 0, 0, 0, 0, 0);
        :>> CALIBRATION.calibrationDelta = (0, 2.8, 0, 0, 0, 0);
        :>> CALIB_ORDER = "(0 1 2) (3) (4 5)";
    }
    part calibration [2] = (calibrator1, calibrator2);

    part electronics1 :> electronics = "hardware/electronics/face-eb22-j0-eln.xml" {
        :>> ETH_BOARD.ETH_BOARD_PROPERTIES.IpAddress = "10.0.1.22";
        :>> ETH_BOARD.ETH_BOARD_PROPERTIES.maxSizeRXpacket = 768;
        :>> ETH_BOARD.ETH_BOARD_PROPERTIES.maxSizeROP = 384;
        :>> ETH_BOARD.ETH_BOARD_SETTINGS.Name = "face-eb22-j0";
    }
    part electronics2 :> electronics = "hardware/electronics/head-eb20-j0_1-eln.xml" {
        :>> ETH_BOARD.ETH_BOARD_PROPERTIES.IpAddress = "10.0.1.20";
        :>> ETH_BOARD.ETH_BOARD_PROPERTIES.maxSizeRXpacket = 768;
        :>> ETH_BOARD.ETH_BOARD_PROPERTIES.maxSizeROP = 384;
        :>> ETH_BOARD.ETH_BOARD_SETTINGS.Name = "head-eb20-j0_1";
        :>> ETH_BOARD.ETH_BOARD_SETTINGS.RUNNINGMODE.TXrateOfRegularROPs = 5;
    }
    part electronics3 :> electronics = "hardware/electronics/head-eb21-j2_5-eln.xml" {
        :>> ETH_BOARD.ETH_BOARD_PROPERTIES.IpAddress = "10.0.1.21";
        :>> ETH_BOARD.ETH_BOARD_PROPERTIES.maxSizeRXpacket = 768;
        :>> ETH_BOARD.ETH_BOARD_PROPERTIES.maxSizeROP = 384;
        :>> ETH_BOARD.ETH_BOARD_SETTINGS.Name = "head-eb21-j2_5";
        :>> ETH_BOARD.ETH_BOARD_SETTINGS.RUNNINGMODE.TXrateOfRegularROPs = 5;
    }
    part eln [3] = (electronics1, electronics2, electronics3);

    part pc104 :> PC104 = "hardware/electronics/pc104.xml" {}
    part pc104s [1] = (pc104);

    part mech1 :> mechanical = "hardware/mechanicals/face-eb22-j0-mec.xml" {
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
    part mech2 :> mechanical = "hardware/mechanicals/head-eb20-j0_1-mec.xml" {
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
    part mech3 :> mechanical = "hardware/mechanicals/head-eb21-j2_5-mec.xml" {
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
    }
    part mech [3] = (mech1, mech2, mech3);
}