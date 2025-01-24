// import PartsTree::*;

package iCubErzelli03 {
    attribute name : String default "iCubErzelli03";
    attribute version : String default "V2";
    part head :> Head {
        :>> calibrator1.CALIBRATION.calibration1 = -756;
        :>> electronics2.ETH_BOARD.ETH_BOARD_PROPERTIES.IpAddress = "10.0.1.0";
        :>> electronics3.ETH_BOARD.ETH_BOARD_SETTINGS.RUNNINGMODE.TXrateOfRegularROPs = 2;
        :>> mech2.JOINTSET_CFG.JOINTSET_0.listofjoints = 7;
        :>> motorcontrol1.POS_PID_DEFAULT.kp = 60.0;
        :>> service2.SERVICE.PROPERTIES.ETHBOARD.type = "pippo";
    }
    part parts = (head);
}