part wrapper : device {
    attribute folder_name : String default "wrappers/";
    attribute period : Real default 0.01;
    attribute portName : String default "/robot/part";
    part startup : actionPhase;
    part shutdown : phase;
}