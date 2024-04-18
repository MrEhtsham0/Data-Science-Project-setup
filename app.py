from src.mlops_project_setup.logger import logging
from src.mlops_project_setup.exception import CustomException
import sys
from src.mlops_project_setup.components.data_ingestion import DataIngestion,DataIngestionConfig
from src.mlops_project_setup.components.data_transformation import DataTransormation,DataTransormationConfig

if __name__=="__main__":
    logging.info("Ehtsham khaliq ")
    try:
        # data_ingestion_config = DataIngestionConfig()
        data_ingestion=DataIngestion()
        train_datapath,test_datapath = data_ingestion.init_data_ingestion()
        # data_tranformation_config = DataTransormationConfig()
        data_transformation=DataTransormation()
        data_transformation.initiate_data_transformation(train_datapath,test_datapath)
    except Exception as e:
        logging.info("Custom exception")
        raise CustomException(e,sys)