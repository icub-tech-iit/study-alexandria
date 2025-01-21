// import PartsTree::*;

package iCubErzelli03 {
    attribute name : String default "iCubErzelli03";
    attribute version : String default "V2";
    part head :> Head {
        :>> calibrator1.CALIBRATION.calibration1 = -756;
    }
    part parts = (head);
}