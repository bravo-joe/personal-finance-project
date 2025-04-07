# Beginning of "personal_expenses_dashboard.py"
from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from airflow.operators.python import PythonOperator
from pathlib import Path
from datetime import datetime, timedelta
# Custom functions
# from python.helper_funcs.rm_spcl_char import remove_apostrophe
# from python.helper_funcs.csv_to_sql import generate_insert_queries
from python.helper_funcs.pfp_funcs import (
    plot1_conn,
    plot2_conn,
    plot3_conn,
    plot4_conn
)
# Store dag_id in global variable
DAG_ID = Path(__file__).stem
# File location
CONFIG_LOC = "/home/joebravo/airflow/dags/python/config_files/config.yaml"

# CSV_FILE_PATH = "/home/joebravo/airflow/dags/data/DEC_2023.csv"
# READ_LOC = "/home/joebravo/airflow/dags/data/DEC_2023.csv"
# WRITE_LOC = "/home/joebravo/airflow/dags/data/DEC_2023_cleaned.csv"
SQL_LOC = "/home/joebravo/airflow/dags/sql/plot_1.sql"

# Instatiate the DAG
with DAG(
    dag_id = DAG_ID,
    description = 'Import from database to create Shiny app',
    start_date = datetime(2025, 4, 1),
    schedule_interval = "@once",
    catchup = False
) as dag:
    
    # Dummy Operator to begin the DAG (placeholder)
    start_dag = EmptyOperator(task_id = 'start_the_dag')
    
    plot1_data = PythonOperator(
        task_id = 'plot1',
        python_callable = plot1_conn,
        op_kwargs = {
            "config_loc": CONFIG_LOC
        }
    )

    plot2_data = PythonOperator(
        task_id = 'plot2',
        python_callable = plot2_conn,
        op_kwargs = {
            "config_loc": CONFIG_LOC
        }
    )
    
    plot3_data = PythonOperator(
        task_id = 'plot3',
        python_callable = plot3_conn,
        op_kwargs = {
            "config_loc": CONFIG_LOC
        }
    )
    
    plot4_data = PythonOperator(
        task_id = 'plot4',
        python_callable = plot4_conn,
        op_kwargs = {
            "config_loc": CONFIG_LOC
        }
    )

    tbl1_data = PythonOperator(
        task_id = 'table1',
        python_callable = plot2_conn,
        op_kwargs = {
            "config_loc": CONFIG_LOC
        }
    )

    # Dummy Operator to end the DAG
    final_task = EmptyOperator(task_id = 'end_of_dag')
    
    start_dag >> plot1_data >> final_task
    start_dag >> plot2_data >> final_task
    start_dag >> plot3_data >> final_task
    start_dag >> plot4_data >> final_task
    start_dag >> tbl1_data >> final_task

# End of "personal_expenses_dashboard.py"