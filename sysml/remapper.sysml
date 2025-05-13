part remapper : device {
    attribute element : Array {
        :>> dimensions default 1;
        :>> elements : String[dimensions] default ("(0 0 0 0)");
    }
    attribute joints : Integer default 1;
    part startup : actionPhase;
    part shutdown : phase;
}