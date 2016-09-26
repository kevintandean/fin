import yaml
import ruamel.yaml
from string import Formatter

class Config:
    def __init__(self, file):
        self.file = self.read_file(file)
        self.default = self.get_default()
        self.substitute = self.build_substitute_keys(self.yaml(), self.default)

    def read_file(self, path):
        with open(path, 'r') as filee:
            read = filee.read()
        return read

    def build_substitute_keys(self, template, default):
        fmt = Formatter()
        import ipdb;ipdb.set_trace()
        parsed = fmt.parse(template)
        data = {}
        for item in parsed:
            if item[1]:
                split = item[1].split('__')
                default_key = split[0]
                value = default.get(default_key, None)
                if value:
                    try:
                        comment = default.ca.items[default_key][2].value
                    except KeyError:
                        comment = ""
                        pass
                    value = [value, comment]
                data[item[1]] = value
        return data

    def yaml(self):
        yam = yaml.safe_load(self.file)
        return yam

    def get_default(self):
        text = self.read_file('default.yaml')
        yam = ruamel.yaml.load(text, ruamel.yaml.RoundTripLoader)
        return yam




def get_options(config):
    yam = yaml.safe_load(config)
    options = yam['OPTIONS']
    return options

def build_substitute_keys(template):
    fmt = Formatter()
    parsed = fmt.parse(template)
    data = {}
    for item in parsed:
        if item[1]:
            data[item[1]] = None
    return data

