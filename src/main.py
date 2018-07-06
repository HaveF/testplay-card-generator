#!/usr/bin/python
# -*- coding: utf-8 -*-

''' Simple Entry Point for Testplay Card Generator on CLI '''


import sys
import os
import argparse

here = os.path.dirname(os.path.abspath(__file__))
sys.path.append(here)

from drawing.engine import TestCardGeneratorEngine

import logging
logging.basicConfig(level=logging.DEBUG)


def _parse_args(argv=sys.argv[1:]):
    parser = argparse.ArgumentParser(
        description='testplay card generator (alpha version)',
        add_help=True)
    parser.add_argument('--layout', required=True,
                        help='card layout file (only utf8 yml format supported)')
    parser.add_argument('--data', required=True,
                        help='card contents file (only utf8 csv supported)')
    parser.add_argument('--output', required=True,
                        help='output file name')
    parser.add_argument('--quiet', action='store_true',
                        help='If enabled, no output the progress')
    return parser.parse_args(argv)


if __name__ == '__main__':
    args = _parse_args()
    TestCardGeneratorEngine.run(
        layoutfile=args.layout, datafile=args.data, output=args.output, is_quiet=args.quiet)