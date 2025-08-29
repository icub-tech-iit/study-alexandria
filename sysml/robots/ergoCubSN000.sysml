package ergoCubSN000 {
    attribute name : String default "ergoCubSN000";
    attribute version : String default "1.0";
    part head : ErgoCubHead {
        :>> head_calib.CALIBRATION.calibration1 = (25220, -17823, 61615, 52575);
        :>> head_calib.CALIBRATION.calibration2 = (0, 0, 0, 0);
        :>> head_calib.CALIBRATION.calibration3 = (0, 0, 0, 0);
        :>> head_calib.CALIBRATION.calibration4 = (0, 0, 0, 0);
        :>> head_calib.CALIBRATION.calibration5 = (0, 0, 0, 0);
        :>> head_calib.CALIBRATION.calibrationZero = (0, 0, 0, 0);
        :>> head_calib.CALIBRATION.calibrationDelta = (0, 0, 0, 0);
        :>> head_calib.CALIBRATION.startupPosition = (0, 0, 0, 0);
        :>> head_calib.CALIBRATION.startupVelocity = (10, 10, 20, 20);
        :>> head_calib.CALIBRATION.startupMaxPwm = (1000, 1000, 1000, 1000);
        :>> head_calib.CALIBRATION.startupPosThreshold = (90, 90, 2, 2);
    }
    part torso : ErgoCubTorso {
        :>> torso_calib.CALIBRATION.calibration1 = (6500, -6500, 2500);
        :>> torso_calib.CALIBRATION.calibration2 = (0, 0, 0);
        :>> torso_calib.CALIBRATION.calibration3 = (0, 0, 0);
        :>> torso_calib.CALIBRATION.calibration4 = (0, 0, 0);
        :>> torso_calib.CALIBRATION.calibration5 = (0, 0, 0);
        :>> torso_calib.CALIBRATION.calibrationZero = (24.903, -21.847, -46.066);
        :>> torso_calib.CALIBRATION.calibrationDelta = (0, 0, 0);
        :>> torso_calib.CALIBRATION.startupPosition = (0, 0, 0);
        :>> torso_calib.CALIBRATION.startupVelocity = (10, 10, 10);
        :>> torso_calib.CALIBRATION.startupMaxPwm = (5500, 5500, 5500);
        :>> torso_calib.CALIBRATION.startupPosThreshold = (2, 2, 2);
    }
    part left_arm : ErgoCubLeftArm {
        :>> left_arm_calib.CALIBRATION.calibration1 = (4000, -3000, -3000, 4000, 1127, 24927, 7183, 0, 300, 0, 300, 300, 300);
        :>> left_arm_calib.CALIBRATION.calibration2 = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);
        :>> left_arm_calib.CALIBRATION.calibration3 = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);
        :>> left_arm_calib.CALIBRATION.calibration4 = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);
        :>> left_arm_calib.CALIBRATION.calibration5 = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);
        :>> left_arm_calib.CALIBRATION.calibrationZero = (35, -15, -52, -5, 0, 0, 0, 0, 0, 0, 0, 0, 0);
        :>> left_arm_calib.CALIBRATION.calibrationDelta = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);
        :>> left_arm_calib.CALIBRATION.startupPosition = (34, 50, -10, 90, 0.0, 0.0, 0.0, 0.0, 4.0, 0.0, 4.0, 4.0, 4.0);
        :>> left_arm_calib.CALIBRATION.startupVelocity = (10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 100.0, 100.0, 0.0, 100.0, 100.0, 100.0);
        :>> left_arm_calib.CALIBRATION.startupMaxPwm = (8000, 8000, 8000, 8000, 16000, 16000, 16000, 0, 0, 0, 0, 0, 0);
        :>> left_arm_calib.CALIBRATION.startupPosThreshold = (2, 2, 2, 2, 2, 2, 2, 90, 5, 90, 5, 5, 5);
    }
    part right_arm : ErgoCubRightArm {
        :>> right_arm_calib.CALIBRATION.calibration1 = (-4000, 3000, 3000, -4000, 4023, 2143, 17071, 0, 300, 0, 300, 300, 300);
        :>> right_arm_calib.CALIBRATION.calibration2 = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);
        :>> right_arm_calib.CALIBRATION.calibration3 = (0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0);
        :>> right_arm_calib.CALIBRATION.calibration4 = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);
        :>> right_arm_calib.CALIBRATION.calibration5 = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);
        :>> right_arm_calib.CALIBRATION.calibrationZero = (35, -15, -52, -5, 0, 0, 0, 0, 0, 0, 0, 0, 0);
        :>> right_arm_calib.CALIBRATION.calibrationDelta = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);
        :>> right_arm_calib.CALIBRATION.startupPosition = (34, 50, -10, 90, 0.0, 0.0, 0.0, 0.0, 4.0, 0.0, 4.0, 4.0, 4.0);
        :>> right_arm_calib.CALIBRATION.startupVelocity = (10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 100.0, 100.0, 0.0, 100.0, 100.0, 100.0);
        :>> right_arm_calib.CALIBRATION.startupMaxPwm = (8000, 8000, 8000, 8000, 16000, 16000, 16000, 0, 0, 0, 0, 0, 0);
        :>> right_arm_calib.CALIBRATION.startupPosThreshold = (2, 2, 2, 2, 2, 2, 2, 90, 5, 90, 5, 5, 5);
    }