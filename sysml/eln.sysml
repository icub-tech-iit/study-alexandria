import ScalarValues::*;
import VectorValues::*;
part electronics {
    part ETH_BOARD {
        part ETH_BOARD_PROPERTIES {
            attribute IpAddress : String;
            attribute IpPort : Integer = 12345;
            attribute Type : String;
            attribute maxSizeRXpacket : String;
            attribute maxSizeROP : String;
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