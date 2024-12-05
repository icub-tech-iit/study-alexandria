from lxml import etree

class SysMLParser:
    def create_xml_node(self, parent, tag, attrib=None, text=None):
        element = etree.SubElement(parent, tag, attrib if attrib else {})
        if text:
            element.text = text
        return element

    def parse_sysml_to_xml(self, lines, robot_name):
        nsmap = {'xi': 'http://www.w3.org/2001/XInclude'}
        root = etree.Element('params', {'robot': robot_name, 'build': '1'}, nsmap=nsmap)
        current_part, current_attribute = None, None
        stack, count = [], 0

        for line in lines:
            line = line.strip()
            element = line.split()[0]
            match element:
                case "import":
                    include_name = line.split()[1].strip('::*;')
                    if not include_name[0].istitle():
                        root.insert(0, etree.Element('{http://www.w3.org/2001/XInclude}include', {'href': f"{include_name}.xml"}))
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
                        current_part = self.create_xml_node(stack[-1] if len(stack) > 0 else root, 'group', attrib)
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
                    current_attribute = self.create_xml_node(stack[-1] if len(stack) > 0 else root, 'param', attrib, value)
                    if '[' in line and ']' in line:  # Handle multiplicity
                        multiplicity = line[line.index('[') + 1:line.index(']')]
                        current_attribute.set('multiplicity', multiplicity)
            count += 1
        return root
