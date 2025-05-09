import ScalarValues::*;
part mais : device {
    attribute includes : Array {
        :>> dimensions default 2;
        :>> elements : String[dimensions] default ("../../general.xml", "../../hardware/electronics/eln.xml");
    }
    part SERVICE {
        attribute type : String default "eomn_serv_AS_mais";
        part PROPERTIES {
            part CANBOARDS {
                attribute type : String default "eobrd_mais";
                part PROTOCOL {
                    attribute major : Integer default 0;
                    attribute minor : Integer default 0;
                }
                part FIRMWARE {
                    attribute major : Integer default 0;
                    attribute minor : Integer default 0;
                    attribute build : Integer default 0;
                }
            }
            part SENSORS {
                attribute id : String default "mais";
                attribute type : String default "eoas_mais";
                attribute location : String default "CAN1:1";
            }
        }
        part SETTINGS {
            attribute acquisitionRate : Integer default 10;
            attribute enabledSensors : String default "mais";
        }
    }
}