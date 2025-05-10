# Beginning of "creating_synthetic_data.py"
# Part 1: Import all necessary libraries and modules
##################################################################################
# Will comment out the libraries that I feel confident I do not need.
# Once I run the script, will determine the rest of the libraries that I do not
# need. Will then delete all the commented lines.
##################################################################################
from pathlib import Path
import os
# import re # Regular expression library also for removing apostrophes
import psycopg2 # To handle connection to postgresql
import yaml # For configuration file
# import matplotlib.pyplot as plt
import numpy as np
np.random.seed(1234)
import pandas as pd

# Some custom helper functions
from helper_funcs.pfp_helper_funcs import (
    rm_plot2_cols,
    process_plot4
)
from helper_funcs.synth_data_funcs import (
    desc_and_cat,
    necessities,
    date_day_df,
    create_desc_cat_df,
    amount
)

# Part 2: Declare some global variables
##################################################################################
# Initially global variables, will then be moved to import from a configuration
# file that is shared with the other scripts.
##################################################################################
# Number of records
num_data_pts = 150

# Start and end date
start_date = '2023-12-01'
end_date = '2023-12-31'

# Date and day dataframe
df1 = date_day_df(
    start_date,
    end_date,
    num_data_pts
)

df2 = create_desc_cat_df(
    num_data_pts,
    desc_and_cat
)

df3 = pd.concat(
    [df1, df2], 
    axis=1
)
print(df3)

# End of "creating_synthetic_data.py"
