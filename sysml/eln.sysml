import ScalarValues::*;
import VectorValues::*;
import Collections::*;
part electronics {
    attribute includes : String default "./pc104.xml";
    part ETH_BOARD {
        part ETH_BOARD_PROPERTIES {
            attribute IpAddress : String default "10.0.1.1";
            attribute IpPort : Integer default 12345;
            attribute Type : String default "mc4plus";
            attribute maxSizeRXpacket : Integer default 768;
            attribute maxSizeROP : Integer default 384;
        }
        part ETH_BOARD_SETTINGS {
            attribute Name : String default "foo";
            part RUNNINGMODE {
                attribute period : Integer default 1000;
                attribute maxTimeOfRXactivity : Integer default 400;
                attribute maxTimeOfDOactivity : Integer default 300;
                attribute maxTimeOfTXactivity : Integer default 300;
                attribute TXrateOfRegularROPs : Integer default 3;
            }
        }
        part ETH_BOARD_ACTIONS {
            part MONITOR_ITS_PRESENCE {
                attribute enabled : Boolean default "true";
                attribute timeout : Real default 0.020;
                attribute periodOfMissingReport : Real default 60.0;
            }
        }
    }
}