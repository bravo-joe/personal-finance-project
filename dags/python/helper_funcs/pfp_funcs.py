# Beginning of "pfp_funcs.py"

def plot1_conn(config_loc="../config_files/config.yaml"):
    import psycopg2
    import pandas as pd
    import yaml
    # Read the config file
    with open(config_loc, "r") as file:
        config = yaml.safe_load(file)

    # Create a connection to db server
    conn = psycopg2.connect(
        f"host={config["server"]["host"]} \
        dbname={config["database"]["name"]} \
        user={config["database"]["user"]} \
        password={config["database"]["password"]} \
        "
    )
    # Define query
    query_1 = "SELECT * FROM dec_2023;"
    plot_1 = pd.read_sql_query(query_1, conn)
    conn.close()
    plot_1 = plot_1.drop(columns=['txn_id', 'date', 'day', 'description'])
    plot_1 = plot_1.groupby('category', as_index=False).sum()
    plot_1 = plot_1.sort_values(by='amount', ascending=False)
    plot_1.to_csv('/home/joebravo/airflow/dags/data/plot1_data.csv', index=False)

def plot2_conn(config_loc):
    import psycopg2
    import pandas as pd
    import yaml
    # Read the config file
    with open(config_loc, "r") as file:
        config = yaml.safe_load(file)
    # Create a connection to db server
    conn = psycopg2.connect(
        f"host={config["server"]["host"]} \
        dbname={config["database"]["name"]} \
        user={config["database"]["user"]} \
        password={config["database"]["password"]} \
        "
    )
    # Time series query
    query_1 = "SELECT * FROM dec_2023;"
    
    plot_2 = pd.read_sql_query(query_1, conn)
    table_1 = pd.read_sql_query(query_1, conn)
    conn.close()
    plot_2 = rm_plot2_cols(plot_2)
    plot_2.to_csv('/home/joebravo/airflow/dags/data/plot2_data.csv', index=False)
    table_1.to_csv('/home/joebravo/airflow/dags/data/table1_data.csv', index=False)

def plot3_conn(config_loc):
    import psycopg2
    import pandas as pd
    import yaml
    # Read the config file
    with open(config_loc, "r") as file:
        config = yaml.safe_load(file)
    # Create a connection to db server
    conn = psycopg2.connect(
        f"host={config["server"]["host"]} \
        dbname={config["database"]["name"]} \
        user={config["database"]["user"]} \
        password={config["database"]["password"]} \
        "
    )
    # Time series query
    query_2 = "SELECT date, SUM(amount) \
        FROM dec_2023 \
        GROUP BY date \
        ORDER BY date ASC;"
    
    plot_3 = pd.read_sql_query(query_2, conn)
    conn.close()
    plot_3.to_csv('/home/joebravo/airflow/dags/data/plot3_data.csv', index=False)

def plot4_conn(config_loc):
    import psycopg2
    import pandas as pd
    import yaml
    # Read the config file
    with open(config_loc, "r") as file:
        config = yaml.safe_load(file)
    # Create a connection to db server
    conn = psycopg2.connect(
        f"host={config["server"]["host"]} \
        dbname={config["database"]["name"]} \
        user={config["database"]["user"]} \
        password={config["database"]["password"]} \
        "
    )
    # Time series query
    query_1 = "SELECT * FROM dec_2023;"
    
    plot_4 = pd.read_sql_query(query_1, conn)
    conn.close()
    plot_4 = process_plot4(plot_4)
    plot_4.to_csv('/home/joebravo/airflow/dags/data/plot4_data.csv', index=False)

def rm_plot2_cols(df):
    """Helper function to remove unnecessary columns for plot 2."""
    #Using the 'drop' method
    df = df.drop(columns=['txn_id', 'date', 'day', 'description'])
    return df

def process_plot4(df):
    """All the processing for plot 4."""
    # Total spent
    total_spent = df['amount'].sum().round(2)
    # Remove unnecessary columns
    df = df.drop(columns=['txn_id', 'date', 'day', 'category'])
    # Group By
    df = df.groupby('description', as_index=False).sum()
    # Compute new column
    df['proportion'] = df.apply(lambda row: row['amount'] / total_spent, axis=1)
    df = df.sort_values(by='proportion', ascending=True)
    # df = df.tail(20)
    return df

# End of "pfp_helper_funcs.py"