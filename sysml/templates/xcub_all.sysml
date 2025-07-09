part xcub_all {
    attribute folder_name : String default "./";
    attribute pc104 : Array {
        :>> dimensions default 1;
        :>> elements : String[dimensions] default ("hardware/electronics/pc104.xml");
    }
    attribute cartesian : Array {
        :>> dimensions default 2;
        :>> elements : String[dimensions] default ("cartesian/left_arm_cartesian.xml", "cartesian/right_arm_cartesian.xml");
    }
    attribute motorControl_wrapper : Array {
        :>> dimensions default 5;
        :>> elements : String[dimensions] default ("wrappers/motorControl/left_arm_mc_wrapper.xml", "wrappers/motorControl/right_arm_mc_wrapper.xml", "wrappers/motorControl/torso_mc_wrapper.xml", "wrappers/motorControl/head_mc_wrapper.xml", "wrappers/motorControl/face_mc_wrapper.xml");
    }
    attribute motorControl_remapper : Array {
        :>> dimensions default 5;
        :>> elements : String[dimensions] default ("wrappers/motorControl/left_arm_mc_remapper.xml", "wrappers/motorControl/right_arm_mc_remapper.xml", "wrappers/motorControl/torso_mc_remapper.xml", "wrappers/motorControl/head_mc_remapper.xml", "wrappers/motorControl/face_mc_remapper.xml");
    }
    attribute motorControl : Array {
        :>> dimensions default 5;
        :>> elements : String[dimensions] default ("hardware/motorControl/head_eb20_j0_1_mc.xml", "hardware/motorControl/head_eb21_j2_5_mc.xml", "hardware/motorControl/face_eb22_j0_mc.xml", "hardware/motorControl/torso_eb5_j0_2_mc.xml", "hardware/motorControl/left_arm_eb1_j0_3_mc.xml", "hardware/motorControl/left_arm_eb24_j4_7_mc.xml", "hardware/motorControl/left_arm_eb25_j8_11_mc.xml", "hardware/motorControl/left_arm_eb26_j12_15_mc.xml", "hardware/motorControl/right_arm_eb3_j0_3_mc.xml", "hardware/motorControl/right_arm_eb27_j4_7_mc.xml", "hardware/motorControl/right_arm_eb28_j8_11_mc.xml", "hardware/motorControl/right_arm_eb29_j12_15_mc.xml");
    }
    attribute FT : Array {
        :>> dimensions default 4;
        :>> elements : String[dimensions] default ("hardware/FT/left_arm_eb1_j0_3_strain.xml", "hardware/FT/right_arm_eb3_j0_3_strain.xml", "wrappers/FT/left_arm_FT_wrapper.xml", "wrappers/FT/right_arm_FT_wrapper.xml");
    }
    attribute calibrators : Array {
        :>> dimensions default 5;
        :>> elements : String[dimensions] default ("calibrators/left_arm_calib.xml", "calibrators/right_arm_calib.xml", "calibrators/torso_calib.xml", "calibrators/head_calib.xml", "calibrators/face_calib.xml");
    }
}