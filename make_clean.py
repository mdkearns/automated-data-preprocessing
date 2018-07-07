# make_clean is a command line utility program that automatically
# performs common data preprocessing tasks on your uncleaned data sets.

# Usage: python make_clean.py [options] /file/path/to/data/

import sys
import messages

def main():
    print(messages.welcome)
    print(sys.argv[1])

if __name__ == '__main__':
    main()