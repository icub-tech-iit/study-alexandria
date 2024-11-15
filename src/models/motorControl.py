from dataclasses import dataclass
from device import Device

class motorControl(Device):
    def __init__(self):
        super().__init__()

    @dataclass
    class LIMITS:
        jntPosMin = list[int]
        jntPosMax = list[int]
        jntVelMax = list[int]
        motorOverloadCurrents = list[int]
        motorNominalCurrents = list[int]
        motorPeakCurrents = list[int]
        motorPwmLimit = list[int]
    
    @dataclass
    class TIMEOUTS:
        velocity = list[int]

    @dataclass
    class IMPEDANCE:
        stiffness = list[float]
        damping = list[float]

    @dataclass
    class CONTROLS:
        positionControl = list[str]
        velocityControl = list[str]
        mixedControl = list[str]
        torqueControl = list[str]
        currentPid = list[str]
        speedPid = list[str]

    @dataclass
    class POS_PID_DEFAULT:
        controlLaw = str
        outputType = str
        fbkControlUnits = str
        outputControlUnits = str
        kp = list[int]
        kd = list[int]
        ki = list[int]
        maxOutput = list[int]
        maxInt = list[int]
        stictionUp = list[int]
        stictionDown = list[int]
        kff = list[int]