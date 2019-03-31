#!/usr/bin/env python
'''Generate files from Jinja2 templates and environment variables.'''

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from jinja2 import Environment
from os import environ
from sys import stdin, stdout
import argparse
from argparse import ArgumentParser
import template.filters


def render(template_string):
    env = Environment()
    # Add all functions in template.filters as Jinja filters.
    for tf in filter(lambda x: not x.startswith('_'), dir(template.filters)):
        env.filters[tf] = template.filters.__getattribute__(tf)
    t = env.from_string(template_string)
    return t.render(environ)


def main():
    parser = ArgumentParser(
        description='''A CLI tool for generating files from Jinja2 templates
        and environment variables.''')
    parser.add_argument('filename',
                        help='Input filename',
                        type=argparse.FileType('r'),
                        nargs='?')
    parser.add_argument('-o', '--output',
                        help='Output to filename',
                        type=argparse.FileType('w'))
    args = parser.parse_args()
    infd = args.filename if args.filename else stdin
    outfd = args.output if args.output else stdout
    print(render(infd.read()), file=outfd)


if __name__ == '__main__':
    main()
