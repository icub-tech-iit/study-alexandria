from dataclasses import dataclass
from encoder import Encoder
import re

@dataclass
class SERVICE:
    type: list[str]
    class PROPERTIES:
        @dataclass
        class ETHBOARD:
            type: str
        class JOINTMAPPING:
            @dataclass
            class ACTUATOR:
                type: list[str]
                port: list[str]
            class ENCODER1(Encoder):
                def __init__(self):
                    encoder1 = Encoder().from_sysml('/home/mgloria/iit/study-alexandria/sysml/encoder.sysml')
                    super().__init__(**encoder1.__dict__)
            class ENCODER2(Encoder):
                def __init__(self):
                    encoder2 = Encoder().from_sysml('/home/mgloria/iit/study-alexandria/sysml/encoder.sysml')
                    super().__init__(**encoder2.__dict__)
        
    @classmethod
    def from_sysml(cls, file_path):
        with open(file_path, 'r') as file:
            sysml_str = file.read()

        vector_pattern = r'attribute (\w+) :\s*\w+\s*{\s*:\s*>>\s*dimensions\s*default\s*\d+;\s*:\s*>>\s*elements\s*:\s*\w+\[\w+\]\s*default\s*\(([^)]+)\);'
        enc_pattern = r'attribute (\w+) :> (\w+);'
        ser = cls(None)

        def extract_attributes(block, pattern):
            matches = re.findall(pattern, block)
            attributes = {}
            for match in matches:
                key = match[0]
                value = None
                if match[1]:
                    try:
                        value = float(match[1])
                    except ValueError:
                        value = match[1]
                elif match[2]:
                    value = int(match[2])
                else:
                    value = match[3]
                attributes[key] = value
            return attributes
                
        attr = extract_attributes(sysml_str, vector_pattern) | extract_attributes(sysml_str, enc_pattern)
        ser.type = attr['service_type']

        ser.ethboard = cls.PROPERTIES().ETHBOARD(
            type = [attr['eth_type']]
        )

        ser.actuator = cls.PROPERTIES().JOINTMAPPING().ACTUATOR(
            type = [attr['actuator_type']],
            port = [attr['portName']]
        )

        ser.encoder1 = Encoder.from_sysml('/home/mgloria/iit/study-alexandria/sysml/encoder.sysml')
        ser.encoder2 = Encoder.from_sysml('/home/mgloria/iit/study-alexandria/sysml/encoder.sysml')
        return ser
    
def main():
    serv = SERVICE.from_sysml('/home/mgloria/iit/study-alexandria/sysml/service.sysml')
    print(serv.encoder2.position)

if __name__ == '__main__':
    main()