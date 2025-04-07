package iCubGenova11 {
    attribute name : String default "iCubGenova11";
    attribute version : String default "V2";
    part head : Head {
        :>> face_calib.CALIBRATION.calibration1 = -3110;
        :>> face_calib.CALIBRATION.calibration2 = 0;
        :>> face_calib.CALIBRATION.calibration3 = 0;
        :>> face_calib.CALIBRATION.calibration4 = 0;
        :>> face_calib.CALIBRATION.calibration5 = 0;
        :>> face_calib.CALIBRATION.calibrationZero = 0;
        :>> face_calib.CALIBRATION.calibrationDelta = 0;
        :>> face_calib.CALIBRATION.startupPosition = 0;
        :>> face_calib.CALIBRATION.startupVelocity = 10;
        :>> face_calib.CALIBRATION.startupPwm = 3360;
        :>> face_calib.CALIBRATION.startupPosThreshold = 90;

        :>> head_calib.CALIBRATION.calibration1 = (52543, 64079, 33231, 52175, 3000, 3000);
        :>> head_calib.CALIBRATION.calibration2 = (0, 0, 0, 0, 8192, 8192);
        :>> head_calib.CALIBRATION.calibration3 = (0, 0, 0, 0, 0, 0);
        :>> head_calib.CALIBRATION.calibration4 = (0, 0, 0, 0, 0, 0);
        :>> head_calib.CALIBRATION.calibration5 = (0, 0, 0, 0, 0, 0);
        :>> head_calib.CALIBRATION.calibrationZero = (0, 0, 0, 0, 0, 0);
        :>> head_calib.CALIBRATION.calibrationDelta = (0, 0, 0, -6, -6, 10);
        :>> head_calib.CALIBRATION.startupPosition = (0, 0, 0, 0, 0, 0);
        :>> head_calib.CALIBRATION.startupVelocity = (10, 10, 20, 20, 20, 20);
        :>> head_calib.CALIBRATION.startupPwm = (3000, 3000, 3000, 3000, 0, 0);
        :>> head_calib.CALIBRATION.startupPosThreshold = (90, 90, 2, 2, 2, 2);

        :>> head_eb20_j0_1_eln.ETH_BOARD.ETH_BOARD_PROPERTIES.IpAddress = "10.0.1.0";
        :>> head_eb21_j2_5_eln.ETH_BOARD.ETH_BOARD_SETTINGS.RUNNINGMODE.TXrateOfRegularROPs = 2;
        :>> head_eb20_j0_1_mec.JOINTSET_CFG.JOINTSET_0.listofjoints = 7;
        :>> face_eb22_j0_mc.POS_PID_DEFAULT.kp = 60.0;
        :>> head_eb20_j0_1_mc_service.SERVICE.PROPERTIES.ETHBOARD.type = "pippo";
    }
    part torso : Torso {
        :>> torso_calib.CALIBRATION.calibration1 = (17759, 20300, 43551);
        :>> torso_calib.CALIBRATION.calibration2 = (0, 0, 0);
        :>> torso_calib.CALIBRATION.calibration3 = (0, 0, 0);
        :>> torso_calib.CALIBRATION.calibration4 = (0, 0, 0);
        :>> torso_calib.CALIBRATION.calibration5 = (0, 0, 0);
        :>> torso_calib.CALIBRATION.calibrationZero = (0, 0, 0);
        :>> torso_calib.CALIBRATION.calibrationDelta = (0, 0, 0);
        :>> torso_calib.CALIBRATION.startupPosition = (0, 0, 0);
        :>> torso_calib.CALIBRATION.startupVelocity = (10, 10, 10);
        :>> torso_calib.CALIBRATION.startupPwm = (8500, 8500, 8500);
        :>> torso_calib.CALIBRATION.startupPosThreshold = (2, 2, 2);
    }
}