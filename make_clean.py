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
    parser.add_argument('-a', help='All')

    args = parser.parse_args()

    # if sys.argv[-1] == '--help':
    #     print(output.info)
    #     print(output.description)
    #     print(output.usage)


if __name__ == '__main__':
    main()