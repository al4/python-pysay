from __future__ import print_function
import argparse
from .ascii_art import py_format

print('pysay imported!')


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('text', help='Text to pysay')
    return parser.parse_args()


def main():
    print('This is the main function')
    args = parse_args()
    print(py_format(args.text))
