from pymongo.mongo_client import MongoClient
import json
import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv()

client = MongoClient(os.getenv("MONGO_URL"))


df = pd.read_csv(r"E:\WAFER_FAULT_DETECTION\notebooks\wafer_data.csv")
df.drop(['Unnamed: 0'],axis=1,inplace=True)
json_record = list(json.loads(df.T.to_json()).values())

client[os.getenv("WAFER_DB")][os.getenv("WAFER_COLLECTION")].insert_many(json_record)
