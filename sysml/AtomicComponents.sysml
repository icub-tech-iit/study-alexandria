package AtomicComponents {
    import ScalarValues::*;
    attribute def phase {
		attribute level : Integer;
		attribute type : String;
		attribute target : String;
	}
	part def device {
		attribute type : String;
		attribute Phase : phase [4];
	}
	part embObjMotionControl {}
	part parametricCalibratorEth {}
	part def service {}
}
