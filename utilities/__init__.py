# utility functions for data preprocessing

from numpy import nan
from pandas import read_csv, get_dummies

def load_csv(filePath, missing_headers=False):
    """Read data as csv and return as pandas data frame."""

    if missing_headers:
        print(filePath, 'doesn\'t contain field names.\n')
        data = read_csv(filePath, header=None)
    else:
        print(filePath, 'contains field names.\n')
        data = read_csv(filePath, header=0)

    return data

def one_hot_encode(data):
    """Perform a one-hot encoding and return as pandas data frame."""

    return get_dummies(data)

def impute_missing_data(data):
    """Impute missing data values and return as pandas data frame."""

    # strip whitespace from data
    data = data.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

    # replace missing values with the sentinel NaN value
    data = data.replace('?', nan)

