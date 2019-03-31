"""
Manage with eggs.txt
"""
from configparser import ConfigParser

from .common import get_version
from .output import output

EGGS_TXT = 'eggs.txt'


class Basket:
    def __init__(self):
        self.config = ConfigParser()

    def open(self):
        self.config.read(EGGS_TXT)

    def close(self):
        with open(EGGS_TXT, 'w') as f:
            eggs = self.format()
            f.write(eggs)
            f.write('\n')
        output(eggs)

    def sections(self):
        return self.config.sections()

    def section(self, section):
        return self.config[section] if section in self.config else None

    def section_of(self, egg):
        for s in self.config.sections():
            if egg in self.config[s]:
                return s
        return None

    def add(self, eggs, results, section):
        for egg in eggs:
            egg = egg.split('==')[0].lower()
            index = self.section_of(egg)
            if index:
                self.config[index].pop(egg, None)
                if not self.config[index]:
                    del self.config[index]
            if section not in self.config:
                self.config[section] = {}
            self.config[section][egg] = get_version(results, egg)

    def remove(self, eggs):
        for egg in eggs:
            egg = egg.split('==')[0].lower()
            index = self.section_of(egg)
            if index:
                self.config[index].pop(egg, None)
                if not self.config[index]:
                    del self.config[index]

    def update(self, eggs, results):
        for egg in eggs:
            egg = egg.split('==')[0].lower()
            index = self.section_of(egg)
            self.config[index][egg] = get_version(results, egg)

    def show(self):
        self.open()
        output(self.format())

    def format(self):
        items = []
        for section in self.config.sections():
            eggs = ['{0} = {1}'.format(key, value) for key, value in self.config[section].items()]
            if eggs:
                eggs.sort()
            eggs.insert(0, '[{}]'.format(section))
            items.append('\n'.join(eggs))
        return '\n\n'.join(items)
