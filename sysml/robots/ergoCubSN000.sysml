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
}