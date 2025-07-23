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
        :>> face_calib.CALIBRATION.startupMaxPwm = 3360;
        :>> face_calib.CALIBRATION.startupPosThreshold = 90;

        :>> head_calib.CALIBRATION.calibration1 = (52543, 64079, 33231, 52175, 3000, 3000);
        :>> head_calib.CALIBRATION.calibration2 = (0, 0, 0, 0, 8192, 8192);
        :>> head_calib.CALIBRATION.calibration3 = (0, 0, 0, 0, 0, 0);
        :>> head_calib.CALIBRATION.calibration4 = (0, 0, 0, 0, 0, 0);
        :>> head_calib.CALIBRATION.calibration5 = (0, 0, 0, 0, 0, 0);
        :>> head_calib.CALIBRATION.calibrationZero = (0, 0, 0, 0, 0, 0);
        :>> head_calib.CALIBRATION.calibrationDelta = (0, 0, 0, -6, -6, -10);
        :>> head_calib.CALIBRATION.startupPosition = (0, 0, 0, 0, 0, 0);
        :>> head_calib.CALIBRATION.startupVelocity = (10, 10, 20, 20, 20, 20);
        :>> head_calib.CALIBRATION.startupMaxPwm = (3000, 3000, 3000, 3000, 0, 0);
        :>> head_calib.CALIBRATION.startupPosThreshold = (90, 90, 2, 2, 2, 2);
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
        :>> torso_calib.CALIBRATION.startupMaxPwm = (8500, 8500, 8500);
        :>> torso_calib.CALIBRATION.startupPosThreshold = (2, 2, 2);
        :>> torso_eb5_j0_2_mc_service.SERVICE.PROPERTIES.CANBOARDS.PROTOCOL.major = 1;
        :>> torso_eb5_j0_2_mc_service.SERVICE.PROPERTIES.CANBOARDS.PROTOCOL.minor = 6;
        :>> torso_eb5_j0_2_mc_service.SERVICE.PROPERTIES.CANBOARDS.FIRMWARE.major = 3;
        :>> torso_eb5_j0_2_mc_service.SERVICE.PROPERTIES.CANBOARDS.FIRMWARE.minor = 3;
        :>> torso_eb5_j0_2_mc_service.SERVICE.PROPERTIES.CANBOARDS.FIRMWARE.build = 3;
    }
    part left_arm : LeftArm {
        :>> left_arm_calib.CALIBRATION.calibration1 = (58559, 22639, 48830, 51983, -1500, 450, 11679, 0, 0, 0, 0, 0, 0, 0, 0, 0);
        :>> left_arm_calib.CALIBRATION.calibration2 = (0, 0, 0, 0, 16384, 0, 0, 0, 0, 9102, 9102, 9102, 9102, 9102, 9102, 10000);
        :>> left_arm_calib.CALIBRATION.calibration3 = (0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 1, -1, 1, -1, 1, 1);
        :>> left_arm_calib.CALIBRATION.calibration4 = (0, 0, 0, 0, 0, 0, 0, 3140, 1150, 255, 480, 255, 491, 255, 494, 780);
        :>> left_arm_calib.CALIBRATION.calibration5 = (0, 0, 0, 0, 0, 0, 0, 3295, 3450, 0, 18, 0, 18, 0, 11, 198);
        :>> left_arm_calib.CALIBRATION.calibrationZero = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);
        :>> left_arm_calib.CALIBRATION.calibrationDelta = (0, -9.2, -17.1, -2.7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);
        :>> left_arm_calib.CALIBRATION.startupPosition = (-35, 30, 0, 50, 0, 0, 0, 35, 50, 0, 0, 0, 0, 0, 0, 0);
        :>> left_arm_calib.CALIBRATION.startupVelocity = (10, 10, 10, 10, 30, 30, 30, 60, 100, 100, 100, 100, 100, 100, 100, 100);
        :>> left_arm_calib.CALIBRATION.startupMaxPwm = (3000, 3000, 3000, 3000, 3000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);
        :>> left_arm_calib.CALIBRATION.startupPosThreshold = (2, 2, 2, 2, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90);
        :>> left_arm_calib.CALIB_ORDER = "(0 1 2 3) (4) (5 6) (8 9 11 13) (10 12 14)";
        :>> left_arm_eb1_j0_3_mc_service.SERVICE.PROPERTIES.CANBOARDS.PROTOCOL.major = 1;
        :>> left_arm_eb1_j0_3_mc_service.SERVICE.PROPERTIES.CANBOARDS.PROTOCOL.minor = 6;
        :>> left_arm_eb1_j0_3_mc_service.SERVICE.PROPERTIES.CANBOARDS.FIRMWARE.major = 3;
        :>> left_arm_eb1_j0_3_mc_service.SERVICE.PROPERTIES.CANBOARDS.FIRMWARE.minor = 3;
        :>> left_arm_eb1_j0_3_mc_service.SERVICE.PROPERTIES.CANBOARDS.FIRMWARE.build = 3;
    }
    part right_arm : RightArm {
        :>> right_arm_calib.CALIBRATION.calibration1 = (35535, 33135, 24960, 25983, 1500, 11700, 55950, 0, 0, 0, 0, 0, 0, 0, 0, 0);
        :>> right_arm_calib.CALIBRATION.calibration2 = (0, 0, 0, 0, 16384, 0, 0, 0, 0, 9102, 9102, 9102, 9102, 9102, 9102, 10000);
        :>> right_arm_calib.CALIBRATION.calibration3 = (0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 1, -1, 1, -1, 1, 1);
        :>> right_arm_calib.CALIBRATION.calibration4 = (0, 0, 0, 0, 0, 0, 0, 1720, 2180, 241, 510, 255, 510, 255, 510, 785);
        :>> right_arm_calib.CALIBRATION.calibration5 = (0, 0, 0, 0, 0, 0, 0, 1945, 3420, 40, 0, 0, 23, 0, 0, 210);
        :>> right_arm_calib.CALIBRATION.calibrationZero = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);
        :>> right_arm_calib.CALIBRATION.calibrationDelta = (1.0, -9.2, -14.2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);
        :>> right_arm_calib.CALIBRATION.startupPosition = (-35, 30, 0, 50, 0, 0, 0, 35, 50, 0, 0, 0, 0, 0, 0, 0);
        :>> right_arm_calib.CALIBRATION.startupVelocity = (10, 10, 10, 10, 30, 30, 30, 60, 100, 100, 100, 100, 100, 100, 100, 100);
        :>> right_arm_calib.CALIBRATION.startupMaxPwm = (3000, 3000, 3000, 3000, 3000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);
        :>> right_arm_calib.CALIBRATION.startupPosThreshold = (5, 2, 2, 2, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90);
        :>> right_arm_calib.CALIB_ORDER = "(0 1 2 3) (4) (5 6) (8 9 11 13) (10 12 14)";
        :>> right_arm_eb3_j0_3_mc_service.SERVICE.PROPERTIES.CANBOARDS.PROTOCOL.major = 1;
        :>> right_arm_eb3_j0_3_mc_service.SERVICE.PROPERTIES.CANBOARDS.PROTOCOL.minor = 6;
        :>> right_arm_eb3_j0_3_mc_service.SERVICE.PROPERTIES.CANBOARDS.FIRMWARE.major = 3;
        :>> right_arm_eb3_j0_3_mc_service.SERVICE.PROPERTIES.CANBOARDS.FIRMWARE.minor = 3;
        :>> right_arm_eb3_j0_3_mc_service.SERVICE.PROPERTIES.CANBOARDS.FIRMWARE.build = 3;
    }
    part extra : Extra;
}