from lxml import etree
import os
import json
import argparse
from pathlib import Path

def create_xml_node(parent, tag, attrib=None, text=None):
    element = etree.SubElement(parent, tag, attrib if attrib else {})
    if text:
        element.text = text
    return element

def sysml_to_xml(lines, robotName):
    nsmap = {'xi': 'http://www.w3.org/2001/XInclude'}
    root = etree.Element('params', {'robot': robotName, 'build': '1'}, nsmap=nsmap)
    current_package = None
    current_part = None
    current_attribute = None

    stack = []
    count = 0

    for line in lines:
        line = line.strip()
        element = line.split()[0]
        match element:
            case "import":
                include_name = line.split()[1].strip('::*;')
                if include_name[0].istitle() == False:
                    root.insert(0, etree.Element('{http://www.w3.org/2001/XInclude}include', {'href': include_name+".xml"}))
            # case "package":
            #     package_name = line.split()[1].strip('{')
            #     current_package = create_xml_node(root, 'group',  {'name': package_name})
            #     stack.append(current_package)
            case "part":
                c = count
                while lines[c-1].startswith("attribute") or lines[c-1].strip().startswith("}"): # Fix indentation
                    stack.pop()
                    c-=1
                tokens = line.split()
                name = tokens[1].strip(':')
                datatype = None
                attrib = {'name': name}
                if datatype:
                    attrib['type'] = datatype
                if '[' in line and ']' in line:  # Handle multiplicity
                    multiplicity = line[line.index('[') + 1:line.index(']')]
                    # current_part.set('multiplicity', multiplicity)
                if ':' in tokens: # Verify if the part is a specification 
                    inher = tokens[3].strip(':')
                    if inher == 'device':
                        device_type = tokens[5].strip("=")
                        root = etree.Element('device', {'name': ' ', 'type': device_type}, nsmap=nsmap)
                else:
                    current_part = create_xml_node(stack[-1] if len(stack) > 0 else root, 'group', attrib)
                    stack.append(current_part)
            case "attribute":
                c = count
                while lines[c-1].startswith("attribute") or lines[c-1].strip().startswith("}"): # Fix indentation
                    stack.pop()
                    c-=1
                tokens = line.split()
                name = tokens[1]
                datatype = None
                value = None
                if '='  in line: # The attribute has a default value
                    value = tokens[5].strip(';') if len(tokens) > 5 else None
                attrib = {'name': name}
                if datatype:
                    attrib['type'] = datatype
                current_attribute = create_xml_node(stack[-1] if len(stack) > 0 else root, 'param', attrib, value)
                if '[' in line and ']' in line:  # Handle multiplicity
                    multiplicity = line[line.index('[') + 1:line.index(']')]
                    current_attribute.set('multiplicity', multiplicity) 
        count += 1
    return root

def write_xml_to_file(root, output_filename):
    etree.indent(root, space='    ')
    doctype = '<!DOCTYPE params PUBLIC "-//YARP//DTD yarprobotinterface 3.0//EN" "http://www.yarp.it/DTD/yarprobotinterfaceV3.0.dtd">'
    xml_object = etree.tostring(root, pretty_print=True, xml_declaration=True, encoding='UTF-8', doctype=doctype)
    with open(output_filename, "wb") as writer:
        writer.write(xml_object)

def create_files_for_part(robot_name, part_data):
    parser = argparse.ArgumentParser(description="")
    parser.add_argument(
    "--config",
    type=lambda p: Path(p).absolute(),
    required=True,
    help="Path to the configuration files.",
    )
    args = parser.parse_args()
    
    sysml_files = [f for f in os.listdir(args.config) if f.endswith('.sysml')]
    filenames_without_ext = [os.path.splitext(f)[0] for f in sysml_files]
    
    for section, details in part_data.items():
        dir_path = os.path.join(robot_name, details["path"])
        os.makedirs(dir_path, exist_ok=True)
        for file_name in details["files"]:
            for file in filenames_without_ext:
                if file == section:
                    file_path = os.path.join(dir_path, file_name)
                    sysml_file_path = os.path.join(args.config, file + ".sysml")
                    with open(sysml_file_path, 'r') as f:
                        sysml_lines = f.readlines()
                    xml_root = sysml_to_xml(sysml_lines, robot_name)
                    write_xml_to_file(xml_root, file_path)

def extract_general_params(robot_info, part_info):
    for robot_type, robot_list in robot_info.items():
        for robot in robot_list:
            name = robot['robotName']
            version = robot['robotVersion']
            parts = robot["parts"]

            for part in parts:
                if part in part_info:
                    part_data = part_info[part]
                    create_files_for_part(name, part_data)

def main():
    with open('general.json', 'r') as robot_info_file:
        robot_info = json.load(robot_info_file)
    
    with open('par.json', 'r') as part_info_file:
        part_info = json.load(part_info_file)

    extract_general_params(robot_info, part_info)

if __name__ == "__main__":
    main()