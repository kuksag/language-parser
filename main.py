#!/usr/bin/env python3

import fileinput
import argparse
from lib.parser import main


def parse_args():
    parser = argparse.ArgumentParser(description='Command line arguments')
    parser.add_argument('-i', '--input', help='Input file, stdin by default', default=None)
    parser.add_argument('-o', '--output', help='Output file, stdout by default; ignored if no input specified', default=None)
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    if args.input:
        with open(args.output, 'w+') as output:
            for line in fileinput.input(args.input):
                try:
                    output.write(str(main.parse(line)) + '\n')
                except Exception as e:
                    output.write(str(e.args[0]) + '\n')
    else:
        while True:
            try:
                line = input('>>> ')
                result = main.parse(line)
                print(result)
            except Exception as e:
                print(e.args[0])
