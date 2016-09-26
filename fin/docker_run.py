def local(command):
    print "run command:"
    print command
    print
    proc = subprocess.Popen(command, shell=True)
    proc.communicate()

class Run:
    def __init__(self, options="", image="", command="", arg=""):
        self.text = "docker run{options} {image} {command} {arg}"
        self.image = image
        self.options = options
        self.command = command
        self.arg = arg

    def add_option(self, option_name, value=None):
        self.options += ' option_name'
        if value:
            self.options += value

    def add_port(self, host, container):
        text = ' -p {host}:{container}'.format(host=host, container=container)
        self.options += text

    def add_volume(self, host, container):
        text = ' -v {host}:{container}'.format(host=host, container=container)
        self.options += text

    def add_env(self, key, value):
        text = ' -e {key}={value}'.format(key=key, value=value)
        self.options += text

    def get_command(self):
        text = self.text.format(options=self.options, image=self.image, command=self.command, arg=self.arg)
        return text





def run(service_config):
    pass



