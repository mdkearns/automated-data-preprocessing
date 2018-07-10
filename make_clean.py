# make_clean is a command line utility program that automatically
# performs common data preprocessing tasks on your uncleaned data sets.
# Author: Matthew D. Kearns
# Usage: python make_clean.py [options] filePath

import argparse
import output
import pandas as pd
import numpy as np

def clean(args):
    print('CLEANING DATA....\n')

    if args.missing:
        print(args.filePath, 'doesn\'t contain field names.\n')
        df = pd.read_csv(args.filePath, header=None)
    else:
        print(args.filePath, 'contains field names.\n')
        df = pd.read_csv(args.filePath, header=0)

    if args.categorical or args.all:
        # get list of fields that are continuous and transform categorical fields
        real = [i for i in range(len(df.iloc[0])) if type(df.iloc[0, i]) != str]
        print('Transforming categorical data using one-hot encoding...', end='')
        df = pd.get_dummies(df)
        print('ok')

    print(df.head())

    if args.interpolate or args.all:
        print('Detecting missing values...', end='')
        df.replace('?', np.nan)
        print('ok')
        print('Imputing missing values...', end='')
        # perform computation
        print('ok')

    if args.outliers or args.all:
        print('Detecting outliers...', end='')
        # perform computation
        print('ok')
        print('Removing outliers...', end='')
        # perform computation
        print('ok')

    print('\nDONE.')

def add_args(parser):
    parser.add_argument('filePath', metavar='filePath', type=str, help='Path to uncleaned data file')
    parser.add_argument('-v', '--version', action='version', version='v1.0.0')
    parser.add_argument('-a', '--all', action='store_const', const='a', help=output.options['-a'])
    parser.add_argument('-c', '--categorical', action='store_const', const='c', help=output.options['-c'])
    parser.add_argument('-i', '--interpolate', action='store_const', const='i', help=output.options['-i'])
    parser.add_argument('-m', '--missing', action='store_const', const='m', help=output.options['-m'])
    parser.add_argument('-o', '--outliers', action='store_const', const='o', help=output.options['-o'])

def main():

    # create argument parser for [options] and save to namespace
    parser = argparse.ArgumentParser(description=output.description)
    add_args(parser)
    args = parser.parse_args()

    # clean the supplied data file according to the user-supplied options
    clean(args)

if __name__ == '__main__':
    main()