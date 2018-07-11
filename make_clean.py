# make_clean is a command line utility program that automatically
# performs common data preprocessing tasks on your uncleaned data sets.
# Author: Matthew D. Kearns
# Usage: python make_clean.py [options] filePath

import argparse
import text
import numpy as np
import pandas as pd
from utilities import *

def clean(args):
    """Load and clean user-supplied data."""

    print('CLEANING DATA....')

    # load data as a pandas data frame
    df = load_csv(args.filePath, missing_headers=args.missing)

    # get lists of fields that are continuous and discrete
    real = [i for i in range(len(df.iloc[0])) if type(df.iloc[0, i]) != str]
    discrete = [i for i in range(len(df.iloc[0])) if type(df.iloc[0, i]) == str]

    # interpolate missing data values
    if args.interpolate or args.all:
        print('\tDetecting missing values...')
        df = replace_missing_data(df)
        print('\tImputing missing values...')
        df = interpolate_missing_data(df, real, discrete)

    # detect and remove outliers
    if args.outliers or args.all:
        print('\tRemoving outliers...')
        df = remove_outliers(df, real)

    # one-hot encode the categorical variables
    if args.categorical or args.all:
        print('\tTransforming categorical data using one-hot encoding...')
        df = one_hot_encode(df)

    # save cleaned data file to same directory as uncleaned version
    df.to_csv(args.filePath[:-5] + '_CLEAN.csv')

    print('DONE.')

def add_args(parser):
    """Add command line options for customized data preprocessing."""
    parser.add_argument('filePath', metavar='filePath', type=str, help='Path to uncleaned data file')
    parser.add_argument('-a', '--all', action='store_const', const='a', help=text.options['-a'])
    parser.add_argument('-c', '--categorical', action='store_const', const='c', help=text.options['-c'])
    parser.add_argument('-i', '--interpolate', action='store_const', const='i', help=text.options['-i'])
    parser.add_argument('-m', '--missing', action='store_const', const='m', help=text.options['-m'])
    parser.add_argument('-o', '--outliers', action='store_const', const='o', help=text.options['-o'])
    parser.add_argument('-v', '--version', action='version', version='v1.0.0')

def main():
    """Create command line argument parser and call clean for preprocessing."""
    parser = argparse.ArgumentParser(description=text.description)
    add_args(parser)
    args = parser.parse_args()
    clean(args) # clean data according to user-supplied options

if __name__ == '__main__':
    main()