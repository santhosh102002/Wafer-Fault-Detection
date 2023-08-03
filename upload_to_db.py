from pymongo.mongo_client import MongoClient
import json
import pandas as pd

url = "mongodb+srv://santhoshNode:santhoshNode@cluster0.ofceqbd.mongodb.net/"

client = MongoClient(url)

DATABASE = "waferDB"
COLLECTION = "WaferCollection"

df = pd.read_csv(r"E:\WAFER_FAULT_DETECTION\notebooks\wafer_data.csv")
df.drop(['Unnamed: 0'],axis=1,inplace=True)
json_record = list(json.loads(df.T.to_json()).values())

client[DATABASE][COLLECTION].insert_many(json_record)
