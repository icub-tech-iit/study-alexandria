part inertial : device {
    part SERVICE {
        attribute type : String default "inertial";
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
                    :>> dimensions default 3;
                    :>> elements : String[dimensions] default ("acc", "gyro", "mag");
                }
                attribute sensorName : Array {
                    :>> dimensions default 3;
                    :>> elements : String[dimensions] default ("acc", "gyro", "mag");
                }
                attribute type : Array {
                    :>> dimensions default 3;
                    :>> elements : String[dimensions] default ("acc", "gyro", "mag");
                }
                attribute boardType : Array {
                    :>> dimensions default 3;
                    :>> elements : String[dimensions] default ("brd", "brd", "brd");
                }
                attribute location : Array {
                    :>> dimensions default 3;
                    :>> elements : String[dimensions] default ("CAN1:1", "CAN1:2", "CAN1:3");
                }
            }
            part SETTINGS {
                attribute acquisitionRate : Integer default 50;
                attribute enabledSensors : Array {
                    :>> dimensions default 3;
                    :>> elements : String[dimensions] default ("acc", "gyro", "mag");
                }
            }
        }
    }
}