from base import BaseClass

class PC104(BaseClass):
    def __init__(self, root_path):
        super().__init__()

        self.folder_name = str
        self.PC104IpAddress = str
        self.PC104IpPort = int
        self.PC104TXrate = int
        self.PC104RXrate = int

    @classmethod
    def from_sysml(cls, root_path):
        return super().from_sysml(root_path)
    
    def to_xml(self, root_path, file_name):
        root = super().to_xml(root_path, file_name)

        self.generate_xml(root, root_path, file_name)

def main():
    pass

if __name__ == '__main__':
    main()
