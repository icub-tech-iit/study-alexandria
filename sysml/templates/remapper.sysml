part remapper : device {
    attribute folder_name : String default "wrappers/";
    attribute elementName : Array {
        :>> dimensions default 1;
        :>> elements : String[dimensions] default ("elem1");
    }
    attribute elementValue : Array {
        :>> dimensions default 1;
        :>> elements : String[dimensions] default ("value1");
    }
    attribute joints : Integer default 1;
    part startup : actionPhase;
    part shutdown : phase;
}