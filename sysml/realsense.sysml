part realsense : device {
    attribute folder_name : String default "camera/";
    part SETTINGS {
        attribute depthResolution : Array {
            :>> dimensions default 2;
            :>> elements : Integer[dimensions] default (640, 480);
        }
        attribute rgbResolution : Array {
            :>> dimensions default 2;
            :>> elements : Integer[dimensions] default (640, 480);
        }
        attribute framerate : Integer default 30;
        attribute enableEmitter : Boolean default true;
        attribute needAlignment : Boolean default true;
        attribute alignmentFrame : String default "None";
    }
    part HW_DESCRIPTION {
        attribute clipPlanes : Array {
            :>> dimensions default 2;
            :>> elements : Real[dimensions] default (0.0, 10.0);
        }
    }
}