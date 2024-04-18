import os
import sys
from dataclasses import dataclass
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from src.mlops_project_setup.exception import CustomException
from src.mlops_project_setup.logger import logging
from src.mlops_project_setup.utils import save_model


@dataclass
class DataTransormationConfig:
    preprocessor_file_path = os.path.join("artifacts","preprocessor.pkl")
class DataTransormation:
    def __init__(self):
        self.transormation=DataTransormationConfig()
    def data_transormation(self):
        try:
            numerical_cols = ["writing_score","reading_score"]
            categorical_cols = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",	
                "lunch",
                "test_preparation_course"
            ]
            num_pipeline = Pipeline(steps=[
                ("imputer", SimpleImputer(strategy="median")),
                ("scaler", StandardScaler())
            ])
            cat_pipeline = Pipeline(steps=[
                ("imputer", SimpleImputer(strategy='most_frequent')),
                ("onehot", OneHotEncoder()),
                ("scalar",StandardScaler(with_mean=False))
            ])
            logging.info(f"Categorical columns:{cat_pipeline}")
            logging.info(f"Numerical columns:{num_pipeline}")
            preprocessor = ColumnTransformer(transformers=[
                ("num_pipeline", num_pipeline, numerical_cols),
                ("cat_pipeline", cat_pipeline, categorical_cols)
            ])
            return preprocessor
        except Exception as e:
            raise CustomException(e,sys)
    def initiate_data_transformation(self,train_path,test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            logging.info("reading train and test files...")
            preprocessor = self.data_transormation()
            target_col = "math_score"
            numerical_cols = ["writing_score","reading_score"]
            #train data
            input_feature_train_df = train_df.drop(columns=[target_col],axis=1) 
            target_feature_train_df = train_df[target_col]
            #test data set
            input_feature_test_df = test_df.drop(columns=[target_col],axis=1) 
            target_feature_test_df = test_df[target_col]
            logging.info("Applying processing on training data...") 
            #trainign the dataa
            input_feature_train_arr = preprocessor.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessor.transform(input_feature_test_df)
            #saving as array
            train_arr = np.c_[
                input_feature_train_arr, np.array(input_feature_train_df)
            ]
            test_arr = np.c_[
                input_feature_test_arr, np.array(input_feature_test_df)
            ]
            logging.info("Saving the preprocessed data...")
            save_model(
                file_path=self.transormation.preprocessor_file_path,
                obj=preprocessor
            )
            return(
                train_arr,
                test_arr,
                self.transormation.preprocessor_file_path
            )
            
        except Exception as e:
            raise CustomException(e,sys)
        