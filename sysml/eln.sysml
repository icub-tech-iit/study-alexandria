import ScalarValues::*;
import VectorValues::*;
part electronics {
    part ETH_BOARD {
        part ETH_BOARD_PROPERTIES {
            attribute IpAddress : String default "foo";
            attribute IpPort : Integer default 12345;
            attribute Type : String default "foo";
            attribute maxSizeRXpacket : String default "foo";
            attribute maxSizeROP : String default "foo";
        }
        part ETH_BOARD_SETTINGS {
            attribute Name : String;
            part RUNNINGMODE {
                attribute period : Integer;
                attribute maxTimeOfRXactivity : Integer;
                attribute maxTimeOfDOactivity : Integer;
                attribute maxTimeOfTXactivity : Integer;
                attribute TXrateOfRegularROPs : Integer;
            }
        }
        part ETH_BOARD_ACTIONS {
            part MONITOR_ITS_PRESENCE {
                attribute enabled : Boolean = true;
                attribute timeout : Real;
                attribute periodOfMissingReport : Real;
            }
        }
    }
}