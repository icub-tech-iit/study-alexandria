package iCubErzelli03 {
    attribute name : String default "iCubErzelli03";
    attribute version : String default "V2";
    part head : Head = "" {
        :>> face_calib.CALIBRATION.calibration1 = -756;
        :>> head_eb20_j0_1_eln.ETH_BOARD.ETH_BOARD_PROPERTIES.IpAddress = "10.0.1.0";
        :>> head_eb21_j2_5_eln.ETH_BOARD.ETH_BOARD_SETTINGS.RUNNINGMODE.TXrateOfRegularROPs = 2;
        :>> head_eb20_j0_1_mec.JOINTSET_CFG.JOINTSET_0.listofjoints = 7;
        :>> face_eb22_j0_mc.POS_PID_DEFAULT.kp = 60.0;
        :>> head_eb20_j0_1_mc_service.SERVICE.PROPERTIES.ETHBOARD.type = "pippo";
    }
}