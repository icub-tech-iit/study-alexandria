import ScalarValues::*;
import VectorValues::*;
part SERVICE {
    attribute type : VectorValue;
    part PROPERTIES {
        part ETHBOARD {
            attribute type : VectorValue;
        }
        part JOINTMAPPING {
            part ACTUATOR {
                attribute type : VectorValue;
                attribute portName : VectorValue;
            }
            part ENCODER1 :> ENCODER;
            part ENCODER2 :> ENCODER;
        }
    }
}