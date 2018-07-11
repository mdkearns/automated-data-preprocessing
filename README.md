# Automated Data Preprocessing

A command-line utility program for automating the trivial, frequently occurring data preparation tasks: missing value interpolation, outlier removal, and encoding categorical variables.

- Identify missing values in the data set and replace them with the sentinel NaN value.
- Interpolate missing values using mean for continuous features, mode for discrete features.
- Remove outliers on the assumption that the distribution of the field values follow a normal distribution.
- Encode categorical features using a one-hot encoding schema.

## Getting Started

For a copy of the command-line utility program, simply clone the repository by running:

```
git clone https://github.com/mdkearns/automated-data-preprocessing
```

inside of the directory where you would like to store the program.

### Prerequisites

This program relies on having the NumPy and Pandas Python packages.
You can use pip to install the prerequisites for this program as follows:

```
pip install -r requirements.txt
```

### Running

You can use the program by running

```
python make_clean.py [options] path/to/your/data
```

Running

```
python make_clean.py --help
```

has the output

```
usage: make_clean.py [-h] [-a] [-c] [-i] [-m] [-o] [-v] filePath

The make_clean command line utility program automatically performs common data
preprocessing tasks on your uncleaned data sets.

positional arguments:
  filePath           Path to uncleaned data file

optional arguments:
  -h, --help         show this help message and exit
  -a, --all          all
  -c, --categorical  file contains categorical data
  -i, --interpolate  interpolate missing values
  -m, --missing      file is missing field names
  -o, --outliers     outlier detection and removal
  -v, --version      show program's version number and exit
  ```

## Versioning

We use [SemVer](http://semver.org/) for versioning.

## Authors

* **Matthew D. Kearns** - *Initial work* - [mdkearns](https://github.com/mdkearns)

See also the list of [contributors](https://github.com/automated-data-preprocessing/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgements

Thanks to [PurpleBooth](https://github.com/PurpleBooth) for the gist providing a helpful README.md template. If you like the template and would like to use it for your project, it can be found [here](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2).
