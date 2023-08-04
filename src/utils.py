from pymongo.mongo_client import MongoClient
import os
import pandas as pd
import numpy as np


DATABASE = "waferDB"
COLLECTION = "WaferCollection"

url = "mongodb+srv://santhoshNode:santhoshNode@cluster0.ofceqbd.mongodb.net/"
def export_collection_as_dataframe(db_name,collection_name):
    client = MongoClient(url)
    collection = client[db_name][collection_name]
    df = pd.DataFrame(list(collection.find()))
    # print(list(df.find()))
    if '_id' in df.columns.to_list():
        df.drop('_id',axis=1,inplace=True)
    df.replace({'na':np.nan},inplace =True)
    return df

df = export_collection_as_dataframe(db_name=DATABASE,collection_name=COLLECTION)
print(df)