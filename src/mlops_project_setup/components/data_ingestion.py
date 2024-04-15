import os
import sys
from src.mlops_project_setup.exception import CustomException
from src.mlops_project_setup.logger import logging
import pandas as pd
from src.mlops_project_setup.utils import read_sql_data
from sklearn.model_selection import train_test_split

from dataclasses import dataclass
@dataclass
class DataIngestionConfig:
    train_datapath = os.path.join('artifacts','train.csv')
    test_datapath = os.path.join('artifacts','test.csv')
    raw_datapath = os.path.join('artifacts','raw.csv')

class DataIngestion:
    def __init__(self) -> None:
        self.ingestion=DataIngestionConfig()
    def init_data_ingestion(self):
        try:
            df=read_sql_data()
            logging.info("Reading from mysql database")
            os.makedirs(os.path.dirname(self.ingestion.train_datapath),exist_ok=True)
            df.to_csv(self.ingestion.raw_datapath,index=False,header=True)
            train_set,test_set = train_test_split(df,test_size=0.2,random_state=42)
            df.to_csv(self.ingestion.train_datapath,index=False,header=True)
            df.to_csv(self.ingestion.test_datapath,index=False,header=True)

        except Exception as e:
            raise CustomException(e,sys)

