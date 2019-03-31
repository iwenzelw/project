import subprocess
import sys

from .output import output, ERROR


def run_command(*cmd):
    output('>>' + ' '.join(cmd))
    try:
        return subprocess.check_output(cmd).decode()
    except subprocess.CalledProcessError as e:
        output(e, ERROR)
        sys.exit(1)


def get_egg(line):
    line = line.lstrip()
    end = line.index(' ')
    name = line[:end].lower()
    version = line[end:].strip()
    return name, version


def get_version(line, e):
    begin = line.index(e) + len(e)
    end = line.index('\n', begin)
    return line[begin: end].strip()
