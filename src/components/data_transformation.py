from dataclasses import dataclass
import os,sys
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import FunctionTransformer
from sklearn.preprocessing import RobustScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
import numpy as np
import pandas as pd
from imblearn.combine import SMOTETomek
from imblearn.over_sampling import SMOTE
from src.utils import save_obj
from src.exception import CustomException
from sklearn.model_selection import train_test_split

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts','preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()
    def data_transformation_obj(self):
        try:
            
            # define custom function to replace 'NA' with np.nan
            replace_na_with_nan = lambda X: np.where(X == 'na', np.nan, X)

            # define the steps for the preprocessor pipeline
            # nan_replacement_step = 
            # imputer_step = 
            # scaler_step = 

            pipeline = Pipeline(
                steps=[
                ('nan_replacement', FunctionTransformer(replace_na_with_nan)),
                ('imputer', SimpleImputer(strategy='median')),
                ('scaler', RobustScaler())
                ]
            )
            
            return pipeline

        except Exception as e:
            raise CustomException(e, sys)
    def initiate_data_transformation(self,train_path,test_path):

        try:
            train_df = pd.read_csv(train_path)
            # df = pd.read_csv(raw_path)
           
            test_df = pd.read_csv(test_path)
 
            pipeline = self.data_transformation_obj()

            target_column_name = "Good/Bad"
            target_column_mapping = {-1.0: 1, 1.0: 0}

            #training dataframe
            input_feature_train_df = train_df.drop(columns=[target_column_name],axis=1)
         
            target_feature_train_df = train_df[target_column_name].map(target_column_mapping)
     

            # testing dataframe
            input_feature_test_df = test_df.drop(columns=[target_column_name],axis=1)
            target_feature_test_df = test_df[target_column_name].map(target_column_mapping)
            input_columns = []
            for column in input_feature_train_df.columns:
                input_columns.append(column)
            preprocessor = ColumnTransformer([('pipeline',pipeline,input_columns)])

            transformed_input_train_feature = preprocessor.fit_transform(input_feature_train_df)


            transformed_input_test_feature =preprocessor.transform(input_feature_test_df)

            smt = SMOTE(sampling_strategy="minority",k_neighbors=1)
   
           
            input_feature_train_final, target_feature_train_final = smt.fit_resample(transformed_input_train_feature, target_feature_train_df)  #smt.fit_resample(
            #)

            input_feature_test_final, target_feature_test_final = smt.fit_resample(transformed_input_test_feature, target_feature_test_df)
             #) smt.fit_resample(

            # print(pd.DataFrame(target_feature_train_final).value_counts())
            # print(pd.DataFrame(target_feature_test_final).value_counts())
           
                

            train_arr = np.c_[input_feature_train_final, np.array(target_feature_train_final) ]
            test_arr = np.c_[ input_feature_test_final, np.array(target_feature_test_final) ]

            save_obj(self.data_transformation_config.preprocessor_obj_file_path,
                        obj= preprocessor)
        
            

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            )
        except Exception as e:
            raise CustomException(e,sys)
