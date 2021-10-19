#!/usr/bin/env python3

import fileinput
import argparse
from lib.parser import interactor, filer_rarser


def parse_args():
    parser = argparse.ArgumentParser(description='Command line arguments')
    parser.add_argument('-i', '--input', help='Input file, stdin by default', default=None)
    parser.add_argument('-o', '--output', help='Output file, stdout by default; ignored if no input specified', default=None)
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    if args.input:
        with open(args.input, 'r') as input_data:
            with open(args.output, 'w+') as output_data:
                try:
                    output_data.write(str(filer_rarser.parse(input_data.read())))
                except Exception as e:
                    output_data.write(str(e.args[0]) + '\n')
    else:
        while True:
            try:
                line = input('>>> ')
                result = interactor.parse(line)
                print(result)
            except Exception as e:
                print(e.args[0])
