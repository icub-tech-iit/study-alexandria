abstract part head {
    /*Define calibrators*/
    part calibration [2] :> calibrator {
        :>> device::type = "parametricCalibratorEth";
        attribute attach :> phase {
            :>> level = 10;
        }
        attribute interrupt1 :> phase {
            :>> type = "park";
        }
        attribute interrupt3 :> phase {
            :>> type = "abort";
        }
    }
    part calibrator1 subsets calibrator = "calibrators/face-calib.xml";
    part calibrator2 subsets calibrator = "calibrators/head-calib.xml";
    
    /*Define electronics*/
    part eln [3] :> electronics;
    part eln1 subsets eln = "hardware/electronics/face-eb22-j0-eln.xml";
    part eln2 subsets eln = "hardware/electronics/head-eb20-j0_1-eln.xml";
    part eln3 subsets eln = "hardware/electronics/head-eb21-j2_5-eln.xml";
    /*Define pc104*/
    part pc104 [1] :> pc104;
    part pc1041 subsets pc104 = "hardware/electronics/pc104.xml";

    /*Define inertials*/
    part inertials [1] :> inertial {
        :>> device::type = "embObjIMU";
    }
    part inertial1 subsets inertials = "hardware/inertials/head-inertial.xml";

    /*Define mechanicals*/
    part mechanicals [3] :> mechanical;
    part mech1 subsets mechanical = "hardware/mechanicals/face-eb22-j0-mec.xml";
    part mech2 subsets mechanical = "hardware/mechanicals/head-eb20-j0_1-mec.xml";
    part mech3 subsets mechanical = "hardware/mechanicals/head-eb21-j2_5-mec.xml";

    /*Define motorControl*/
    part motorcontrol [3] :> motorControl {
        :>> device::type = "embObjMotionControl";
    }
    part mc1 subsets motorcontrol = "hardware/motorControl/face-eb22-j0-mc.xml";
    part mc2 subsets motorcontrol = "hardware/motorControl/head-eb20-j0_1-mc.xml";
    part mc3 subsets motorcontrol = "hardware/motorControl/head-eb21-j2_5-mc.xml";

    /*Define service*/
    part service [3] :> SERVICE;
    part service1 subsets service = "hardware/motorControl/face-eb22-j0-mc_service.xml" {
        :>> service_type = "eomn_serv_MC_mc4plus";
    }
    part service2 subsets service = "hardware/motorControl/head-eb20-j0_1-mc_service.xml" {
        :>> service_type = "eomn_serv_MC_mc4plus";
    }
    part service3 subsets service = "hardware/motorControl/head-eb21-j2_5-mc_service.xml" {
        :>> service_type = "eomn_serv_MC_mc4plus";
    }
}