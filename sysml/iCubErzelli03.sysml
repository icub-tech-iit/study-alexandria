// import PartsTree::*;

package iCubErzelli03 {
    attribute name : String default "iCubErzelli03";
    attribute version : String default "V2";
    attribute parts : Array {
        :>> dimensions default 1;
        :>> elements : String[dimensions] default ("head");
    }
}