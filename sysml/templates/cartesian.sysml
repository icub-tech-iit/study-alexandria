part cartesian : device {
    attribute folder_name : String default "cartesian/";
    part GENERAL {
        attribute ControllerName : String default "foo";
        attribute ControllerPeriod : Integer default 10;
        attribute TaskRefVelPeriodFactor : Integer default 4;
        attribute SolverNameToConnect : String default "foo";
        attribute KinematicPart : String default "arm";
        attribute KinematicType : String default "part_version";
        attribute PositionControl : String default "on";
        attribute NumberOfDrivers : Integer default 2;
    }
    part DRIVER_0 {
        attribute Key : String default "torso";
        attribute JointsOrder : String default "reversed";
        attribute MinAbsVels : Array {
            :>> dimensions default 3;
            :>> elements : Real[dimensions] default (0.35, 0.35, 0.35);
        }
    }
    part DRIVER_1 {
        attribute Key : String default "arm";
        attribute JointsOrder : String default "direct";
        attribute MinAbsVels : Array {
            :>> dimensions default 7;
            :>> elements : Real[dimensions] default (0.35, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35);
        }
    }
    part PLANT_MODEL {
        attribute plant_compensator : String default "on";
        attribute smith_predictor : String default "off";
        attribute joint_0 : Array {
            :>> dimensions default 5;
            :>> elements : String[dimensions] default ("(Kp 1.022)", "(Tz 0.405)", "(Tw 0.248)", "(Zeta 0.797)", "(Td 0.000)");
        }
        attribute joint_1 : Array {
            :>> dimensions default 5;
            :>> elements : String[dimensions] default ("(Kp 1.026)", "(Tz 0.407)", "(Tw 0.243)", "(Zeta 0.822)", "(Td 0.000)");
        }
        attribute joint_2 : Array {
            :>> dimensions default 5;
            :>> elements : String[dimensions] default ("(Kp 1.040)", "(Tz 0.344)", "(Tw 0.160)", "(Zeta 1.110)", "(Td 0.000)");
        }
        attribute joint_3 : Array {
            :>> dimensions default 5;
            :>> elements : String[dimensions] default ("(Kp 1.035)", "(Tz 0.410)", "(Tw 0.178)", "(Zeta 1.198)", "(Td 0.000)");
        }
        attribute joint_4 : Array {
            :>> dimensions default 5;
            :>> elements : String[dimensions] default ("(Kp 1.016)", "(Tz 0.384)", "(Tw 0.159)", "(Zeta 1.222)", "(Td 0.000)");
        }
        attribute joint_5 : Array {
            :>> dimensions default 5;
            :>> elements : String[dimensions] default ("(Kp 1.025)", "(Tz 0.823)", "(Tw 0.405)", "(Zeta 1.030)", "(Td 0.000)");
        }
        attribute joint_6 : Array {
            :>> dimensions default 5;
            :>> elements : String[dimensions] default ("(Kp 1.022)", "(Tz 0.300)", "(Tw 0.120)", "(Zeta 1.303)", "(Td 0.000)");
        }
        attribute joint_7 : Array {
            :>> dimensions default 5;
            :>> elements : String[dimensions] default ("(Kp 1.016)", "(Tz 0.123)", "(Tw 0.030)", "(Zeta 2.204)", "(Td 0.000)");
        }
        attribute joint_8 : Array {
            :>> dimensions default 5;
            :>> elements : String[dimensions] default ("(Kp 1.000)", "(Tz 0.000)", "(Tw 0.000)", "(Zeta 0.000)", "(Td 0.000)");
        }
        attribute joint_9 : Array {
            :>> dimensions default 5;
            :>> elements : String[dimensions] default ("(Kp 1.000)", "(Tz 0.000)", "(Tw 0.000)", "(Zeta 0.000)", "(Td 0.000)");
        }
    }
    part startup : actionPhase;	
    part shutdown : phase;
}