# utility functions for data preprocessing

from pandas import read_csv, get_dummies

def load_csv(filePath, missing_headers=False):
    """Read data as csv and return as pandas dataframe."""

    if missing_headers:
        print(filePath, 'doesn\'t contain field names.\n')
        data = read_csv(filePath, header=None)
    else:
        print(filePath, 'contains field names.\n')
        data = read_csv(filePath, header=0)

    return data

def one_hot_encode(data):
    """Perform a one-hot encoding and return as pandas dataframe."""

    return get_dummies(data)

