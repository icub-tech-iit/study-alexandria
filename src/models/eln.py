from dataclasses import dataclass

class Electronics:
    class ETH_BOARD:
        @dataclass
        class ETH_BOARD_PROPERTIES:
            IpAddress = str
            IpPort = int
            Type = str
            maxSizeRXpacket = str
            maxSizeROP = str
        
        @dataclass
        class ETH_BOARD_SETTINGS:
            Name = str

            @dataclass
            class RUNNINGMODE:
                period = int
                maxTimeOfRXactivity = int
                maxTimeOfDOactivity = int
                maxTimeOfTXactivity = int
                TXrateOfRegularROPs = int
        
        class ETH_BOARD_ACTIONS:
            @dataclass
            class MONITOR_ITS_PRESENCE:
                enabled = bool
                timeout = float
                periodOfMissingReport = float