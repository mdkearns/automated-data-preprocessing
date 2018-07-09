# make_clean is a command line utility program that automatically
# performs common data preprocessing tasks on your uncleaned data sets.

# Usage: python make_clean.py [options] /file/path/to/data/

import argparse
import sys
import output

def all():
    print("ALL")

def main():

    parser = argparse.ArgumentParser(description=output.description)

    parser.add_argument('filePath', metavar='filePath', type=str, help='Path to uncleaned data file')
    parser.add_argument('-a', '--all',         action='store_const', const='a', help=output.options['-a'])
    parser.add_argument('-c', '--categorical', action='store_const', const='c', help=output.options['-c'])
    parser.add_argument('-f', '--fields',      action='store_const', const='f', help=output.options['-f'])
    parser.add_argument('-i', '--interpolate', action='store_const', const='i', help=output.options['-i'])
    parser.add_argument('-o', '--outliers',    action='store_const', const='o', help=output.options['-o'])
    parser.add_argument('-v', '--version',     action='version', version='v1.0.0')

    args = parser.parse_args()

    print(args)

    # if sys.argv[-1] == '--help':
    #     print(output.info)
    #     print(output.description)
    #     print(output.usage)


if __name__ == '__main__':
    main()