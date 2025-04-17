part skin : device {
    part patches {
        attribute skinCanAddrsPatch1 : Array {
            :>> dimensions default 1;
            :>> elements : Integer[dimensions] default (0);
        }
        attribute skinCanAddrsPatch2 : Array {
            :>> dimensions default 1;
            :>> elements : Integer[dimensions] default (0);
        }
    }
}