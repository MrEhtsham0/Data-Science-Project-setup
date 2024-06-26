import os
import sys
from src.mlops_project_setup.exception import CustomException
from src.mlops_project_setup.logger import logging
import pandas as pd
from dotenv import load_dotenv
import pymysql
import pickle
import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score


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
        df.columns = df.iloc[0]
        df = df[1:]
        df.reset_index(drop=True, inplace=True)
        print(df.head())
        return df
    except Exception as ex:
        # Properly handle exceptions
        logging.error("Error occurred while reading SQL data: {}".format(ex))
        raise CustomException(ex, sys)
def evaluate_models(X_train, y_train,X_test,y_test,models,param):
    try:
        report = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]
            para=param[list(models.keys())[i]]

            gs = GridSearchCV(model,para,cv=3)
            gs.fit(X_train,y_train)

            model.set_params(**gs.best_params_)
            model.fit(X_train,y_train)

            #model.fit(X_train, y_train)  # Train model

            y_train_pred = model.predict(X_train)

            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)

            test_model_score = r2_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = test_model_score

        return report

    except Exception as e:
        raise CustomException(e, sys)
def save_model(file_path,obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        with open(file_path, 'wb') as file:
            pickle.dump(obj, file)
        logging.info("Saving the pickle model")
    except Exception as e:
        raise CustomException(e,sys)