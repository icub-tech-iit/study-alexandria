from dataclasses import dataclass

class Mechanicals:
    @dataclass
    class GENERAL:
        MotioncontrolVersion = int
        Joints = int
        AxisMap = list[int]
        AxisName = list[str]
        AxisType = list[str]
        Encoder = list[float]
        fullscalePWM = list[int]
        ampsToSensor = list[float]
        Gearbox_M2J = list[float]
        Gearbox_E2J = list[int]
        useMotorSpeedFbk = list[int]
        MotorType = list[str]
        Verbose = int

    @dataclass
    class LIMITS:
        hardwareJntPosMin = list[int]
        hardwareJntPosMax = list[int]
        rotorPosMin = list[int]
        rotorPosMax = list[int]

    @dataclass
    class COUPLINGS:
        matrixJ2M = list[list[float]]
        matrixM2J = list[list[float]]
        matrixE2J = list[list[float]]

    @dataclass
    class JOINTSET_CFG:
        numberofsets = int

        @dataclass
        class JOINTSET_0:
            listofjoints = list[int]
            constraintName = str
            param1 = int
            param2 = int
