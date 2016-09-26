"""
Usage:
    fin <app> [-d something] [-h something] [-p some] [-v some] [-i asf] [-n asf] [SHELL ...]
    fin db [-p port] [-i image] [-v volume_dir] [-n container_name]

Options:
    -d <dbname>
    -h <host>
    -p <port>
    -i <image>
    -n <name>
    -c <checkout>
    -v <volume>

"""
import argparse
import subprocess
import fcntl
import os
from docopt import docopt
from fin.HelpText import build_helptext
from fin.Config import Config
from subprocess import call, PIPE


def local(command):
    print("run command:")
    print(command)
    print()
    proc = subprocess.Popen(command, shell=True)
    proc.communicate()

def main():
    try:
        # helptext = build_helptext(config)
        config = Config('Fin.yaml')
    except FileNotFoundError:
        raise FileNotFoundError("Fin.yaml or default.yaml can not be found in the current directory")
    helptext = build_helptext(config)
    argu = docopt(helptext, help=False)
    if argu['--help']:
      print(helptext)

    run_opts = config.run_options()
    import ipdb;ipdb.set_trace()
