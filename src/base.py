from lxml import etree
from dataclasses import fields, is_dataclass
from phase import Phase
from action import Action
from encoder import Encoder
from utils import check_subfolders_existance, parse_sysml

class BaseClass:
    def __init__(self):
        self.is_device = False
        self.includes = []
        self.folder_name = str

    @classmethod
    def from_sysml(cls, root_path):
        class_name = cls.__name__.lower()
        template_file = f'{root_path}/templates/{class_name}.sysml'
        attr = dict(parse_sysml(template_file).part_definitions.items())
        phase_keys = ['startup', 'interrupt1', 'interrupt3', 'shutdown']
        encoder_keys = ['ENCODER1', 'ENCODER2']
        cls_instance = cls(root_path)

        def _set_parameters(instance, attributes):
            for key, value in attributes.items():
                if hasattr(instance, key) and key in phase_keys:
                    phase_instance = getattr(instance, key)
                    if phase_instance is Action:
                        setattr(instance, key, Action.from_sysml(root_path))
                    elif phase_instance is Phase:
                        setattr(instance, key, Phase.from_sysml(root_path))
                elif key in encoder_keys:
                    setattr(instance, key, Encoder.from_sysml(root_path))
                elif hasattr(instance, key):
                    subclass = getattr(instance, key)
                    if is_dataclass(subclass):
                        params = {param: [x for x in val['value'].strip("()").split(',')] if isinstance(val, dict) else val.strip('"')
                                    for param, val in value.parameters.items()}
                        setattr(instance, key, subclass(**params))
                    if value.children:
                        _set_parameters(getattr(instance, key), {child: value.children[child] for child in value.children})
                elif key.lower() == class_name:
                    for param, param_value in value.parameters.items():
                        if isinstance(param_value, dict) and 'value' in param_value:
                            setattr(instance, param, [x.strip() for x in param_value['value'].strip("()").split(',')])
                        else:
                            setattr(instance, param, param_value.strip('"'))

        _set_parameters(cls_instance, attr)
        return cls_instance

    def to_xml(self, root_path, file_name):
        root, xi_ns = self._define_root()
        check_subfolders_existance(root_path, file_name)

        def _dataclass_to_xml(parent, name, dataclass_instance):
            group_elem = etree.SubElement(parent, "group", {"name": name.strip('_')})
            for field in fields(dataclass_instance):
                field_name = field.name
                field_value = getattr(dataclass_instance, field_name)
                
                if is_dataclass(field_value):
                    _dataclass_to_xml(group_elem, field_name, field_value) 
                elif isinstance(field_value, list):
                    if any(isinstance(i, list) for i in field_value):
                        param = etree.SubElement(group_elem, "param", {"name": field_name.strip('_')})
                        formatted_text = "\n".join(
                            "   ".join(map(str, row)) for row in field_value
                        )
                        param.text = f"\n{formatted_text}\n"
                    else:
                        param = etree.SubElement(group_elem, "param", {"name": field_name.strip('_')})
                        param.text = "   ".join(map(str, field_value))
                elif field_name == 'temperature_acquisitionRate': # Special case since sysml doesn't support - in attribute names
                    param = etree.SubElement(group_elem, "param", {"name": 'temperature-acquisitionRate'})
                    param.text = str(field_value)
                else:
                    param = etree.SubElement(group_elem, "param", {"name": field_name.strip('_')})
                    param.text = str(field_value)

        for attr_name, attr_value in self.__dict__.items():
            if self._skip_cases(attr_name) or isinstance(attr_value, Phase) or isinstance(attr_value, Action) or isinstance(attr_value, Encoder):
                continue
            elif attr_name == 'includes':	
                self._add_includes(attr_value, root)
            elif is_dataclass(attr_value):
                _dataclass_to_xml(root, attr_name, attr_value)
            else:
                param = etree.SubElement(root, "param", {"name": attr_name.strip('_')})
                param.text = "   ".join(map(str, attr_value)) if isinstance(attr_value, list) else str(attr_value)

        return root
    
    def _skip_cases(self, attr_name):
        return attr_name in ['device_type', 'device_name', 'folder_name', 'is_device', 'elementName', 'elementValue']
    def _add_includes(self, includes, root):
        xi_ns = 'http://www.w3.org/2001/XInclude'
        if isinstance(includes, list):
            return [etree.SubElement(root, f'{{{xi_ns}}}include', href=inc.strip('"')) for inc in includes]
        else:
            return etree.SubElement(root, f'{{{xi_ns}}}include', href=includes.strip('"'))    
    def _extra_attributes(self, extra_attr):
        return etree.XML(extra_attr.to_xml())
    
    def _define_root(self):
        xi_ns = 'http://www.w3.org/2001/XInclude'
        nsmap = {'xi': xi_ns}
        if self.is_device:
            root = etree.Element('device', {'name': str(self.device_name).strip('"'), 'type': str(self.device_type).strip('"')}, nsmap=nsmap)
        else:
            root = etree.Element('params', {'robot': '', 'build': '1'}, nsmap=nsmap)
        return root, xi_ns
    
    def generate_xml(self, root, root_path, file_name):
        etree.indent(root, space='    ')
        if self.is_device:
            doctype = '<!DOCTYPE devices PUBLIC "-//YARP//DTD yarprobotinterface 3.0//EN" "http://www.yarp.it/DTD/yarprobotinterfaceV3.0.dtd">'
        else:
            doctype = '<!DOCTYPE params PUBLIC "-//YARP//DTD yarprobotinterface 3.0//EN" "http://www.yarp.it/DTD/yarprobotinterfaceV3.0.dtd">'
        xml_object = etree.tostring(root, pretty_print=True, xml_declaration=True, encoding='UTF-8', doctype=doctype)
        with open(root_path+"/"+file_name, "wb") as writer:
            writer.write(xml_object)
