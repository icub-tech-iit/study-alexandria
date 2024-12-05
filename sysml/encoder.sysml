import Collections::*;

part ENCODER {
    attribute type : Array {
        :>> dimensions default 1; 
        :>> elements : String[dimensions] default ("aea"); 
        }
    attribute portName : Array {
        :>> dimensions default 1; 
        :>> elements : String[dimensions] default ("CONN:P1"); 
        }
    attribute position : Array {
        :>> dimensions default 1;
        :>> elements : String[dimensions] default ("atjoint"); 
        }
    attribute resolution : Array {
        :>> dimensions default 1; 
        :>> elements : Integer[dimensions] default (4096); 
        }
    attribute tolerance : Array {
        :>> dimensions default 1; 
        :>> elements : Real[dimensions] default (0.703); 
        }
}