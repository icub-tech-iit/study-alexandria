import os
from lxml import etree
from pathlib import Path
from parsers.sysml_parser import SysMLParser
from models.robot import Robot
from models.part import Part

class FileGenerator:
    def __init__(self, config_path):
        self.config_path = Path(config_path).absolute()
        self.sysml_parser = SysMLParser()

    def load_sysml_files(self):
        return [f for f in os.listdir(self.config_path) if f.endswith('.sysml')]
    
    def write_xml_to_file(self, root, output_filename):
        etree.indent(root, space='    ')
        doctype = '<!DOCTYPE params PUBLIC "-//YARP//DTD yarprobotinterface 3.0//EN" "http://www.yarp.it/DTD/yarprobotinterfaceV3.0.dtd">'
        xml_object = etree.tostring(root, pretty_print=True, xml_declaration=True, encoding='UTF-8', doctype=doctype)
        with open(output_filename, "wb") as writer:
            writer.write(xml_object)

    def generate_files_for_robot(self, robot: Robot, part_data):
        sysml_files = self.load_sysml_files()
        filenames_without_ext = [os.path.splitext(f)[0] for f in sysml_files]

        for part_name, details in part_data.items():
            for item_name, item_details in details.items():
                part = Part(part_name, item_details["path"], item_details["files"])
                dir_path = os.path.join(robot.name, part.path)
                os.makedirs(dir_path, exist_ok=True)
                for file_name in part.files:
                    if item_name in filenames_without_ext:
                        sysml_file_path = os.path.join(self.config_path, f"{item_name}.sysml")
                        file_path = os.path.join(dir_path, file_name)
                        with open(sysml_file_path, 'r') as f:
                            sysml_lines = f.readlines()
                        xml_root = self.sysml_parser.parse_sysml_to_xml(sysml_lines, robot.name)
                        self.write_xml_to_file(xml_root, file_path)

