# Beginning of "process_day_column.py"
# Import all necessary libraries and module
import pandas as pd

def process_day_col(df):
    """Helper function to make all strings in day column lower case."""
    df['day'] = df['day'].str.lower()
    return df

# End of "process_day_column.py"