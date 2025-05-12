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
# import numpy as np
# np.random.seed(1234)
import pandas as pd
from io import StringIO
import time

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

# Part 3: Create dataframes and concatenate
##################################################################################
# Will call the functions and store them as dataframes, then join all three
# dataframes.
##################################################################################
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
# print(df3)

# Adding the txn_id which also works as a primary key (column).
df3.insert(0, 'txn_id', range(len(df3)))

# Will add the final amount column
processed_df = df3
processed_df['Amount'] = processed_df['Category'].map(amount)

# Part 3: Open connection to database
##################################################################################
# Will use the configuration file to open a connection to Postgres and populate a
# new table.
##################################################################################
# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
# Change the current working
os.chdir(script_dir)
# Read the config file
with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)
conn = psycopg2.connect(
    f"host={config["server"]["host"]} \
    dbname={config["synth_data"]["database"]} \
    user={config["database"]["user"]} \
    password={config["database"]["password"]} \
    "
)
# To issue queries to the server
cur = conn.cursor()
# Execute commands on the postgres db
cur.execute(
    f"""CREATE TABLE IF NOT EXISTS {config["synth_data"]["tbl_name"]} (
        txn_id SERIAL PRIMARY key
        , date DATE NOT NULL
        , day VARCHAR NOT NULL
        , description VARCHAR NOT NULL
        , category VARCHAR NOT NULL
        , amount FLOAT NOT  NULL
        );
    """
)
# Retrieve csv and clean up the data
# raw_data = pd.read_csv(config["directories"]["csv_file"])
# raw_data['date'] = pd.to_datetime(raw_data['date']).dt.date

start_time = time.time() # Get start time before insert

sio = StringIO()
processed_df.to_csv(sio, index=None, header=None)
sio.seek(0)
with conn.cursor() as c:
    c.copy_expert(
        sql=f"""COPY {config["synth_data"]["tbl_name"]} (
                txn_id,
                date,
                day,
                description,
                category,
                amount
                ) FROM STDIN WITH CSV
            """,
        file=sio
    )
# Commit the changes
conn.commit()
end_time = time.time() # Get end time after insert
total_time = end_time - start_time # Calculate the time difference
print(f"Insert time: {total_time} seconds") # Print time
#Close the connection
conn.close()

# End of "creating_synthetic_data.py"
