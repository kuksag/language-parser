#!/usr/bin/env python3

import argparse
import sys
from lib.parser import *
from lib.base import *


def parse_args():
    parser = argparse.ArgumentParser(description='Command line arguments')
    parser.add_argument('-i', '--input', help='Input file, stdin by default', default=sys.stdin)
    parser.add_argument('-o', '--output', help='Output file, stdout by default', default=sys.stdout)
    return parser.parse_args()


if __name__ == '__main__':
    print(relation.parse('abc () {cde (gde)}'))
    print(relation.parse('abc (x, y, z {t, y}) {[cde (gde) && [o () || p ()]]}'))
