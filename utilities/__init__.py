# utility functions for data preprocessing

from numpy import nan, zeros
from pandas import read_csv, get_dummies, Series

def load_csv(filePath, missing_headers=False):
    """Read data as csv and return as pandas data frame."""

    if missing_headers:
        data = read_csv(filePath, header=None)
    else:
        data = read_csv(filePath, header=0)

    # make shape of data frame global
    global rows, cols
    rows, cols = data.shape

    return data

def one_hot_encode(data):
    """Perform a one-hot encoding and return as pandas data frame."""

    return get_dummies(data)

def replace_missing_data(data):
    """replace missing data values and return as pandas data frame."""

    # strip whitespace from data
    data = data.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

    # replace missing values with the sentinel NaN value
    data = data.replace('?', nan)

    # get missing field count
    nan_vals = dict(data.count(axis=1))
    nan_vals = {key: value for (key, value) in nan_vals.items() if value < cols-2}

    # remove samples with more than one missing field
    data = data.drop(index=nan_vals.keys())

    return data

def interpolate_missing_data(data, real, discrete):
    """Interpolate missing data and return as pandas data frame."""

    # get mean of real-valued fields and mode for categorical fields
    mode = data.mode().values.flatten()
    mean = data.mean().values.flatten()

    # keep ONLY the categorical modes
    mode = [x for x in mode.copy() if type(x) == str]

    replacements = list(zeros(15))

    # get mean replacements for continuous fields
    j = 0
    for index in real:
        replacements[index] = mean[j]
        j += 1

    # get mode replacements for discrete fields
    j = 0
    for index in discrete:
        replacements[index] = mode[j]
        j += 1

    # fill NaN values with mode (discrete fields) and mean (continuous fields)
    data = data.fillna(Series(replacements))

    return data

def remove_outliers(data):
    """Remove outliers from data and return as a pandas data frame."""
    return data


