part skinSpec {
    part defaultCfgBoard {
        attribute period : Integer default 50;
        attribute skinType : Integer default 8;
        attribute noLoad : String default "0xf0";
        attribute diagnostic : Boolean default false;
    }
    part defaultCfgTriangle {
        attribute enabled : Boolean default true;
        attribute shift : Integer default 2;
        attribute cdcOffset : String default "0x2200";
    }
    part specialCfgTriangles {
        attribute numOfSets : Integer default 20;
        attribute triangleSetCfg1 : Array {
            :>> dimensions default 7;
            :>> elements : Integer[dimensions] default (1, 14, 0, 6, 1, 0, "0x2000");
        }
        attribute triangleSetCfg2 : Array {
            :>> dimensions default 7;
            :>> elements : Integer[dimensions] default (1, 14, 8, 11, 1, 2, "0x2200");
        }
        attribute triangleSetCfg3 : Array {
            :>> dimensions default 7;
            :>> elements : Integer[dimensions] default (1, 13, 0, 15, 1, 2, "0x2200");
        }
        attribute triangleSetCfg4 : Array {
            :>> dimensions default 7;
            :>> elements : Integer[dimensions] default (1, 12, 0, 1, 1, 2, "0x2200");
        }
        attribute triangleSetCfg5 : Array {
            :>> dimensions default 7;
            :>> elements : Integer[dimensions] default (1, 12, 3, 3, 1, 2, "0x2200");
        }
        attribute triangleSetCfg6 : Array {
            :>> dimensions default 7;
            :>> elements : Integer[dimensions] default (1, 12, 6, 6, 1, 2, "0x2200");
        }
        attribute triangleSetCfg7 : Array {
            :>> dimensions default 7;
            :>> elements : Integer[dimensions] default (1, 12, 8, 9, 1, 2, "0x2200");
        }
        attribute triangleSetCfg8 : Array {
            :>> dimensions default 7;
            :>> elements : Integer[dimensions] default (1, 12, 12, 13, 1, 2, "0x2200");
        }  
        attribute triangleSetCfg9 : Array {
            :>> dimensions default 7;
            :>> elements : Integer[dimensions] default (1, 11, 1, 4, 1, 2, "0x2200");
        }
        attribute triangleSetCfg10 : Array {
            :>> dimensions default 7;
            :>> elements : Integer[dimensions] default (1, 11, 8, 13, 1, 2, "0x2200");
        }
        attribute triangleSetCfg11 : Array {
            :>> dimensions default 7;
            :>> elements : Integer[dimensions] default (1, 10, 0, 1, 1, 2, "0x2200");
        }
        attribute triangleSetCfg12 : Array {
            :>> dimensions default 7;
            :>> elements : Integer[dimensions] default (1, 10, 6, 6, 1, 2, "0x2200");
        }
        attribute triangleSetCfg13 : Array {
            :>> dimensions default 7;
            :>> elements : Integer[dimensions] default (1, 10, 8, 15, 1, 2, "0x2200");
        }
        attribute triangleSetCfg14 : Array {
            :>> dimensions default 7;
            :>> elements : Integer[dimensions] default (1, 9, 0, 8, 1, 2, "0x2200");
        }
        attribute triangleSetCfg15 : Array {
            :>> dimensions default 7;
            :>> elements : Integer[dimensions] default (1, 9, 12, 13, 1, 2, "0x2200");
        }
        attribute triangleSetCfg16 : Array {
            :>> dimensions default 7;
            :>> elements : Integer[dimensions] default (1, 8, 0, 0, 1, 2, "0x2200");
        }
        attribute triangleSetCfg17 : Array {
            :>> dimensions default 7;
            :>> elements : Integer[dimensions] default (1, 8, 8, 9, 1, 2, "0x2200");
        }
        attribute triangleSetCfg18 : Array {
            :>> dimensions default 7;
            :>> elements : Integer[dimensions] default (1, 8, 10, 11, 1, 2, "0x2200");
        }
        attribute triangleSetCfg19 : Array {
            :>> dimensions default 7;
            :>> elements : Integer[dimensions] default (1, 8, 13, 13, 1, 2, "0x2200");
        }
        attribute triangleSetCfg20 : Array {
            :>> dimensions default 7;
            :>> elements : Integer[dimensions] default (1, 8, 15, 15, 1, 2, "0x2200");
        }
    }
}