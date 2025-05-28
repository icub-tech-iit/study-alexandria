import Collections::*;
part service {
    attribute folder_name : String default "hardware/motorControl/";
    part SERVICE {
        attribute type : Array {
            :>> dimensions default 1; 
            :>> elements : String[dimensions] default ("type"); 
            }
        part PROPERTIES {
            part ETHBOARD {
                attribute type : Array {
                    :>> dimensions default 1; 
                    :>> elements : String[dimensions] default ("type_ethboard"); 
                    }
            }
            part CANBOARDS {
                attribute type : Array {
                    :>> dimensions default 1; 
                    :>> elements : String[dimensions] default ("none"); 
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
            part JOINTMAPPING {
                part ACTUATOR {
                    attribute type : Array {
                        :>> dimensions default 1; 
                        :>> elements : String[dimensions] default ("pwm"); 
                        }
                    attribute _port : Array {
                        :>> dimensions default 1; 
                        :>> elements : String[dimensions] default ("portName"); 
                        }
                }
                part ENCODER1 :> ENCODER;
                part ENCODER2 :> ENCODER;
            }
        }
    }
}