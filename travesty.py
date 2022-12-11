#!/usr/bin/python3

import sys

if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")

import argparse
from travestylib import Travesty

# modify these if index range error
DEFAULT_ARRAYSIZE = 1000
DEFAULT_PATTERN_LENGTH = 9
DEFAULT_PATTERN_LENGTH_MAX = 15
DEFAULT_PATTERN_LENGTH_MIN = 3
DEFAULT_OUTCHARS = 7000
DEFAULT_LINE_WIDTH = 50

def pattern_length_type(astr, pat_len_min=DEFAULT_PATTERN_LENGTH_MIN, pat_len_max=DEFAULT_PATTERN_LENGTH_MAX):
    value = int(astr)
    if pat_len_min > value:
        print("WARN: pattern-length ({value}) is less than minimum allowed ({DEFAULT_PATTERN_LENGTH_MIN})")
        value = pat_len_min
    if pat_len_max < value:
        print("WARN: pattern-length ({value}) is greater than maximum allowed ({DEFAULT_PATTERN_LENGTH_MAX})")
        value = pat_len_max

    return value

parser = argparse.ArgumentParser(description='Analyzes input text and then randomly generates text output based on the pattern porbablity.')
parser.add_argument('-p', '--pattern-length',
                    metavar='pattern_length',
                    dest='pattern_length',
                    type=pattern_length_type,
                    nargs='?',
                    default=DEFAULT_PATTERN_LENGTH,
                    help='Pattern Length')
parser.add_argument('-b', '--buffer-size',
                    metavar='buffer_size',
                    dest='buffer_size',
                    type=int,
                    nargs='?',
                    default=DEFAULT_ARRAYSIZE,
                    help='The size of the buffer to be analyzed. The larger this is the slower the output will appear')
parser.add_argument('-o', '--output-size',
                    metavar='out_size',
                    dest='out_chars',
                    type=int,
                    nargs='?',
                    default=DEFAULT_OUTCHARS,
                    help='Number of characters to output')
parser.add_argument('-l', '--line-width',
                    metavar='line_width',
                    dest='line_width',
                    type=int,
                    nargs='?',
                    default=DEFAULT_LINE_WIDTH,
                    help='Approximate line length to output')
parser.add_argument('-d', '--debug',
                    action='store_true',
                    dest='debug',
                    default=False,
                    help='Print debugging info')
parser.add_argument('--verse',
                    action='store_true',
                    dest='use_verse',
                    default=False,
                    help='Sets output to verse mode, defaults to prose')
parser.add_argument('input_file',
                    nargs='?',
                    help='Sets the input file to use')
parser.add_argument('-V', '--version',
                    action='version',
                    version='%(prog)s 1.0.0')

args = parser.parse_args()

travesty = Travesty(args.buffer_size,
                    args.pattern_length,
                    args.out_chars,
                    args.line_width,
                    args.use_verse,
                    args.debug,
                    args.input_file)

travesty.execute()
