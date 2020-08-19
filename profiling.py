# note you could use `pandas_profiling --config_file config.yaml [YOUR_FILE.csv]` but this gives you flexibility to play with pandas import with dirty data
# so run this as `pipenv run python3 profiling.py 'YOUR_FILE.csv'`

import sys
import csv
import pandas as pd
from pandas_profiling import ProfileReport


def load_csv(local_filename):
    df = pd.read_csv(local_filename, encoding='unicode_escape')
    return df


def run_profiling(df):
    prof = ProfileReport(df)
    return prof


def export_profiling(prof):
    prof.to_file(output_file='output.html')


if __name__ == '__main__':
    local_filename = sys.argv[1]
    df = load_csv(local_filename)
    prof = run_profiling(df)
    export_profiling(prof)
