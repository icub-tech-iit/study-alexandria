part dragonfly : device {
    attribute folder_name : String default "camera/";
    attribute width : Integer default 320;
    attribute height : Integer default 240;
    attribute video_type : Integer default 1;
    attribute white_balance : Array {
        :>> dimensions default 2;
        :>> elements : Real[dimensions] default (0.540, 0.660);
    }
    attribute framerate : Integer default 30;
    attribute gain : Real default 0.0;
    attribute shutter : Real default 0.9;
    attribute brightness : Real default 1;
    attribute DR2 : Boolean default true;
    attribute stamp : Boolean default true;
    attribute sharpness : Real default 0.5;
    attribute hue : Real default 0.48;
    attribute gamma : Real default 0.229;
    attribute saturation : Real default 0.271;
    attribute guid : String default "guid";
}