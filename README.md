# exploratory_data_analysis_helper
helper script that takes a csv and does exploratory data analysis using [pandas_profiling](https://github.com/pandas-profiling/pandas-profiling).
`pandas_profiling` is excellent but sometimes you have a dataset that needs a little cleanup in pandas before `pandas_profiling` will work nicely with it.  This is just a little helper script to let you write a line or two of code to fix import errors that come up (e.g., data formatting).

So if `pandas_profiling --config_file config.yaml [YOUR_FILE.csv]` fails, I use this.

# to run
`pipenv run python3 profiling.py 'YOUR_FILE.csv'`
