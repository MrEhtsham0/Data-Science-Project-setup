import os
import sys
from src.mlops_project_setup.exception import CustomException
from src.mlops_project_setup.logger import logging
import pandas as pd
from dotenv import load_dotenv
import pymysql

load_dotenv()
host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
db = os.getenv('db')


def read_sql_data():
    logging.info("Reading SQL database started")
    try:
        mydb = pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db
        )
        logging.info("Connection Established: {}".format(mydb))  # Properly format the log message
        df = pd.read_sql_query('SELECT * FROM dataset', mydb)
        print(df.head())
        return df
    except Exception as ex:
        # Properly handle exceptions
        logging.error("Error occurred while reading SQL data: {}".format(ex))
        raise CustomException(ex, sys)
