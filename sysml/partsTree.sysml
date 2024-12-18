package PartsTree {
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
        part calibrator1 subsets calibrator = "face-calib.xml";
        part calibrator2 subsets calibrator = "head-calib.xml";
        
        /*Define electronics*/
        part eln [3] :> electronics;
        part eln1 subsets eln = "face-eb22-j0-eln.xml";
        part eln2 subsets eln = "head-eb20-j0_1-eln.xml";
        part eln3 subsets eln = "head-eb21-j2_5-eln.xml";
        part pc104 subsets pc104 = "pc104.xml";

        /*Define inertials*/
        part inertials :> inertial {
            :>> device::type = "embObjIMU";
        }
        part inertial1 subsets inertials = "head-inertial.xml";

        /*Define mechanicals*/
        part mechanicals [3] :> mechanical;
        part mech1 subsets mechanical = "face-eb22-j0-mec.xml";
        part mech2 subsets mechanical = "head-eb20-j0_1-mec.xml";
        part mech3 subsets mechanical = "head-eb21-j2_5-mec.xml";

        /*Define motorControl*/
        part motorcontrol [3] :> motorControl {
            :>> device::type = "embObjMotionControl";
        }
        part mc1 subsets motorcontrol = "face-eb22-j0-mc.xml";
        part mc2 subsets motorcontrol = "head-eb20-j0_1-mc.xml";
        part mc3 subsets motorcontrol = "head-eb21-j2_5-mc.xml";

        /*Define service*/
        part service [3] :> SERVICE;
        part service1 subsets service = "face-eb22-j0-mc_service.xml" {
            :>> service_type = "eomn_serv_MC_mc4plus";
        }
        part service2 subsets service = "head-eb20-j0_1-mc_service.xml" {
            :>> service_type = "eomn_serv_MC_mc4plus";
        }
        part service3 subsets service = "head-eb21-j2_5-mc_service.xml" {
            :>> service_type = "eomn_serv_MC_mc4plus";
        }
    }

    abstract part torso {
        part calibrator1 subsets calibrator = "torso-calib.xml";
    }
}   