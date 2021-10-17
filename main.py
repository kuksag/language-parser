#!/usr/bin/env python3

import argparse
import sys
from lib.parser import *


def parse_args():
    parser = argparse.ArgumentParser(description='Command line arguments')
    parser.add_argument('-i', '--input', help='input file, stdin by default', default=sys.stdin)
    parser.add_argument('-o', '--output', help='output file, stdout by default', default=sys.stdout)
    return parser.parse_args()


if __name__ == '__main__':
    print(atom.parse('abcd'))
    print(atom.parse('abcd {defg}'))
    print(atom.parse('abcd {defg, xyz}'))
    print(atom.parse('abcd {defg, xyz {vbn}}'))
