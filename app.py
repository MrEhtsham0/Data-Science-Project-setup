from src.mlops_project_setup.logger import logging
from src.mlops_project_setup.exception import CustomException
import sys
from src.mlops_project_setup.components.data_ingestion import DataIngestion,DataIngestionConfig
from src.mlops_project_setup.components.data_transformation import DataTransformationConfig,DataTransformation
from src.mlops_project_setup.components.model_trainer import ModelTrainer,ModelTrainerConfig
from src.mlops_project_setup.utils import save_model

if __name__=="__main__":
    logging.info("Ehtsham khaliq ")
    try:
        # data_ingestion_config = DataIngestionConfig()
        data_ingestion=DataIngestion()
        train_datapath,test_datapath = data_ingestion.init_data_ingestion()
        # data_tranformation_config = DataTransormationConfig()
        data_transformation=DataTransformation()
        train_arr,test_arr,_ = data_transformation.initiate_data_transormation(train_datapath,test_datapath)
        #data training
        model_trainer = ModelTrainer() 
        print(model_trainer.initiate_model_trainer(train_arr,test_arr)) 
    except Exception as e:
        logging.info("Custom exception")
        raise CustomException(e,sys)