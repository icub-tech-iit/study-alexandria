import Collections::*;
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
        part JOINTMAPPING {
            part ACTUATOR {
                attribute type : Array {
                    :>> dimensions default 1; 
                    :>> elements : String[dimensions] default ("pwm"); 
                    }
                attribute portName : Array {
                    :>> dimensions default 1; 
                    :>> elements : String[dimensions] default ("portName"); 
                    }
            }
            part ENCODER1 :> ENCODER;
            part ENCODER2 :> ENCODER;
        }
    }
}