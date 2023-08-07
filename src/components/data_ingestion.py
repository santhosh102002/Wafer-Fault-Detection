import pandas as pd
import os
from dataclasses import dataclass
from src.exception import CustomException
from src.logger import logging
import sys
from src.utils.main_utils import MainUtils
from sklearn.model_selection import train_test_split
from dotenv import load_dotenv
load_dotenv()

@dataclass
class DataIngestionConfig:
    raw_data_path = os.path.join('artifacts','raw.csv')
    train_data_path = os.path.join('artifacts','train.csv')
    test_data_path = os.path.join('artifacts','test.csv')

class DataIngestion:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        logging.info('Data Ingestion started')
        try:
            df : pd.DataFrame = MainUtils.export_collection_as_dataframe( os.getenv("WAFER_DB"),
                                          os.getenv("WAFER_COLLECTION"))
            logging.info('Exported collection as dataframe')

            os.makedirs(os.path.dirname(self.data_ingestion_config.raw_data_path),exist_ok=True)
            df.to_csv(self.data_ingestion_config.raw_data_path,index=False,header=True)
            train_set,test_set = train_test_split(df,test_size=0.20,random_state=50)
            train_set.to_csv(self.data_ingestion_config.train_data_path,index = False,header=True)
            test_set.to_csv(self.data_ingestion_config.test_data_path,index=False,header=True)
            logging.info(f'The dataingested from mongodb to {self.data_ingestion_config.raw_data_path}')

            logging.info('Exited initiate_data_ingestion method of DataIngestion class')
            return(
               
                self.data_ingestion_config.train_data_path,
                self.data_ingestion_config.test_data_path
            )

            
        except Exception as e:
            return CustomException(e,sys)

    