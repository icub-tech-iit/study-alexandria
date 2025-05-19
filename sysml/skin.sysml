part skin : device {
    attribute folder_name : String default "hardware/skin/";
    attribute includes : Array {
        :>> dimensions default 2;
        :>> elements : String[dimensions] default ("../../general.xml", "../../hardware/electronics/eln.xml");
    }
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