from pymongo.mongo_client import MongoClient
import os,sys
import pandas as pd
import numpy as np
# import boto3
from src.exception import CustomException
import dill
from dotenv import load_dotenv
load_dotenv()



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

def save_obj(file_path,obj):
    try:
        dirname = os.path.dirname(file_path)
        os.makedirs(dirname,exist_ok=True)

        with open(file_path,'wb') as file_obj:
            dill.dump(obj,file_obj)
    except Exception as e:
        raise CustomException(e,sys)
   

