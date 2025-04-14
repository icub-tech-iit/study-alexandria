part ft : device {
    part SERVICE {
        attribute type : String default "strain";
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
                attribute board : Array {
                    :>> dimensions default 1;
                    :>> elements : String[dimensions] default ("strain2");
                }
                attribute location : Array {
                    :>> dimensions default 1;
                    :>> elements : String[dimensions] default ("CAN1:1");
                }
            }
            part SETTINGS {
                attribute enabledSensors : Array {
                    :>> dimensions default 1;
                    :>> elements : String[dimensions] default ("ft");
                }
                attribute ftPeriod : Integer default 1;
                attribute temperaturePeriod : Integer default 1000;
                attribute useCalibration : Boolean default "true";
            }
            part CANMONITOR {
                attribute checkPeriod : Integer default 100;
                attribute reportMode: String default "ALL";
                attribute ratePeriod: Integer default 20000;
            }
        }
    }
}