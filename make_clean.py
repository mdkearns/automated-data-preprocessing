# make_clean is a command line utility program that automatically
# performs common data preprocessing tasks on your uncleaned data sets.
# Author: Matthew D. Kearns
# Usage: python make_clean.py [options] filePath

import argparse
import output

def clean():
    print('CLEANING DATA....')

def add_args(parser):
    parser.add_argument('filePath', metavar='filePath', type=str, help='Path to uncleaned data file')
    parser.add_argument('-v', '--version', action='version', version='v1.0.0')
    parser.add_argument('-a', '--all', action='store_const', const='a', help=output.options['-a'])
    parser.add_argument('-c', '--categorical', action='store_const', const='c', help=output.options['-c'])
    parser.add_argument('-f', '--fields', action='store_const', const='f', help=output.options['-f'])
    parser.add_argument('-i', '--interpolate', action='store_const', const='i', help=output.options['-i'])
    parser.add_argument('-o', '--outliers', action='store_const', const='o', help=output.options['-o'])

def main():

    # create argument parser for [options] and save args to namespace
    parser = argparse.ArgumentParser(description=output.description)
    add_args(parser)
    args = parser.parse_args()

    # clean the supplied data file according to the user-supplied options
    clean()

if __name__ == '__main__':
    main()