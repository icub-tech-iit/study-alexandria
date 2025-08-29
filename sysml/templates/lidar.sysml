part lidar : device {
    attribute folder_name : String default "sensors/";
    part GENERAL {
        attribute name : String default "rpLidar4";
        attribute serial_baudrate : Integer default 1000000;
        attribute serial_port : String default "/dev/ttyUSB0";
        attribute sample_buffer_life : Integer default 1;
    }
    part SENSOR {
        attribute max_distance : Real default 30.0;
        attribute min_distance : Real default 0.1;
        attribute max_angle : Integer default 360;
        attribute min_angle : Integer default 0;
        attribute resolution : Real default 0.12;
        attribute allow_infinity : Real default 1;
    }
    part RPLIDAR {
        attribute scan_mode : String default "DenseBoost";
    }
}