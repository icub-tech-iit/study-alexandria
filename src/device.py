from dataclasses import dataclass
from base import BaseClass

@dataclass
class Device(BaseClass):
    device_type: str = ""
    device_name: str = ""

    def __post_init__(self):
        super().__init__()
        self.is_device = True
        
    @classmethod
    def from_sysml(cls, root_path):
        return super().from_sysml(root_path)
    
    def to_xml(self, root_path, file_name):
        root = super().to_xml(root_path, file_name)
        super().generate_xml(root, root_path, file_name)

        return root
    
def main():
    pass

if __name__ == '__main__':
    main()