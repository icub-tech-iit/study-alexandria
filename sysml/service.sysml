import Collections::*;
part SERVICE {
    attribute service_type : Array {
        :>> dimensions default 1; 
        :>> elements : String[dimensions] default ("type"); 
        }
    part PROPERTIES {
        part ETHBOARD {
            attribute eth_type : Array {
                :>> dimensions default 1; 
                :>> elements : String[dimensions] default ("type_ethboard"); 
                }
        }
        part JOINTMAPPING {
            part ACTUATOR {
                attribute actuator_type : Array {
                    :>> dimensions default 1; 
                    :>> elements : String[dimensions] default ("type_actuator"); 
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