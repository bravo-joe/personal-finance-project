# Beginning of "data_migration.py"
# Import necessary libraries and modules
from io import StringIO
from process_day_column import process_day_col
import pandas as pd
import psycopg2
import yaml
import os
import time

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
# Change the current working
os.chdir(script_dir)

# Read the config file
with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

conn = psycopg2.connect(
    f"host={config["server"]["host"]} \
    dbname={config["database"]["name"]} \
    user={config["database"]["user"]} \
    password={config["database"]["password"]} \
    "
)

# To issue queries to the server
cur = conn.cursor()

# Execute commands on the postgres db
cur.execute(open(config["directories"]["tbl_schema"], "r").read())

# Commit changes to db
# conn.commit()

# Retrieve csv and clean up the data
raw_data = pd.read_csv(config["directories"]["csv_file"])
raw_data['date'] = pd.to_datetime(raw_data['date']).dt.date
df = process_day_col(raw_data)
df.insert(0, 'txn_id', range(len(df)))

start_time = time.time() # Get start time before insert

sio = StringIO()
df.to_csv(sio, index=None, header=None)
sio.seek(0)
with conn.cursor() as c:
    c.copy_expert(
        sql=f"""
    COPY {config["database"]["table"]} (
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

# End of "data_migration.py"
