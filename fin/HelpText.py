from fin.Config import Config
CLINAME = "fin"

class HelpText(object):
    def __init__(self):
        self.text = ""
        self.usage_list=[]
        self.options = ""

    def create_usage(self):
        text = "usage: \n"
        for item in self.usage_list:
            text += '   ' + item + '\n'
        return text

    def add_usage(self, name, opt=None, arg=None):
        text = "{cliname} {name}".format(cliname=CLINAME, name=name)
        if opt:
            text += ' [options]'
        if arg:
            text += ' [ARG ...]'
        self.usage_list.append(text)

    def create_options(self, substitute):
        text = "Options: \n"
        options = {}
        for key in substitute:
            item = key.split('__')
            if len(item)>1:
                short = item[1]
                long = item[0]
            else:
                short = None
                long = item[0]
            try:
                explain = substitute[key][1]
            except TypeError:
                explain = ""
            if short:
                item = '-{short}, --{long} <{long}>        {explain}'.format(short=short, long=long, explain=explain)
            else:
                item = '--{long} <{long}>        {explain}'.format(long=long, explain=explain)
            text += '   ' + item + '\n'
        self.options = text
        return self.options

def default_helptext():
    helptext = HelpText()
    helptext.add_usage('--fin')
    usage = helptext.create_usage()
    return usage

def build_helptext(config):
    default = config.get_default()
    substitute = config.substitute
    helptext = HelpText()
    options = helptext.create_options(substitute)
    helptext.add_usage('<service_name>', opt=True, arg=True)
    for item in config.yaml()['services']:
        helptext.add_usage(item, opt=True, arg=True)
    helptext.add_usage('--help')
    usage = helptext.create_usage()
    helptext = usage + '\n\n' + options
    helptext += '\n    --help'
    return helptext

if __name__ == "__main__":
    build_helptext()





