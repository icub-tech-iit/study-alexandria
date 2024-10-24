import ScalarValues::*;
import VectorValues::*;
part inertial : device = embObjIMU {
    part SERVICE {
        attribute type : VectorValue;
        part PROPERTIES {
            part CANBOARDS {
                attribute type : VectorValue;
                part PROTOCOL {
                    attribute major : VectorValue;
                    attribute minor : VectorValue;
                }
                part FIRMWARE {
                    attribute major : VectorValue;
                    attribute minor : VectorValue;
                    attribute build : VectorValue;
                }
            }
        }
    }
}