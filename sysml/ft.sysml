part ft : device {
    attribute folder_name : String default "hardware/FT/";
    attribute includes : Array {
        :>> dimensions default 2;
        :>> elements : String[dimensions] default ("../../general.xml", "../../hardware/electronics/eln.xml");
    }
    part SERVICE {
        attribute type : String default "eomn_serv_AS_strain";
        part PROPERTIES {
            part CANBOARDS {
                attribute type : Array {
                    :>> dimensions default 1;
                    :>> elements : String[dimensions] default ("eobrd");
                }
                part PROTOCOL {
                    attribute major : Array {
                        :>> dimensions default 1;
                        :>> elements : Integer[dimensions] default (0);
                    }
                    attribute minor : Array {
                        :>> dimensions default 1;
                        :>> elements : Integer[dimensions] default (0);
                    }
                }
                part FIRMWARE {
                    attribute major : Array {
                        :>> dimensions default 1;
                        :>> elements : Integer[dimensions] default (0);
                    }
                    attribute minor : Array {
                        :>> dimensions default 1;
                        :>> elements : Integer[dimensions] default (0);
                    }
                    attribute build : Array {
                        :>> dimensions default 1;
                        :>> elements : Integer[dimensions] default (0);
                    }
                }
            }
            part SENSORS {
                attribute id : Array {
                    :>> dimensions default 1;
                    :>> elements : String[dimensions] default ("ft");
                }
                attribute framename : Array {
                    :>> dimensions default 1;
                    :>> elements : String[dimensions] default ("ft");
                }
                attribute type : Array {
                    :>> dimensions default 1;
                    :>> elements : String[dimensions] default ("eoas_strain");
                }
                attribute location : Array {
                    :>> dimensions default 1;
                    :>> elements : String[dimensions] default ("CAN1:1");
                }
            }
        }
        part SETTINGS {
            attribute acquisitionRate: Integer default 10;
            attribute enabledSensors : Array {
                :>> dimensions default 1;
                :>> elements : String[dimensions] default ("ft");
            }
            attribute temperature_acquisitionRate : Integer default 1000;
        }
        part STRAIN_SETTINGS {
            attribute useCalibration : Boolean default true;
        }
    }
}