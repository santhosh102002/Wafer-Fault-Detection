import sys
from typing import Dict, Tuple
import os
import pandas as pd
# import pickle
import dill
import yaml
# import boto3

# from src.constant import *
from src.exception import CustomException
from src.logger import logging
from pymongo.mongo_client import MongoClient
import os,sys
import pandas as pd
import numpy as np
# import boto3

import dill
from dotenv import load_dotenv
load_dotenv()
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


class MainUtils:
    def __init__(self) -> None:
        pass

    def read_yaml_file(self, filename: str) -> dict:
        try:
            with open(filename, "rb") as yaml_file:
                return yaml.safe_load(yaml_file)

        except Exception as e:
            raise CustomException(e, sys) from e

    def read_schema_config_file(self) -> dict:
        try:
            schema_config = self.read_yaml_file(os.path.join("config", "schema.yaml"))

            return schema_config

        except Exception as e:
            raise CustomException(e, sys) from e

    

    @staticmethod
    def save_object(file_path: str, obj: object) -> None:
        logging.info("Entered the save_object method of MainUtils class")

        try:
            with open(file_path, "wb") as file_obj:
                dill.dump(obj, file_obj)

            logging.info("Exited the save_object method of MainUtils class")

        except Exception as e:
            raise CustomException(e, sys) from e

    

    @staticmethod
    def load_object(file_path: str) -> object:
        logging.info("Entered the load_object method of MainUtils class")

        try:
            with open(file_path, "rb") as file_obj:
                obj = dill.load(file_obj)

            logging.info("Exited the load_object method of MainUtils class")

            return obj

        except Exception as e:
            raise CustomException(e, sys) from e
   
    # @staticmethod     
    # def load_object(file_path):
    #     try:
    #         with open(file_path,'rb') as file_obj:
    #             return dill.load(file_obj)
    #     except Exception as e:
    #         logging.info('Exception Occured in load_object function utils')
    #         raise CustomException(e,sys)
    @staticmethod
    def export_collection_as_dataframe(db_name,collection_name):
        try:
            client = MongoClient(os.getenv("MONGO_URL"))
            collection = client[db_name][collection_name]
            df = pd.DataFrame(list(collection.find()))
            # print(list(df.find()))
            if '_id' in df.columns.to_list():
                df.drop('_id',axis=1,inplace=True)
            df.replace({'na':np.nan},inplace =True)
            return df
        except Exception as e:
            raise CustomException(e,sys)
    @staticmethod
    def evaluate_models(X, y, models):
        try:
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.20, random_state=30
            )

            report = {}

            for i in range(len(list(models))):
                model = list(models.values())[i]

                model.fit(X_train, y_train)  # Train model

                y_train_pred = model.predict(X_train)

                y_test_pred = model.predict(X_test)

                train_model_score = accuracy_score(y_train, y_train_pred)

                test_model_score = accuracy_score(y_test, y_test_pred)

                report[list(models.keys())[i]] = test_model_score

            return report

        except Exception as e:
            raise CustomException(e, sys)
   

    





# def save_obj(file_path,obj):
#     try:
#         dirname = os.path.dirname(file_path)
#         os.makedirs(dirname,exist_ok=True)

#         with open(file_path,'wb') as file_obj:
#             dill.dump(obj,file_obj)
#     except Exception as e:
#         raise CustomException(e,sys)
# def load_object(file_path):
#     try:
#         with open(file_path, "rb") as file_obj:
#             return dill.load(file_obj)

#     except Exception as e:
#         raise CustomException(e, sys)


    