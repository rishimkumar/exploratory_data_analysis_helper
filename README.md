# exploratory_data_analysis_helper
helper script that takes a csv and does EDA using pandas_profiling. 
note you could always just use `pandas_profiling --config_file config.yaml [YOUR_FILE.csv]` but this gives you flexibility to play with pandas import with dirty data (e.g., strfdate)

# to run
`pipenv run python3 profiling.py 'YOUR_FILE.csv'`
