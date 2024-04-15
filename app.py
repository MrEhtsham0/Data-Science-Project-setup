from src.mlops_project_setup.logger import logging
from src.mlops_project_setup.exception import CustomException
import sys
from src.mlops_project_setup.components.data_ingestion import DataIngestion,DataIngestionConfig

if __name__=="__main__":
    logging.info("Ehtsham khaliq ")
    try:
        # data_ingestion_config = DataIngestionConfig()
        data_ingestion=DataIngestion()
        data_ingestion.init_data_ingestion()
    except Exception as e:
        logging.info("Custom exception")
        raise CustomException(e,sys)