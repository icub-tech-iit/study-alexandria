import Collections::*;
part def actionPhase {
    attribute phase : String default "phase";
    attribute level : Integer default 1;
    attribute type : String default "type";
    attribute elementName : Array {
        :>> dimensions default 1;
        :>> elements : String[dimensions] default ("elem1");
    }
    attribute elementValue : Array {
        :>> dimensions default 1;
        :>> elements : String[dimensions] default ("value1");
    }
}