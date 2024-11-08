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
            part ENCODER1 {
                attribute type : VectorValue;
                attribute portName : VectorValue;
                attribute position : VectorValue;
                attribute resolution : VectorValue;
                attribute tolerance : VectorValue;
            }
            part ENCODER2 {
                attribute type : VectorValue;
                attribute portName : VectorValue;
                attribute position : VectorValue;
                attribute resolution : VectorValue;
                attribute tolerance : VectorValue;
            }
        }
    }
}