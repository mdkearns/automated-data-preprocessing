# make_clean is a command line utility program that automatically
# performs common data preprocessing tasks on your uncleaned data sets.

# Usage: python make_clean.py [options] /file/path/to/data/

import argparse
import sys
import output

def main():

    parser = argparse.ArgumentParser(description=output.description)

    # if sys.argv[-1] == '--help':
    #     print(output.info)
    #     print(output.description)
    #     print(output.usage)


if __name__ == '__main__':
    main()