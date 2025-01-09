abstract part torso {
    part calibration [1] :> calibrator;
    part calibrator1 subsets calibrator = "torso-calib.xml";
}