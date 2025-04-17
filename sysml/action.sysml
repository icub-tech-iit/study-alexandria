part def actionPhase {
    attribute phase : String default "phase";
    attribute level : Integer default 1;
    attribute type : String default "type";
    attribute element : Array {
        :>> dimensions default 2;
        :>> elements : String[dimensions] default ("elem1", "elem2");
    }
}